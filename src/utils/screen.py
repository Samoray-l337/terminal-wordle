import curses

from ..config import *

def start_screen_settings(stdscr: 'curses._CursesWindow'):
    curses.curs_set(0)

    curses.init_pair(TOP_BAR_COLOR_PAIR_INDEX,
                     curses.COLOR_CYAN, curses.COLOR_WHITE)

    return stdscr.getmaxyx()


def close_screen_settings():
    curses.curs_set(1)

def apply_color_pair(stdscr: 'curses._CursesWindow', index: 'int'):
    stdscr.attron(curses.color_pair(index))

def remove_color_pair(stdscr: 'curses._CursesWindow', index: 'int'):
    stdscr.attroff(curses.color_pair(index))