import curses

from time import sleep

from pynput.keyboard import Key, Listener

from random import choice
from string import ascii_letters

from ..config import BOARD_SIZE

from ..utils.game import draw_game_board

# TODO: allow more keys to leave the level
is_escape_pressed = False


def handle_key_pressed(key):
    global is_escape_pressed

    if key == Key.backspace:
        is_escape_pressed = True


def generate_random_2d_array_of_letters(size):
    return [[choice(ascii_letters) for _ in range(size)] for _ in range(size)]


def home(stdscr: 'curses._CursesWindow'):
    global is_escape_pressed

    listener = Listener(on_press=handle_key_pressed)
    listener.start()

    stdscr.clear()

    while True:
        stdscr.clear()

        if is_escape_pressed:
            is_escape_pressed = False
            break

        array = generate_random_2d_array_of_letters(BOARD_SIZE)
        draw_game_board(stdscr, array)

        stdscr.refresh()
        sleep(0.5)
