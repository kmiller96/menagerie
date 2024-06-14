"""Defines the individual playing cards."""

from enum import Enum


class Suit(str, Enum):
    """The suits of a standard deck of playing cards."""

    CLUBS = "♣"
    DIAMONDS = "♦"
    HEARTS = "♥"
    SPADES = "♠"


class Rank(int, Enum):
    """The ranks of a standard deck of playing cards."""

    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14

    def to_string(self):
        """Converts the rank to a string representation."""

        mapping = {
            11: "J",
            12: "Q",
            13: "K",
            14: "A",
        }

        return mapping.get(self.value) or str(self.value)


class Card:
    """A single playing card."""

    def __init__(self, rank: Rank, suit: Suit):
        assert isinstance(rank, Rank)
        assert isinstance(suit, Suit)

        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return f"{self.rank.to_string()}{self.suit.value}"

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

    @property
    def points(self):
        """The number of points this card is worth."""
        if self.suit == Suit.HEARTS:
            return 1
        elif self.suit == Suit.SPADES and self.rank == Rank.QUEEN:
            return 13
        else:
            return 0
