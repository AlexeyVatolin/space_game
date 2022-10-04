from typing import Any, Coroutine

import asyncio
import curses
import random

from constants import STARS, STARS_RATIO, TIC_TIMEOUT
from custom_types import Window


def generate_stars(canvas: Window) -> list[Coroutine[Any, Any, None]]:
    max_height, max_width = canvas.getmaxyx()
    start_count = int(max_height * max_width / STARS_RATIO)
    starts_corutines = [
        blink(
            canvas,
            random.randint(1, max_height - 2),
            random.randint(1, max_width - 2),
            random.choice(STARS),
        )
        for _ in range(start_count)
    ]
    return starts_corutines


async def blink(canvas: Window, row: int, column: int, symbol: str = "*") -> None:
    while True:
        canvas.addstr(row, column, symbol, curses.A_DIM)
        for _ in range(int(random.uniform(1.8, 2.2) / TIC_TIMEOUT)):
            await asyncio.sleep(0)

        canvas.addstr(row, column, symbol)
        for _ in range(int(random.uniform(0.1, 0.5) / TIC_TIMEOUT)):
            await asyncio.sleep(0)

        canvas.addstr(row, column, symbol, curses.A_BOLD)
        for _ in range(int(random.uniform(0.3, 0.7) / TIC_TIMEOUT)):
            await asyncio.sleep(0)

        canvas.addstr(row, column, symbol)
        for _ in range(int(random.uniform(0.1, 0.5) / TIC_TIMEOUT)):
            await asyncio.sleep(0)
