"""Defines the collection of algorithms used in the package."""

import re
import logging
from pathlib import Path
from dataclasses import dataclass
from typing import Iterable, Optional


@dataclass
class Puzzle:
    """Represents an individual puzzle."""

    id: Optional[int] = None
    type: str = None
    description: str = None

    path: Path = None
    line: int = None

    raw: str = None

    def __hash__(self) -> int:
        return hash(self.id)

    def __repr__(self) -> str:
        return f"Puzzle(id={self.id})"

    def __str__(self) -> str:
        return self.format()

    def format(self) -> str:
        """Formats the puzzle string."""
        return f"[{self.type} {self.id}] {self.description}"


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

    def search(self, path: Path) -> set[Puzzle]:
        """Searches over the provided path for puzzles."""
        puzzles = set()

        for f in path.rglob("*"):
            if not f.is_file():
                logging.debug("%s is a folder; skipping.", f)
                continue

            logging.debug("Searching %s", f)
            content = f.read_text()

            for puzzle in self.find(content):
                puzzle.path = f

                logging.info("Found puzzle %s", puzzle)
                puzzles.add(puzzle)

        return puzzles

    def find(self, content: str) -> Iterable[Puzzle]:
        """Searches over the provided string for puzzles."""
        for m in re.finditer(self.pattern, content, re.MULTILINE):
            puzzle_type, puzzle_id, puzzle_content = m.groups()
            puzzle_line = self._pos2line(content=content, pos=m.start())

            yield Puzzle(
                id=int(puzzle_id) if puzzle_id else None,
                type=puzzle_type or None,
                description=puzzle_content.strip() or None,
                line=puzzle_line,
                raw=m.group(0),
            )

        ## Assign IDs to the puzzles if required
        # i = 1
        # for puzzle in puzzles:
        #     if puzzle.id is None:
        #         puzzle.id = i
        #         i += 1

        # return puzzles

    @staticmethod
    def _pos2line(content: str, pos: int) -> int:
        """Converts a position in a string to a line number."""
        return content.count("\n", 0, pos) + 1
