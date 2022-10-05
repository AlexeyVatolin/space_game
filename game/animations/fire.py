from typing import Coroutine

import asyncio
import curses

from custom_types import Window


async def animate_fire(canvas: Window) -> None:
    rows, columns = canvas.getmaxyx()
    await fire(canvas, rows // 2, columns // 2)


async def fire(
    canvas: Window,
    start_row: int,
    start_column: int,
    rows_speed: float = -0.3,
    columns_speed: float = 0,
) -> None:
    """Display animation of gun shot, direction and speed can be specified."""

    row, column = float(start_row), float(start_column)

    canvas.addstr(round(row), round(column), "*")
    await asyncio.sleep(0)

    canvas.addstr(round(row), round(column), "O")
    await asyncio.sleep(0)
    canvas.addstr(round(row), round(column), " ")

    row += rows_speed
    column += columns_speed

    symbol = "-" if columns_speed else "|"

    rows, columns = canvas.getmaxyx()
    max_row, max_column = rows - 1, columns - 1

    curses.beep()

    while 0 < row < max_row and 0 < column < max_column:
        canvas.addstr(round(row), round(column), symbol)
        await asyncio.sleep(0)
        canvas.addstr(round(row), round(column), " ")
        row += rows_speed
        column += columns_speed
