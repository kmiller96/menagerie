import random
from copy import deepcopy
from typing import Iterable

from hearts.cards import Card, Suit


class Pile:
    """Represents a pile of playing cards.

    This is a generalisation of a deck, hand of cards, or a trick.
    """

    def __init__(self, cards: list[Card] = None):
        self.cards = cards or []

    def __repr__(self) -> str:
        return f"Pile(cards={self.cards})"

    def __len__(self) -> int:
        return len(self.cards)

    def __iter__(self) -> Card:
        return iter(self.cards)

    def __getitem__(self, index) -> Iterable[Card]:
        return self.cards[index]

    def add(self, card: Card):
        """Add a card to the hand."""
        self.cards.append(card)

    def remove(self, card: Card):
        """Remove a card from the hand."""
        self.cards.remove(card)

    def shuffle(self):
        """Shuffle the deck."""
        random.shuffle(self.cards)

    def sort(self):
        """Sort the deck."""
        self.cards.sort(key=lambda card: (card.suit, card.rank))

    def split(self, n: int):
        """Split the deck into n piles."""
        return [Pile(self.cards[i::n]) for i in range(n)]

    def save(self) -> "Pile":
        """Save the pile."""
        return deepcopy(self)

    def clear(self):
        """Clear the pile."""
        self.cards.clear()


class Trick(Pile):
    """Represents a trick within the game."""

    @property
    def leading_suit(self) -> Suit:
        """Returns the leading suit of the trick."""
        return self.cards[0].suit

    @property
    def winner(self) -> Card:
        """Returns the winner of the trick."""
        return max(
            (card for card in self if card.suit == self.leading_suit),
            key=lambda card: card.rank,
        )
