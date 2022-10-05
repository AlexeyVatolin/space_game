import asyncio
import itertools
from pathlib import Path

from animations.frame import draw_frame, get_frame_size
from constants import BASE_DIR
from controls.controls import read_controls
from custom_types import Window


def _get_start_postion(canvas: Window, frame: str) -> tuple[int, int]:
    max_height, max_width = canvas.getmaxyx()
    frame_height, frame_width = get_frame_size(frame)
    return (max_height - frame_height + 1) // 2, (max_width - frame_width + 1) // 2


def _get_max_postion(canvas: Window, frame: str) -> tuple[int, int]:
    max_height, max_width = canvas.getmaxyx()
    frame_height, frame_width = get_frame_size(frame)
    return max_height - frame_height - 1, max_width - frame_width - 1


def _get_spaceship_postion(canvas: Window, frame: str, row: int, column: int) -> tuple[int, int]:
    rows_direction, columns_direction, space_pressed = read_controls(canvas)
    row += rows_direction
    column += columns_direction

    max_height, max_width = _get_max_postion(canvas, frame)
    row = min(max_height, max(1, row))
    column = min(max_width, max(1, column))
    return row, column


async def animate_spaceship(canvas: Window) -> None:
    canvas.nodelay(True)

    frames = [f.read_text() for f in sorted((BASE_DIR / "frames").glob("rocket_frame_*.txt"))]
    if not len(frames):
        raise ValueError("No frames for spaceship animation")

    start_row, start_column = _get_start_postion(canvas, frames[0])

    for prev_frame, frame in itertools.cycle(zip(frames, frames[1:] + [frames[0]])):
        draw_frame(canvas, start_row, start_column, prev_frame, negative=True)

        start_row, start_column = _get_spaceship_postion(canvas, frame, start_row, start_column)

        draw_frame(canvas, start_row, start_column, frame)
        await asyncio.sleep(0)
