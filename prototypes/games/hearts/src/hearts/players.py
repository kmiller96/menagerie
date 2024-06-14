"""Data structure representing a player in the game of hearts."""

import random
from typing import Callable

from hearts.cards import Card
from hearts.pile import Pile


class Player:
    """Represents a player in the game of hearts."""

    def __init__(self, name: str, hand: Pile = None):
        self.name = name
        self.hand = hand or Pile([])
        self.tricks: list[Pile] = []

    def __repr__(self) -> str:
        return f"Player(name={self.name})"

    def play(self, validator: Callable[[Card, Pile], bool]) -> Card:
        """Decides which card to play.

        NOTE: For now, this just plays the first valid card in the player's hand.
        """

        while True:
            choice = random.choice(self.hand.cards)
            print(choice, self.hand, validator(choice, self.hand))

            if validator(choice, self.hand):
                self.hand.cards.remove(choice)
                return choice
