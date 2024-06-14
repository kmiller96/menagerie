"""Defines the game rules for Hearts."""

from hearts.cards import Card, Suit, Rank
from hearts.pile import Pile


class Umpire:
    """Represents a game umpire. It validates if a card can be played."""

    def __init__(self):
        self.trick: Pile = Pile()
        self.played: Pile = Pile()

    @property
    def hearts_broken(self) -> bool:
        """Determines if hearts have been broken."""
        return any(card.suit == Suit.HEARTS for card in self.played)

    def check(self, card: Card, hand: Pile) -> bool:
        """Determines if a card can be played."""

        if len(self.trick) == 0:
            if len(self.played) == 0 and card != Card(Rank.TWO, Suit.CLUBS):
                return False  # First trick must lead with 2 of clubs

            if card.suit == Suit.HEARTS and not self.hearts_broken:
                return False  # Hearts cannot be played until broken

        if len(self.trick) > 0:
            lead_suit = self.trick[0].suit

            if card.suit != lead_suit and any(c.suit == lead_suit for c in hand):
                return False  # Must follow suit if possible

        return True

    def register(self, card: Card):
        """Registers that a card was played."""
        self.trick.append(card)
        self.played.append(card)
