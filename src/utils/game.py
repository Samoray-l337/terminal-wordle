import curses

from ..config import CORRECT_LETTER_COLOR_PAIR_INDEX, EXISTS_LETTER_COLOR_PAIR_INDEX, MENU_SELECTED_COLOR_PAIR_INDEX, TILE_SIZE

from .screen import apply_color_pair, remove_color_pair

# support highlight in red color if incorrect
def generate_game_element(letter, correct=False, exists_in_answer=False):
    return {'value': letter, 'correct': correct, 'exists_in_answer': exists_in_answer}


def pad_letter_with_spaces_to_match_tile_size(letter: str):
    return letter.center(TILE_SIZE)


def get_counting_dict(word):
    return {item: word.count(item) for item in set(word)}


def get_word_letters_marked(word_letters_elements, chosen_word):
    marked_word_letters = []

    word_letters = [element['value'] for element in word_letters_elements]
    letters_count_in_chosen_word = get_counting_dict(chosen_word)

    for i in range(len(word_letters)):
        letter = word_letters[i]
        correct = False
        exists_in_answer = False

        if letter == chosen_word[i] and letters_count_in_chosen_word[letter] > 0:
            correct = True
            letters_count_in_chosen_word[letter] -= 1
        elif letter in chosen_word and letters_count_in_chosen_word[letter] > 0:
            exists_in_answer = True
            letters_count_in_chosen_word[letter] -= 1

        marked_letter = generate_game_element(letter, correct, exists_in_answer)
        marked_word_letters.append(marked_letter)

    return marked_word_letters


def draw_square(stdscr: 'curses._CursesWindow', i, j, element, board_size, offset):
    height, width = stdscr.getmaxyx()

    value, correct, exists_in_answer = element['value'], element['correct'], element['exists_in_answer']

    if correct:
        apply_color_pair(stdscr, CORRECT_LETTER_COLOR_PAIR_INDEX)
    elif exists_in_answer:
        apply_color_pair(stdscr, EXISTS_LETTER_COLOR_PAIR_INDEX)
    else:
        apply_color_pair(stdscr, MENU_SELECTED_COLOR_PAIR_INDEX)

    x = int((width / 2) - TILE_SIZE * (board_size - 0.5 - 2 * i)) + offset
    y = int((height / 2) - (board_size - 0.5 - 2 * j))

    if y <= 0 or x <= 0 or x >= width or y >= height:
        raise Exception('board can\'t fit inside terminal size')

    padded_letter = pad_letter_with_spaces_to_match_tile_size(value)
    stdscr.addstr(y, x, padded_letter)

    remove_color_pair(stdscr, MENU_SELECTED_COLOR_PAIR_INDEX)
    remove_color_pair(stdscr, CORRECT_LETTER_COLOR_PAIR_INDEX)
    remove_color_pair(stdscr, EXISTS_LETTER_COLOR_PAIR_INDEX)


def draw_game_board(stdscr: 'curses._CursesWindow', game_board, offset = 0):
    for row_index, row in enumerate(game_board):
        for col_index, element in enumerate(row):
            draw_square(stdscr, col_index, row_index, element, len(game_board), offset)
