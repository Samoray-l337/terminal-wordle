import curses

import curses

from time import sleep

from pynput.keyboard import Key, Listener

from ..config import BOARD_SIZE
from ..utils.game import draw_game_board

from ..top_bar import draw_top_bar

back_to_home = False


def handle_key_pressed(key):
    global back_to_home

    try:
        if key == Key.backspace or key.char == 'q':
            back_to_home = True
    except AttributeError as e:
        pass


def generate_empty_game_board_array(size):
    return [[' ' for _ in range(size)] for _ in range(size)]


def play(stdscr: 'curses._CursesWindow'):
    global back_to_home

    listener = Listener(on_press=handle_key_pressed)
    listener.start()

    while True:
        stdscr.clear()

        if back_to_home:
            back_to_home = False
            break

        game_board = generate_empty_game_board_array(BOARD_SIZE)
        draw_game_board(stdscr, game_board)

        draw_top_bar(stdscr)

        stdscr.refresh()
        sleep(0.2)

    listener.stop()
