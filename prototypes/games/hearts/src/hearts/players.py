"""Data structure representing a player in the game of hearts."""

from __future__ import annotations  # Treats type hints as strings

import random
from typing import TYPE_CHECKING

from hearts.cards import Card
from hearts.pile import Pile

if TYPE_CHECKING:
    from hearts.state import GameState


class Player:
    """Represents a player in the game of hearts."""

    def __init__(self, name: str):
        self.name = name
        self.hand = Pile([])
        self.tricks: list[Pile] = []

    def __repr__(self) -> str:
        return f"Player(name={self.name})"

    def play(self, state: GameState) -> Card:
        """Decides which card to play.

        NOTE: For now, this just plays the first valid card in the player's hand.
        """

        while True:
            try:
                choice = state.validate(
                    player=self,
                    card=random.choice(self.hand.cards),
                )
            except AssertionError:
                continue  # Try again until valid.
            else:
                return choice
