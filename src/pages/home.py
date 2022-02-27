import curses

from time import sleep

from pynput.keyboard import Key, Listener

from random import choice
from string import ascii_letters

from ..top_bar import draw_top_bar

from ..config import BOARD_SIZE

from ..utils.game import draw_game_board

back_to_home = False


def handle_key_pressed(key):
    global back_to_home

    if key == Key.backspace:
        back_to_home = True


def generate_random_2d_array_of_letters(size):
    return [[choice(ascii_letters) for _ in range(size)] for _ in range(size)]


def home(stdscr: 'curses._CursesWindow'):
    global back_to_home

    listener = Listener(on_press=handle_key_pressed)
    listener.start()

    while True:
        stdscr.clear()

        if back_to_home:
            back_to_home = False
            break

        array = generate_random_2d_array_of_letters(BOARD_SIZE)
        draw_game_board(stdscr, array)

        draw_top_bar(stdscr)

        stdscr.refresh()
        sleep(0.5)

    listener.stop()
