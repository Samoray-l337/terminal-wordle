import curses

from time import sleep

from pynput.keyboard import Key, Listener

from ..config import HELP_PAGE_MESSAGE

from ..top_bar import draw_top_bar

back_to_home = False

# TODO: export this function to another file and use it
def handle_key_pressed(key):
    global back_to_home

    try:
        if key == Key.backspace or key.char == 'q':
            back_to_home = True
    except AttributeError as e:
        pass


def draw_help_information(stdscr: 'curses._CursesWindow'):
    h, w = stdscr.getmaxyx()

    x = w // 2 - (len(HELP_PAGE_MESSAGE) // 2)
    y = h // 2

    stdscr.addstr(y, x, HELP_PAGE_MESSAGE)


def help(stdscr: 'curses._CursesWindow'):
    global back_to_home

    listener = Listener(on_press=handle_key_pressed)
    listener.start()

    while True:
        stdscr.clear()

        if back_to_home:
            back_to_home = False
            break

        draw_top_bar(stdscr)
        draw_help_information(stdscr)

        stdscr.refresh()

        sleep(0.2)

    listener.stop()