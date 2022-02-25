import curses

from .utils.screen import apply_color_pair, remove_color_pair

from .config import TOP_BAR_COLOR_PAIR_INDEX, TOP_BAR_TEXT

def create_top_bar(stdscr: 'curses._CursesWindow', screen_size):
    _, w = screen_size

    x = w // 2 - len(TOP_BAR_TEXT) // 2
    y = 0

    apply_color_pair(stdscr, TOP_BAR_COLOR_PAIR_INDEX)
    stdscr.addstr(y, x, TOP_BAR_TEXT)
    remove_color_pair(stdscr, TOP_BAR_COLOR_PAIR_INDEX)

    stdscr.refresh()
