"""Defines the collection of algorithms used in the package."""

import re
from typing import Iterable, Callable

from .structs import Puzzle


def groupby(iterable: Iterable, key: Callable):
    """Groups the provided iterable by the provided key."""
    groups: dict[str, list] = {}

    for item in iterable:
        val = key(item)

        if val not in groups:
            groups[val] = []

        groups[val].append(item)

    return groups.items()


class PuzzleFinder:
    """Discovers puzzles in the codebase."""

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
