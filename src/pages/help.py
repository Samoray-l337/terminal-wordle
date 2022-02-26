import curses


def help(stdscr: 'curses._CursesWindow'):
    stdscr.addstr(0, 0, 'Help')
    stdscr.refresh()
