"""Defines the main routines of the package."""

# pylint: disable=redefined-builtin

from pathlib import Path

from .puzzles import search
from .formatter import Formatter


def extract(path: Path, format: str = "todo"):
    """Extracts all puzzles from the supplied path."""
    puzzles = search(path)
    fmt = Formatter(puzzles)

    if format == "json":
        return fmt.to_json()
    elif format == "todo":
        return fmt.to_todo()
    else:
        raise ValueError(f"Unknown format: {format}")


def assign(path: Path):
    """Finds puzzles with IDs and assign them an ID."""
    puzzles = search(path)

    ...


def run(path: Path):
    """Searches over the provided path for puzzles, writing IDs if not present."""
