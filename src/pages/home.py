import curses

from time import sleep

from pynput.keyboard import Key, Listener

from random import choice
from string import ascii_letters

from ..config import MENU_SELECTED_COLOR_PAIR_INDEX, TILE_SIZE, BOARD_SIZE

from ..utils.screen import apply_color_pair, remove_color_pair


is_escape_pressed = False


def handle_key_pressed(key):
    global is_escape_pressed

    if key == Key.backspace:
        is_escape_pressed = True


def generate_random_2d_array_of_letters(size):
    return [[choice(ascii_letters) for _ in range(size)] for _ in range(size)]


def draw_square(stdscr: 'curses._CursesWindow', i, j, value, board_size):
    height, width = stdscr.getmaxyx()

    apply_color_pair(stdscr, MENU_SELECTED_COLOR_PAIR_INDEX)

    x = (width // 2) - (board_size * (TILE_SIZE - i))
    y = (height // 2) - (board_size // 2 + (j * 2)) + board_size + 1

    if y < 0 or x < 0 or x > width or y > height:
        raise Exception('board can\'t fit inside terminal size')

    stdscr.addstr(y, x, f' {value} ')
    remove_color_pair(stdscr, MENU_SELECTED_COLOR_PAIR_INDEX)


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
        for row_index, row in enumerate(array):
            for col_index, value in enumerate(row):
                draw_square(stdscr, col_index, row_index, value, len(array))

        stdscr.refresh()
        sleep(0.2)
