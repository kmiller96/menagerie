"""Prototype for a spelling game."""


import curses
from pathlib import Path

from .typer import Typer


HERE = Path(__file__).parent


def main(stdscr: "curses.window"):
    """Runs the spelling game."""
    words = (HERE / "wordlist.txt").read_text().splitlines()

    typer = Typer([word for word in words if len(word) > 3])
    typer.init(stdscr)

    while True:
        typer.update()
        typer.draw()

        curses.doupdate()
