"""Defines the main routines of the package."""

import logging
from pathlib import Path

from .structs import Puzzle
from .algorithms import PuzzleFinder


def search(path: Path) -> set[Puzzle]:
    """Searches over the provided path for puzzles."""
    puzzles = set()
    finder = PuzzleFinder()

    for f in path.rglob("*"):
        if not f.is_file():
            logging.debug("%s is a folder; skipping.", f)
            continue
        else:
            logging.debug("Searching %s", f)

        content = f.read_text()

        for puzzle in finder.find(content):
            logging.info("Found puzzle %s", puzzle)
            puzzles.add(puzzle)

    return puzzles
