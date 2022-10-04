import curses
import time

from animations import animate_fire, animate_spaceship, generate_stars
from constants import TIC_TIMEOUT
from custom_types import Window


def draw(canvas: Window) -> None:

    while True:
        curses.curs_set(False)
        canvas.border()

        corutines = generate_stars(canvas)
        corutines.append(animate_fire(canvas))
        corutines.append(animate_spaceship(canvas))

        while len(corutines):

            for corutine in corutines.copy():
                try:
                    corutine.send(None)
                except StopIteration:
                    corutines.remove(corutine)

            canvas.refresh()
            time.sleep(TIC_TIMEOUT)
        canvas.clear()


if __name__ == "__main__":
    curses.update_lines_cols()
    curses.wrapper(draw)
