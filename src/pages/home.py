import curses

from time import sleep

from pynput.keyboard import Key, Listener

from random import choice
from string import ascii_letters

from ..top_bar import draw_top_bar

from ..config import BOARD_SIZE

from ..utils.game import draw_game_board, generate_game_element

back_to_home = False

# TODO: think how to export this function to another file
def handle_key_pressed(key):
    global back_to_home

    try:
        if key == Key.backspace or key.char == 'q':
            back_to_home = True
    except AttributeError as e:
        pass


def get_random_boolean():
    return choice([False, True])


def generate_random_letters_gameboard(size):
    return [[generate_game_element(choice(ascii_letters), get_random_boolean(), get_random_boolean()) for _ in range(size)] for _ in range(size)]


def home(stdscr: 'curses._CursesWindow'):
    global back_to_home

    listener = Listener(on_press=handle_key_pressed)
    listener.start()

    while True:
        stdscr.clear()

        if back_to_home:
            back_to_home = False
            break

        array = generate_random_letters_gameboard(BOARD_SIZE)
        draw_game_board(stdscr, array)

        draw_top_bar(stdscr)

        stdscr.refresh()
        sleep(0.5)

    listener.stop()
