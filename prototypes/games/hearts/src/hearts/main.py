"""Defines the main game loop."""

from hearts.pile import Pile
from hearts.players import Player
from hearts.logic import create_deck, determine_starting_player, winning_card


def play(player_names: list[str]):
    """Runs the main game loop."""

    # -- Initialise the players -- #
    num_players = len(player_names)

    # -- Initialise the deck -- #
    deck = create_deck()
    hands = deck.split(num_players)

    # -- Initialise the players -- #
    players = [Player(name, hand=hand) for name, hand in zip(player_names, hands)]

    # -- Main game loop -- #
    leader = determine_starting_player(players)
    trick_number = 0

    while trick_number < 13:
        print("Starting trick: ", trick_number)
        trick = Pile()

        # -- Play the trick -- #
        start = players.index(leader)
        play_order = [players[(start + i) % num_players] for i in range(num_players)]

        for current_player in play_order:
            card = current_player.play()
            trick.add(card)

        # -- Determine the winner -- #
        winner = play_order[trick.cards.index(winning_card(trick))]
        winner.tricks.append(trick)

        leader = winner
        trick_number += 1

        print("Cards in the trick: ", trick.cards)
        print(f"Player {winner.name} wins the trick.")
        print()

    return


###############
## Utilities ##
###############
