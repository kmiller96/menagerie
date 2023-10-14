"""Defines the screensaver prototype."""

import curses

from .physics import Environment, Coordinate

FPS = 24


def main(stdscr: "curses.window"):
    """Run the screensaver."""
    environment = Environment(start=Coordinate(5, 5))

    environment.init(stdscr)

    while True:
        environment.update()
        environment.draw()

        curses.napms(1000 // FPS)
