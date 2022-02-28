import curses

import curses
from string import ascii_letters

from ..config import BOARD_SIZE, CHOSEN_WORD, ENTER_KEY_OPTIONS
from ..utils.game import draw_game_board, generate_game_element, get_word_letters_marked

from ..top_bar import draw_top_bar


def generate_empty_game_board_array(size):
    return [[generate_game_element(' ') for _ in range(size)] for _ in range(size)]


def play(stdscr: 'curses._CursesWindow'):
    game_board = generate_empty_game_board_array(BOARD_SIZE)

    current_word = 0
    current_letter = 0

    draw_game_board(stdscr, game_board)
    draw_top_bar(stdscr)

    while True:
        pressed_key = stdscr.getch()
        stdscr.clear()

        # TODO: q letter for leaveing the level + q inside a word
        if pressed_key == ord('q'):
            break

        if pressed_key == curses.KEY_BACKSPACE:
            current_letter -= 1

            game_board[current_word][current_letter] = generate_game_element(' ')
            if current_letter < 0:
                current_letter = 0
        elif pressed_key in [ord(letter) for letter in ascii_letters]:
            if current_letter >= BOARD_SIZE:
                draw_game_board(stdscr, game_board)
                draw_top_bar(stdscr)
                continue

            pressed_letter = chr(pressed_key)
            game_board[current_word][current_letter] = generate_game_element(pressed_letter, False, False)
            current_letter += 1
        elif pressed_key in ENTER_KEY_OPTIONS:
            if current_letter == BOARD_SIZE:
                curr_word_marked = get_word_letters_marked(game_board[current_word], chosen_word=CHOSEN_WORD)
                game_board[current_word] = curr_word_marked

                current_word += 1
                current_letter = 0

            if current_word == BOARD_SIZE:
                break

        draw_game_board(stdscr, game_board)
        draw_top_bar(stdscr)

        stdscr.refresh()
