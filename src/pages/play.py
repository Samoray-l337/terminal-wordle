import curses

import curses
from string import ascii_letters

from time import sleep

from ..config import BOARD_SIZE
from ..utils.game import draw_game_board

from ..top_bar import draw_top_bar


def generate_empty_game_board_array(size):
    return [[' ' for _ in range(size)] for _ in range(size)]


def play(stdscr: 'curses._CursesWindow'):
    game_board = generate_empty_game_board_array(BOARD_SIZE)

    current_word = 0
    current_letter = 0

    draw_game_board(stdscr, game_board)
    draw_top_bar(stdscr)

    while True:
        pressed_key = stdscr.getch()
        stdscr.clear()

        if pressed_key == ord('q'):
            break
        elif pressed_key == curses.KEY_BACKSPACE:
            current_letter -= 1

            game_board[current_word][current_letter] = ' '
            if current_letter < 0:
                current_letter = 0
        elif pressed_key in [ord(letter) for letter in ascii_letters]:
            game_board[current_word][current_letter] = chr(pressed_key)

            current_letter += 1
            if current_letter >= BOARD_SIZE:
                current_word += 1
                current_letter = 0

            if current_word >= BOARD_SIZE:
                break # End of the level, show score or something

        draw_game_board(stdscr, game_board)
        draw_top_bar(stdscr)

        stdscr.refresh()
