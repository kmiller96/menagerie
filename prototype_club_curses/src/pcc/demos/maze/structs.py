"""Defines a coordinate structure for the maze. Used for movement primarily."""

from enum import Enum, StrEnum, IntFlag

from dataclasses import dataclass


@dataclass
class Coordinate:
    """A coordinate in the maze."""

    y: int
    x: int

    def __add__(self, other: "Coordinate") -> "Coordinate":
        return Coordinate(self.y + other.y, self.x + other.x)

    def __sub__(self, other: "Coordinate") -> "Coordinate":
        return Coordinate(self.y - other.y, self.x - other.x)


class Sprite(StrEnum):
    """A sprite in the maze."""

    player = "@"
    wall = "█"
    floor = " "


class Tile(IntFlag):
    """A tile in the maze."""

    wall = 0
    floor = 1


class Vectors(Enum):
    """A mapping of keypresses to vectors."""

    KEY_UP = Coordinate(-1, 0)
    KEY_DOWN = Coordinate(1, 0)
    KEY_LEFT = Coordinate(0, -1)
    KEY_RIGHT = Coordinate(0, 1)
