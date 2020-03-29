import os

from screen_utils.constants import *
import pyautogui
import time


def get_square_coords(c, i, side_color):
    if side_color == 'white':
        return luanglex + square_size * (ord(c) - ord('a')), luangley + square_size * (8 - i), \
                luanglex + square_size * (ord(c) - ord('a') + 1), luangley + square_size * (8 - i + 1)
    if side_color == 'black':
        return luanglex + square_size * (ord('h') - ord(c)), luangley + square_size * (i - 1), \
                luanglex + square_size * (ord('h') - ord(c) + 1), luangley + square_size * i


def get_square_middle(square_quadro):
    return (square_quadro[0] + square_quadro[2]) // 2, (square_quadro[1] + square_quadro[3]) // 2


def move(uci_move, side_color):
    from_square = get_square_coords(uci_move[0], int(uci_move[1]), side_color)
    to_square = get_square_coords(uci_move[2], int(uci_move[3]), side_color)
    pyautogui.click(get_square_middle(from_square))
    pyautogui.click(get_square_middle(to_square))
