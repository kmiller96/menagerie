"""Data structure to represent a game of hearts. Contains the global state."""

from hearts.state import GameState
from hearts.players import Player
from hearts.cards import Card, Rank, Suit
from hearts.pile import Pile


class Game:
    """Controls the flow of the game and enforce the rules."""

    def __init__(self, players: list[Player]):
        self.state = GameState(players)

        self.players = players
        self.num_players = len(players)

    def play_trick(self):
        """Plays a single trick."""

        for player in self.state.play_order:
            try:
                choice = player.play(state=self.state)
                card = self.state.validate(  # Final sanity check of the card
                    player=player,
                    card=choice,
                )

            except AssertionError as e:
                raise RuntimeError(
                    f"{player.name} played an invalid card: {choice}"
                ) from e

            else:
                print(f"{player.name} plays: {card}")
                player.hand.remove(card)
                self.state.trick.add(card)

        winner = self.state.resolve()

        print(f"Player {winner.name} wins the trick.")
        print()

    def play_game(self):
        """Plays a single game."""
        # -- Shuffle & deal deck -- #
        deck = Pile([Card(rank, suit) for rank in Rank for suit in Suit])
        deck.shuffle()

        for player, hand in zip(self.players, deck.split(self.num_players)):
            player.hand = hand

        # -- Determine initial starting player -- #
        for player in self.players:
            if Card(Rank.TWO, Suit.CLUBS) in player.hand:
                self.state.leader = player
                break

        # -- Play 13 tricks -- #
        for _ in range(13):
            self.play_trick()

        # -- Score the game -- #
        scores = {
            player: sum(card.points for trick in player.tricks for card in trick)
            for player in self.players
        }

        for player, score in scores.items():
            print(f"{player.name} scored: {score}")
