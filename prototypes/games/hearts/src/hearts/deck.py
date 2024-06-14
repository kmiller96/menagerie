"""Defines individual decks.

Note that a player's hand is just a special case for a deck of cards, so we can
reuse the same class for both.
"""

import random

from hearts.cards import Card, Rank, Suit


class Hand:
    """Represents a hand of playing cards."""

    def __init__(self, cards: list[Card]):
        self.cards = cards

    def __iter__(self):
        return iter(self.cards)

    def shuffle(self):
        """Shuffle the deck."""
        random.shuffle(self.cards)

    def sort(self):
        """Sort the deck."""
        self.cards.sort(key=lambda card: (card.suit, card.rank))


class Deck(Hand):
    def __init__(self):
        self.cards = [Card(rank, suit) for rank in Rank for suit in Suit]
