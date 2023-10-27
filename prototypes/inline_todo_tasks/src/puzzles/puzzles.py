"""Defines the collection of algorithms used in the package."""

import re
import logging
from pathlib import Path
from dataclasses import dataclass


@dataclass
class Puzzle:
    """Represents an individual puzzle."""

    id: int
    type: str
    description: str

    def __hash__(self) -> int:
        return hash(self.id)

    def __repr__(self) -> str:
        return f"Puzzle(id={self.id})"


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


class PuzzleFinder:
    """Discovers puzzles in the codebase.

    A puzzle is defined via the following syntax:

        [PUZZLE 1] This is a puzzle.

    Where `PUZZLE` is the puzzle type, `1` is the puzzle ID, and
    `This is a puzzle.` is the puzzle description.
    """

    # pylint: disable=consider-using-f-string
    pattern: str = r"\[({})\s*(\d*)\](.*)".format(
        "|".join(
            [
                "TODO",
                "FIXME",
                "BUG",
                "REFACTOR",
                "PUZZLE",
            ]
        )
    )

    def find(self, content: str) -> set[Puzzle]:
        """Searches over the provided string for puzzles."""
        puzzles = set()

        ## Parse the puzzles from the content.
        for m in re.finditer(self.pattern, content, re.MULTILINE):
            puzzle_type, puzzle_id, puzzle_content = m.groups()
            puzzles.add(
                Puzzle(
                    id=int(puzzle_id) if puzzle_id else None,
                    type=puzzle_type or None,
                    description=puzzle_content.strip() or None,
                )
            )

        ## Assign IDs to the puzzles if required
        i = 1
        for puzzle in puzzles:
            if puzzle.id is None:
                puzzle.id = i
                i += 1

        return puzzles
