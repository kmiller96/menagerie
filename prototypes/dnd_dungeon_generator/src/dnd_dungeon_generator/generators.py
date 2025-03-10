import random

from dnd_dungeon_generator.seeds import locations, history

#############
## Helpers ##
#############


def _unroll_options() -> dict[str, list[dict]]:
    """Unrolls the options for each location."""

    unrolled = {}

    for location_list, options in history.items():
        for location in location_list:
            unrolled[location] = options

    return unrolled


################
## Generators ##
################


def pick_history(location: str) -> dict:
    """Picks a random history for a given location."""
    options = _unroll_options()
    return random.choice(options[location])


def pick_location() -> dict:
    return random.choice(locations)
