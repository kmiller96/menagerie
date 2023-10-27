"""Formats the output."""

import json
from dataclasses import dataclass
from typing import Iterable

from .structs import Puzzle
from .algorithms import groupby


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
