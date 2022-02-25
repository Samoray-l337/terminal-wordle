import curses


def play(stdscr: 'curses._CursesWindow'):
    stdscr.addstr(0, 0, 'Play')
    stdscr.refresh()
