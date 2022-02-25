#!/usr/bin/env python3

import curses
from time import sleep

from src.top_bar import create_top_bar
from src.utils.screen import close_screen_settings, start_screen_settings

from src.config import *


def main(stdscr: 'curses._CursesWindow'):
    screen_size = start_screen_settings(stdscr)

    create_top_bar(stdscr, screen_size)

    sleep(100)

    close_screen_settings()


if __name__ == "__main__":
    try:
        curses.wrapper(main)
    except KeyboardInterrupt as e:
        pass
