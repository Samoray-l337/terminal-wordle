import curses

from time import sleep

from pynput.keyboard import Key, Listener

from ..top_bar import draw_top_bar

back_to_home = False

# TODO: export this function to another file and use it
def handle_key_pressed(key):
    global back_to_home

    if key == Key.backspace:
        back_to_home = True


def help(stdscr: 'curses._CursesWindow'):
    global back_to_home

    listener = Listener(on_press=handle_key_pressed)
    listener.start()

    while True:
        stdscr.clear()

        if back_to_home:
            back_to_home = False
            break

        stdscr.addstr(0, 0, 'Help')
        stdscr.refresh()

        draw_top_bar(stdscr)

        stdscr.refresh()
        sleep(0.2)

    listener.stop()