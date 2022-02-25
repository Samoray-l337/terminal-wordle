import curses

from .utils.screen import apply_color_pair, remove_color_pair

from .config import MENU_COLOR_PAIR_INDEX, MENU_OPTIONS, MENU_SELECTED_COLOR_PAIR_INDEX


def show_menu(stdscr: 'curses._CursesWindow', screen_size, selected_row_index=0):
    h, w = screen_size

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
