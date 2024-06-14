"""Data structure representing a player in the game of hearts."""

from hearts.cards import Card
from hearts.pile import Pile


class Player:
    """Represents a player in the game of hearts."""

    def __init__(self, name: str, hand: Pile = None):
        self.name = name
        self.hand = hand or Pile([])
        self.tricks: list[Pile] = []

    def play(self) -> Card:
        """Decides which card to play.

        NOTE: For now, this just plays the first card in the player's hand.
        """
        return self.hand.cards.pop()
