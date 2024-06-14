"""Defines the main game loop."""

from hearts.pile import Pile
from hearts.players import Player
from hearts.rules import Umpire
from hearts.logic import create_deck, determine_starting_player, winning_card

##################
## Main Routine ##
##################


def play(player_names: list[str]):
    """Runs the main game loop."""

    num_players = len(player_names)

    # -- Initialise the game -- #
    umpire = Umpire()
    deck = create_deck()
    players = [
        Player(name, hand=hand)
        for name, hand in zip(player_names, deck.split(num_players))
    ]

    # -- Main game loop -- #
    leader = determine_starting_player(players)
    trick_number = 0

    while trick_number < 13:
        winner = _play_trick(players, leader, umpire)

        leader = winner
        trick_number += 1

        print(f"Player {winner.name} wins the trick.")
        print()

    return


#################
## Subroutines ##
#################


def _play_trick(players: list[Player], leader: Player, umpire: Umpire) -> Player:
    """Plays a single trick."""
    num_players = len(players)

    # -- Determine play order -- #
    start = players.index(leader)
    play_order = [players[(start + i) % num_players] for i in range(num_players)]

    # -- Play the trick -- #
    trick = Pile()
    umpire.trick = trick

    for current_player in play_order:
        card = current_player.play(umpire.check)
        print(f"{current_player.name} plays: {card}")
        input()
        trick.add(card)

    # -- Determine the winner -- #
    winner = play_order[trick.cards.index(winning_card(trick))]
    winner.tricks.append(trick)

    return winner
