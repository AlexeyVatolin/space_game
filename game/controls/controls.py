from typing import Literal

from constants import DOWN_KEY_CODE, LEFT_KEY_CODE, RIGHT_KEY_CODE, SPACE_KEY_CODE, UP_KEY_CODE
from custom_types import Window


def read_controls(canvas: Window) -> tuple[Literal[0, 1, -1], Literal[0, 1, -1], bool]:
    """Read keys pressed and returns tuple witl controls state."""

    rows_direction: Literal[0, 1, -1] = 0
    columns_direction: Literal[0, 1, -1] = 0
    space_pressed = False

    while True:
        pressed_key_code = canvas.getch()

        if pressed_key_code == -1:
            # https://docs.python.org/3/library/curses.html#curses.window.getch
            break

        if pressed_key_code == UP_KEY_CODE:
            rows_direction = -1

        if pressed_key_code == DOWN_KEY_CODE:
            rows_direction = 1

        if pressed_key_code == RIGHT_KEY_CODE:
            columns_direction = 1

        if pressed_key_code == LEFT_KEY_CODE:
            columns_direction = -1

        if pressed_key_code == SPACE_KEY_CODE:
            space_pressed = True

    return rows_direction, columns_direction, space_pressed
