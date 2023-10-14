"""Defines the physics engine."""

import curses
from dataclasses import dataclass


def coordinate_to_curses(
    window: "curses.window", coordinate: "Coordinate"
) -> "Coordinate":
    """Converts a coordinate to curses' coordinate system."""
    height, _ = window.getmaxyx()
    return Coordinate(coordinate.x, height - coordinate.y).to_tuple()


@dataclass
class Coordinate:
    x: int
    y: int

    def to_tuple(self) -> tuple[int, int]:
        """Converts the coordinate to a tuple."""
        return (self.x, self.y)

    def __add__(self, other: "Coordinate") -> "Coordinate":
        return Coordinate(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Coordinate") -> "Coordinate":
        return Coordinate(self.x - other.x, self.y - other.y)

    def __neg__(self) -> "Coordinate":
        return Coordinate(-self.x, -self.y)


@dataclass
class Ball:
    """Data structure for the ball."""

    position: Coordinate
    velocity: Coordinate
    acceleration: Coordinate

    sprite: str = "O"

    def tick(self) -> None:
        """Ticks forward the ball, updating position and velocity."""
        self.position.x += self.velocity.x
        self.position.y += self.velocity.y

        self.velocity.x += self.acceleration.x
        self.velocity.y += self.acceleration.y


class Environment:
    """Data structure for the physics environment.

    We have our coordinate system with (0, 0) being in the bottom right corner.
    This is different to curses' coordinate system, which has (0, 0) in the top
    left corner. We have to account for this when drawing the ball.
    """

    def __init__(self, start: Coordinate) -> None:
        self.window: "curses.window"
        self.ball = Ball(
            position=start,
            velocity=Coordinate(2, 1),
            acceleration=Coordinate(0, -1),
        )

    def init(self, window: "curses.window") -> None:
        """Initializes the environment."""
        self.window = window
        curses.curs_set(0)

    def update(self):
        """Updates the ball's position."""
        self.ball.tick()

        _, width = self.window.getmaxyx()

        # Bounce the ball off the walls.
        if self.ball.position.x <= 0 or self.ball.position.x >= width:
            self.ball.velocity = -self.ball.velocity
            self.ball.position.x = max(0, min(width - 2, self.ball.position.x))

        # Bounce the ball off the floor.
        if self.ball.position.y <= 0:
            self.ball.velocity.y = int(-0.5 * self.ball.velocity.y)
            self.ball.position.y = 1

    def draw(self):
        """Draws the ball's position on the screen."""
        self.window.erase()

        x, y = coordinate_to_curses(self.window, self.ball.position)
        self.window.addstr(y, x, self.ball.sprite)

        self.window.refresh()
