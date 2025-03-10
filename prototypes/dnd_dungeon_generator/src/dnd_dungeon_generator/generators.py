import random
import itertools

from dnd_dungeon_generator.seeds import locations, history, monsters
from dnd_dungeon_generator.types import History, Monster, Location


def pick_location() -> Location:
    return random.choice(locations)


def pick_history(location: str) -> History:
    """Picks a random history for a given location."""

    unrolled = {}

    for config, options in history.items():
        for loc in config.locations:
            unrolled[loc] = options

    return random.choice(unrolled[location])


def pick_monster(location: str, history: str) -> Monster:
    """Picks a random monster for a given location and history."""
    unrolled = {}

    for config, options in monsters.items():
        for loc, hist in itertools.product(config.locations, config.history):
            if (loc, hist) not in unrolled:
                unrolled[(loc, hist)] = []

            unrolled[(loc, hist)] += options

    return random.choice(unrolled[(location, history)])
