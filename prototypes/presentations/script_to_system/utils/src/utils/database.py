"""Contains the database utility class."""

from pathlib import Path


class Database:
    """Simulates a simple database. We do this with a plain text CSV file."""

    def __init__(self, here: str):
        """Initializes the database.

        Args:
            here (str): The `__file__` of the script.
        """
        self.path = Path(here).parent / "database.db"
        self.path.unlink(missing_ok=True)

    def insert(self, data: list[int]):
        """Appends data to the database."""
        with open(self.path, "a") as file:
            file.write(",".join(data) + "\n")
