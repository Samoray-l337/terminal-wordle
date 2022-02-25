#!/usr/bin/env python3

import curses
from time import sleep

from config import *


def start_screen_settings(stdscr: 'curses._CursesWindow'):
    curses.curs_set(0)

    return stdscr.getmaxyx()


def close_screen_settings():
    curses.curs_set(1)


def create_top_bar(stdscr: 'curses._CursesWindow', screen_size, text):
    _, w = screen_size

    x = w // 2 - len(text) // 2
    y = 0

    stdscr.addstr(y, x, text)
    stdscr.refresh()


def main(stdscr: 'curses._CursesWindow'):
    height, width = start_screen_settings(stdscr)

    create_top_bar(stdscr, (height, width), TOP_BAR_TEXT)

    sleep(100)

    close_screen_settings()


if __name__ == "__main__":
    try:
        curses.wrapper(main)
    except KeyboardInterrupt as e:
        pass
