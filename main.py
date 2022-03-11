#!/usr/bin/env python3

import curses

from src.menu import show_menu, menu_functions
from src.top_bar import draw_top_bar

from src.utils.screen import close_screen_settings, start_screen_settings
from src.utils.mouse import get_pressed_mouse_element

from src.config import *

def draw_main_page(stdscr: 'curses._CursesWindow', current_selected_row):
    draw_top_bar(stdscr)
    show_menu(stdscr, current_selected_row)

def call_selected_menu_option(stdscr: 'curses._CursesWindow', selected_menu_option: str):
    return menu_functions[selected_menu_option](stdscr)


def main(stdscr: 'curses._CursesWindow'):
    start_screen_settings(stdscr)

    current_selected_row = 0

    while True:
        stdscr.clear()
        draw_main_page(stdscr, current_selected_row)

        pressed_key = stdscr.getch()

        if pressed_key == curses.KEY_MOUSE:
            pressed_element = get_pressed_mouse_element(stdscr)

            if pressed_element not in MENU_OPTIONS:
                continue
            elif pressed_element == 'Exit':
                break

            call_selected_menu_option(stdscr, pressed_element)

        elif pressed_key == curses.KEY_UP:
            current_selected_row = (current_selected_row - 1 + len(MENU_OPTIONS)) % len(MENU_OPTIONS)
        elif pressed_key == curses.KEY_DOWN:
            current_selected_row = (current_selected_row + 1) % len(MENU_OPTIONS)
        elif pressed_key in ENTER_KEY_OPTIONS:
            selected_menu_option = MENU_OPTIONS[current_selected_row]

            if selected_menu_option == 'Exit':
                break

            call_selected_menu_option(stdscr, selected_menu_option)

    close_screen_settings()


if __name__ == "__main__":
    try:
        curses.wrapper(main)
    except KeyboardInterrupt as e:
        close_screen_settings()
