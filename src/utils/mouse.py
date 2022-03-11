import curses


# TODO: this function will capture clicks on all the line, not specefic on the wanted element
def get_pressed_mouse_element(stdscr: 'curses._CursesWindow'):
    _, _, my, _, _ = curses.getmouse()
    _, w = stdscr.getmaxyx()

    pressed_line = stdscr.instr(my, 0, w)

    return pressed_line.decode('utf-8').strip()
