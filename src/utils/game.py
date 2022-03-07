import curses

from ..config import CORRECT_LETTER_COLOR_PAIR_INDEX, EXISTS_LETTER_COLOR_PAIR_INDEX, INCORRECT_LETTER_COLOR_PAIR_INDEX, NORMAL_LETTER_COLOR_PAIR_INDEX, TILE_SIZE

from .screen import apply_color_pair, remove_color_pair

def generate_game_element(letter, correct=False, exists_in_answer=False, incorrect=False):
    return {'value': letter, 'correct': correct, 'exists_in_answer': exists_in_answer, 'incorrect': incorrect}


def pad_letter_with_spaces_to_match_tile_size(letter: str):
    return letter.center(TILE_SIZE)


def get_counting_dict(word):
    return {item: word.count(item) for item in set(word)}


# TODO: this function is not marking well, for an example for the guess 'where' (chosen word: crane), the first e will be yellow and the last e will be red
def get_word_letters_marked(word_letters_elements, chosen_word):
    marked_word_letters = [element for element in word_letters_elements]

    word_letters = [element['value'] for element in word_letters_elements]
    letters_count_in_chosen_word = get_counting_dict(chosen_word)

    # mark true letters first (green)
    for index, chosen_word_letter in enumerate(chosen_word):
        if word_letters[index] == chosen_word_letter and letters_count_in_chosen_word[chosen_word_letter] > 0:
            marked_word_letters[index]['correct'] = True
            letters_count_in_chosen_word[chosen_word_letter] -= 1

    # mark letters that exists in the chosen word
    for index, letter in enumerate(word_letters):
        if letter in chosen_word and letters_count_in_chosen_word[letter] > 0:
            marked_word_letters[index]['exists_in_answer'] = True
            letters_count_in_chosen_word[letter] -= 1

    # mark incorrect letters (doesnt exists in the chosen word)
    for index, marked_letter in enumerate(marked_word_letters):
        if marked_letter['correct'] == False and marked_letter['exists_in_answer'] == False:
            marked_word_letters[index]['incorrect'] = True

    return marked_word_letters


def draw_square(stdscr: 'curses._CursesWindow', i, j, element, board_size, offset):
    height, width = stdscr.getmaxyx()

    value, correct, exists_in_answer, incorrect = element['value'], element['correct'], element['exists_in_answer'], element['incorrect']

    if correct:
        apply_color_pair(stdscr, CORRECT_LETTER_COLOR_PAIR_INDEX)
    elif incorrect:
        apply_color_pair(stdscr, INCORRECT_LETTER_COLOR_PAIR_INDEX)
    elif exists_in_answer:
        apply_color_pair(stdscr, EXISTS_LETTER_COLOR_PAIR_INDEX)
    else:
        apply_color_pair(stdscr, NORMAL_LETTER_COLOR_PAIR_INDEX)

    x = int((width / 2) - TILE_SIZE * (board_size - 0.5 - 2 * i)) + offset
    y = int((height / 2) - (board_size - 0.5 - 2 * j))

    if y <= 0 or x <= 0 or x >= width or y >= height:
        raise Exception('board can\'t fit inside terminal size')

    padded_letter = pad_letter_with_spaces_to_match_tile_size(value)
    stdscr.addstr(y, x, padded_letter)

    remove_color_pair(stdscr, NORMAL_LETTER_COLOR_PAIR_INDEX)
    remove_color_pair(stdscr, CORRECT_LETTER_COLOR_PAIR_INDEX)
    remove_color_pair(stdscr, EXISTS_LETTER_COLOR_PAIR_INDEX)
    remove_color_pair(stdscr, INCORRECT_LETTER_COLOR_PAIR_INDEX)


def draw_game_board(stdscr: 'curses._CursesWindow', game_board, offset = 0):
    for row_index, row in enumerate(game_board):
        for col_index, element in enumerate(row):
            draw_square(stdscr, col_index, row_index, element, len(game_board), offset)
