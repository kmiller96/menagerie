"""Defines the main class to handle the maze logic."""

import curses

from .structs import Coordinate, Sprite, Tile


class Maze:
    """A maze that can be navigated by a player."""

    _maze: list[list[Tile]]

    def __init__(self, template: str):
        self.__init_maze__(template)
        self._player = Coordinate(0, 0)

    def __init_maze__(self, template: str):
        """Initialize the maze with the given string."""
        self._maze = []

        for row in template.splitlines():
            _r = []

            for char in row:
                if char == Sprite.floor:
                    _r.append(Tile.floor)
                elif char == Sprite.wall:
                    _r.append(Tile.wall)
                else:
                    raise ValueError(f"Unknown character: {char}")

            self._maze.append(_r)

        return self

    def _valid_move(self, vector: Coordinate):
        """Confirms that a movement is valid."""
        pos = self._player + vector

        ## Verify within bounds.
        if pos.y < 0 or pos.y >= len(self._maze):
            return False
        if pos.x < 0 or pos.x >= len(self._maze[0]):
            return False

        ## Verify not walking into a wall
        tile = self._maze[pos.y][pos.x]

        if tile == Tile.wall:
            return False

        ## Otherwise, it's a valid move.
        return True

    def move(self, direction: Coordinate):
        """Move the player in the given direction."""

        if self._valid_move(direction):
            self._player += direction

        return self

    def draw(self, window: "curses.window"):
        """Draws the maze onto the window."""
        window.erase()

        for y, row in enumerate(self._maze):
            for x, tile in enumerate(row):
                if self._player == Coordinate(y, x):
                    window.addstr(y, x, Sprite.player)

                else:
                    sprite = Sprite[tile.name]
                    window.addstr(y, x, sprite)

        window.refresh()
        return self
