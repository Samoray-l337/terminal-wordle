import curses

from ..config import CORRECT_LETTER_COLOR_PAIR_INDEX, EXISTS_LETTER_COLOR_PAIR_INDEX, MENU_SELECTED_COLOR_PAIR_INDEX, TILE_SIZE

from .screen import apply_color_pair, remove_color_pair


def generate_game_element(letter, is_correct=False, is_exists=False):
    return {'value': letter, 'is_correct': is_correct, 'is_exists': is_exists}


def draw_square(stdscr: 'curses._CursesWindow', i, j, element, board_size):
    height, width = stdscr.getmaxyx()

    value, is_correct, is_exists = element['value'], element['is_correct'], element['is_exists']

    if is_correct:
        apply_color_pair(stdscr, CORRECT_LETTER_COLOR_PAIR_INDEX)
    elif is_exists:
        apply_color_pair(stdscr, EXISTS_LETTER_COLOR_PAIR_INDEX)
    else:
        apply_color_pair(stdscr, MENU_SELECTED_COLOR_PAIR_INDEX)

    x = int((width / 2) - TILE_SIZE * (board_size - 0.5 - 2 * i))
    y = int((height / 2) - (board_size - 0.5 - 2 * j))

    if y < 0 or x < 0 or x > width or y > height:
        raise Exception('board can\'t fit inside terminal size')

    stdscr.addstr(y, x, f' {value} ')
    
    remove_color_pair(stdscr, MENU_SELECTED_COLOR_PAIR_INDEX)
    remove_color_pair(stdscr, CORRECT_LETTER_COLOR_PAIR_INDEX)
    remove_color_pair(stdscr, EXISTS_LETTER_COLOR_PAIR_INDEX)


def draw_game_board(stdscr: 'curses._CursesWindow', game_board):
    for row_index, row in enumerate(game_board):
        for col_index, element in enumerate(row):
            draw_square(stdscr, col_index, row_index, element, len(game_board))
