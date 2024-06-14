"""Defines special logic functions."""

from hearts.cards import Card, Rank, Suit
from hearts.players import Player
from hearts.pile import Pile


def winning_card(cards: Pile) -> Card:
    """Determines the winning card of the trick."""
    return max(
        (
            card
            for card in cards
            if card.suit == cards[0].suit  # First card determines the leading suit.
        ),
        key=lambda card: card.rank,
    )


def create_deck() -> Pile:
    """Create a new deck of cards."""

    deck = Pile([Card(rank, suit) for rank in Rank for suit in Suit])
    deck.shuffle()

    return deck


def determine_starting_player(players: list[Player]) -> Player:
    """Determines the starting player for the game."""

    for player in players:
        if any(
            card.rank == Rank.TWO and card.suit == Suit.CLUBS for card in player.hand
        ):
            return player

    raise ValueError("No player has the 2 of Clubs.")
