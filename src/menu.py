import curses

from .pages import help, home, play
from .utils.screen import apply_color_pair, remove_color_pair
from .config import MENU_COLOR_PAIR_INDEX, MENU_OPTIONS, MENU_SELECTED_COLOR_PAIR_INDEX


menu_functions = {'Home': home.home, 'Play': play.play, 'Help': help.help}


def show_menu(stdscr: 'curses._CursesWindow', selected_row_index=0):
    h, w = stdscr.getmaxyx()

    apply_color_pair(stdscr, MENU_COLOR_PAIR_INDEX)

    for index, menu_item in enumerate(MENU_OPTIONS):
        x = w // 2 - len(menu_item) // 2
        y = h // 2 - len(MENU_OPTIONS) // 2 + index

        if index == selected_row_index:
            apply_color_pair(stdscr, MENU_SELECTED_COLOR_PAIR_INDEX)

        stdscr.addstr(y, x, menu_item)
        remove_color_pair(stdscr, MENU_SELECTED_COLOR_PAIR_INDEX)

    remove_color_pair(stdscr, MENU_COLOR_PAIR_INDEX)

    stdscr.refresh()
