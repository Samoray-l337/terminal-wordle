#!/usr/bin/env python3

import curses
from time import sleep

from src.utils.screen import apply_color_pair, close_screen_settings, remove_color_pair, start_screen_settings

from src.config import *


def create_top_bar(stdscr: 'curses._CursesWindow', screen_size, text):
    _, w = screen_size

    x = w // 2 - len(text) // 2
    y = 0

    apply_color_pair(stdscr, TOP_BAR_COLOR_PAIR_INDEX)
    stdscr.addstr(y, x, text)
    remove_color_pair(stdscr, TOP_BAR_COLOR_PAIR_INDEX)

    stdscr.refresh()


def main(stdscr: 'curses._CursesWindow'):
    screen_size = start_screen_settings(stdscr)

    create_top_bar(stdscr, screen_size, TOP_BAR_TEXT)

    sleep(100)

    close_screen_settings()


if __name__ == "__main__":
    try:
        curses.wrapper(main)
    except KeyboardInterrupt as e:
        pass
