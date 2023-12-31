"""Defines the main routines of the package."""

# pylint: disable=redefined-builtin

from pathlib import Path

from loguru import logger

from .puzzles import PuzzleFinder
from .formatter import Formatter


def extract(path: Path, format: str = "todo"):
    """Extracts all puzzles from the supplied path."""
    puzzles = PuzzleFinder().search(path)
    fmt = Formatter(puzzles)

    if format == "json":
        return fmt.to_json()
    elif format == "todo":
        return fmt.to_todo()
    else:
        raise ValueError(f"Unknown format: {format}")


def assign(path: Path):
    """Finds puzzles with IDs and assign them an ID."""
    ## Locate puzzles
    puzzles = PuzzleFinder().search(path)

    i = 1

    for puzzle in puzzles:
        if puzzle.id is not None:
            logger.debug(f"Puzzle [{puzzle.reference}] already has an ID. Continuing.")
            continue  # Skip if already has an id

        ## Assign ID
        while i in set(p.id for p in puzzles):
            i += 1  # Find the next valid ID

        puzzle.id = i
        logger.debug(f"Assigned ID {i} to puzzle [{puzzle.reference}]")

        ## Update the file
        logger.debug(f"Writing changes to file {puzzle.path}.")
        with open(puzzle.path, "r+", encoding="utf-8") as f:
            content = f.read()
            content = content.replace(puzzle.raw, puzzle.format())

            f.seek(0)
            f.write(content)


def check(path: Path):
    """Validates that all puzzles have IDs."""
    puzzles = PuzzleFinder().search(path)
    errors = []

    for puzzle in puzzles:
        if puzzle.id is None:
            err = f"[{puzzle.reference}] Puzzle has no ID."

            logger.error(err)
            errors.append(err)

    return errors


def run(path: Path, format: str = "todo"):
    """Searches over the provided path for puzzles, writing IDs if not present."""
    assign(path)
    extract(path=path, format=format)
