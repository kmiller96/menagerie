"""Formats the output."""

import json
from dataclasses import dataclass
from typing import Iterable, Callable

from .puzzles import Puzzle


def groupby(
    iterable: Iterable[Puzzle],
    key: Callable[[Puzzle], str],
) -> Iterable[tuple[str, list[Puzzle]]]:
    """Groups the provided iterable by the provided key."""
    groups: dict[str, list] = {}

    for item in iterable:
        val = key(item)

        if val not in groups:
            groups[val] = []

        groups[val].append(item)

    return groups.items()


@dataclass
class Formatter:
    puzzles: Iterable[Puzzle]

    def to_todo(self):
        """Formats the output as a todo list."""

        output = ""

        for t, puzzle in groupby(self.puzzles, lambda p: p.type):
            output += f"{t}:\n"

            for p in puzzle:
                output += f"    [ ] {p.description}\n"

            output += "\n"

        return output

    def to_dict(self):
        """Formats the output as a dictionary data structure."""
        return [
            {
                "id": p.id,
                "type": p.type,
                "description": p.description,
            }
            for p in self.puzzles
        ]

    def to_json(self):
        """Formats the output as a JSON file."""
        return json.dumps(self.to_dict(), indent=2)
