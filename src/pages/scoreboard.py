import curses


def scoreboard(stdscr: 'curses._CursesWindow'):
    stdscr.addstr(0, 0, 'Scoreboard')
    stdscr.refresh()
