import curses

from ..config import *


def init_color_pairs():
    curses.init_pair(TOP_BAR_COLOR_PAIR_INDEX,
                     curses.COLOR_CYAN, curses.COLOR_BLACK)

    curses.init_pair(MENU_COLOR_PAIR_INDEX,
                     curses.COLOR_WHITE, curses.COLOR_BLACK)

    curses.init_pair(MENU_SELECTED_COLOR_PAIR_INDEX,
                     curses.COLOR_BLACK, curses.COLOR_WHITE)
                     
    curses.init_pair(NORMAL_LETTER_COLOR_PAIR_INDEX,
                     curses.COLOR_BLACK, curses.COLOR_WHITE)
                     
    curses.init_pair(CORRECT_LETTER_COLOR_PAIR_INDEX,
                     curses.COLOR_BLACK, curses.COLOR_GREEN)

    curses.init_pair(INCORRECT_LETTER_COLOR_PAIR_INDEX,
                     curses.COLOR_BLACK, curses.COLOR_RED)

    curses.init_pair(EXISTS_LETTER_COLOR_PAIR_INDEX,
                     curses.COLOR_BLACK, curses.COLOR_YELLOW)


def start_screen_settings(stdscr: 'curses._CursesWindow'):
    curses.curs_set(0)

    init_color_pairs()


def close_screen_settings():
    curses.curs_set(1)


def apply_color_pair(stdscr: 'curses._CursesWindow', index: 'int'):
    stdscr.attron(curses.color_pair(index))


def remove_color_pair(stdscr: 'curses._CursesWindow', index: 'int'):
    stdscr.attroff(curses.color_pair(index))
