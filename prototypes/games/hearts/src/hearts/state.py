from hearts.cards import Card, Suit, Rank
from hearts.pile import Pile, Trick
from hearts.players import Player


class GameState:
    """Represents the state of a game of Hearts."""

    def __init__(self, players: list[Player]):
        self.players = players
        self.trick = Trick()
        self.leader: Player = None

    @property
    def hands(self) -> dict[Player, Pile]:
        """Returns the current hands of all players."""
        return {player: player.hand for player in self.players}

    @property
    def played(self) -> Pile:
        """Returns all the cards that have been played in the game."""
        return Pile(
            [
                card
                for player in self.players
                for trick in player.tricks
                for card in trick
            ]
            + [card for card in self.trick]
        )

    @property
    def is_first_card(self) -> bool:
        """Determines if the current card is the first card of the game."""
        return len(self.played) == 0

    @property
    def hearts_broken(self) -> bool:
        """Determines if hearts have been broken."""
        return any(card.suit == Suit.HEARTS for card in self.played)

    @property
    def play_order(self) -> list[Player]:
        """Returns the order in which players should play."""
        start = self.players.index(self.leader)
        return [
            self.players[(start + i) % len(self.players)]
            for i in range(len(self.players))
        ]

    def resolve(self):
        """Resolves the trick and sets the next player."""

        # -- Determine winner -- #
        player = self.play_order[self.trick.cards.index(self.trick.winner)]

        # -- Update state -- #
        player.tricks.append(self.trick.save())
        self.trick.clear()
        self.leader = player

        return player

    ###########
    ## Rules ##
    ###########

    def validate(self, player: Player, card: Card) -> Card:
        """Validates that the card supplied is valid.

        This function will return the card if it's valid, otherwise it will raise
        an AssertionError.
        """

        self._player_must_have_card(player, card)
        self._player_can_lead_with_heart_if_hearts_broken(card)
        self._player_must_follow_suit(player, card)
        self._first_card_must_be_two_of_clubs(card)

        return card

    def _player_must_have_card(self, player: Player, card: Card):
        """Asserts that the player has the card they are trying to play."""
        assert card in player.hand, f"{player.name} does not have the card {card}"

    def _player_can_lead_with_heart_if_hearts_broken(self, card: Card):
        """Asserts that the player can lead with a heart if hearts have been broken."""
        if len(self.trick) == 0 and card.suit == Suit.HEARTS:
            assert self.hearts_broken, "Hearts have not been broken"

    def _player_must_follow_suit(self, player: Player, card: Card):
        """Asserts that the player must follow suit if possible."""
        if len(self.trick) == 0:
            return  # Player can play any card if they lead

        elif all(c.suit != self.trick[0].suit for c in player.hand):
            return  # Player can play any card if they don't have the suit

        else:
            assert card.suit == self.trick[0].suit, "Player must follow suit"

    def _first_card_must_be_two_of_clubs(self, card: Card):
        """Asserts that the first card played must be the two of clubs."""
        if self.is_first_card:
            assert card == Card(
                Rank.TWO, Suit.CLUBS
            ), "First card must be the two of clubs"
