#!/usr/bin/env python3

import curses

from src.menu import show_menu, menu_functions
from src.top_bar import show_top_bar

from src.utils.screen import close_screen_settings, start_screen_settings

from src.config import *


def call_selected_menu_option(stdscr: 'curses._CursesWindow', selected_row_index: int):
    return menu_functions[selected_row_index](stdscr)


def main(stdscr: 'curses._CursesWindow'):
    screen_size = start_screen_settings(stdscr)

    show_top_bar(stdscr, screen_size)
    show_menu(stdscr, screen_size)

    current_selected_row = 0

    while True:
        pressed_key = stdscr.getch()
        stdscr.clear()

        if pressed_key == curses.KEY_UP:
            current_selected_row = (current_selected_row - 1 + len(MENU_OPTIONS)) % len(MENU_OPTIONS)
        elif pressed_key == curses.KEY_DOWN:
            current_selected_row = (current_selected_row + 1) % len(MENU_OPTIONS)
        elif pressed_key in ENTER_KEY_OPTIONS:
            selected_menu_option = MENU_OPTIONS[current_selected_row]

            if selected_menu_option == 'Exit':
                break

            call_selected_menu_option(stdscr, current_selected_row)
            continue

        show_top_bar(stdscr, screen_size)
        show_menu(stdscr, screen_size, current_selected_row)

    close_screen_settings()


if __name__ == "__main__":
    try:
        curses.wrapper(main)
    except KeyboardInterrupt as e:
        pass
