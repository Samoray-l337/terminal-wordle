import curses

import curses
from string import ascii_lowercase

from ..utils.words import does_word_exists_inside_words_list

from ..config import BOARD_SIZE, CHOSEN_WORD, CTRL_BACKSPACE_VALUE, ENTER_KEY_OPTIONS
from ..utils.game import draw_game_board, generate_game_element, get_word_letters_marked

from ..top_bar import draw_top_bar


def draw_page(stdscr: 'curses._CursesWindow', game_board):
    draw_game_board(stdscr, game_board)
    draw_top_bar(stdscr)


def generate_empty_game_board_array(size):
    return [[generate_game_element(' ') for _ in range(size)] for _ in range(size)]


def play(stdscr: 'curses._CursesWindow'):
    game_board = generate_empty_game_board_array(BOARD_SIZE)

    current_word = 0
    current_letter = 0

    while True:
        stdscr.clear()
        draw_page(stdscr, game_board)

        pressed_key = stdscr.getch()
        if pressed_key == CTRL_BACKSPACE_VALUE:
            break

        if pressed_key in [ord(letter) for letter in ascii_lowercase]:
            if current_letter >= BOARD_SIZE:
                continue

            pressed_letter = chr(pressed_key)
            game_board[current_word][current_letter] = generate_game_element(pressed_letter, False, False)
            current_letter += 1
        elif pressed_key == curses.KEY_BACKSPACE:
            current_letter -= 1

            game_board[current_word][current_letter] = generate_game_element(' ')
            if current_letter < 0:
                current_letter = 0
        elif pressed_key in ENTER_KEY_OPTIONS:
            if current_letter == BOARD_SIZE:
                curr_word = ''.join([element['value']
                                    for element in game_board[current_word]])
                if not does_word_exists_inside_words_list(curr_word):
                    continue

                curr_word_marked = get_word_letters_marked(
                    game_board[current_word], chosen_word=CHOSEN_WORD)
                game_board[current_word] = curr_word_marked

                current_word += 1
                current_letter = 0

            if current_word == BOARD_SIZE:
                break

        stdscr.refresh()
