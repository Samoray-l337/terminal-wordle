import curses


def home(stdscr: 'curses._CursesWindow'):
    stdscr.addstr(0, 0, 'Home')
    stdscr.refresh()
