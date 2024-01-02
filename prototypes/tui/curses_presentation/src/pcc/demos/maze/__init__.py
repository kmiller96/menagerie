"""Prototype showing how to build a maze-navigating game in curses."""

import curses
import sys
from pathlib import Path

from .maze import Maze
from .structs import Vectors

HERE = Path(__file__).parent


class GameLoop:
    """Defines the global game loop object.

    Helps us wrap up our game closer to a more typical game loop structure of
    init-update-draw.
    """

    def __init__(self) -> None:
        self.window: "curses.window" = None
        self.maze = Maze((HERE / "map.txt").read_text())

    def run(self, window: "curses.window") -> None:
        """Run the game loop."""

        @curses.wrapper
        def func(window: "curses.window") -> None:
            self.window = window

            self.init()
            self.draw()

            while True:
                self.handle_input()
                self.draw()

    def init(self) -> None:
        """Initialises the game with any required configuration (post curses init)."""
        curses.curs_set(0)

    def draw(self) -> None:
        """Renders the game map."""
        self.window.erase()
        self.maze.draw(self.window)
        self.window.refresh()

    def handle_input(self) -> None:
        """Handles the user-supplied input."""
        key = self.window.getkey()

        if key == "q":
            sys.exit(0)

        if key in Vectors.__members__:  # Look up key string, not enums themselves.
            self.maze.move(Vectors[key].value)
