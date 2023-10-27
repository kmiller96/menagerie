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
