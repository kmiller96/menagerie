import random

history = {
    ("castle", "outpost"): [
        {
            "id": "active",
            "name": "Active",
        },
        {
            "id": "abandoned",
            "name": "Abandoned",
        },
        {
            "id": "ruined",
            "name": "Ruined",
        },
    ],
    ("mine",): [
        {
            "id": "active",
            "name": "Active",
        },
        {
            "id": "abandoned",
            "name": "Abandoned",
        },
        {
            "id": "collapsed",
            "name": "Collapsed",
        },
        {
            "id": "haunted",
            "name": "Haunted",
        },
        {
            "id": "infested",
            "name": "Infested",
        },
    ],
    ("cave",): [
        {
            "id": "normal",
            "name": "Normal",
        },
        {
            "id": "haunted",
            "name": "Haunted",
        },
        {
            "id": "infested",
            "name": "Infested",
        },
    ],
    ("temple",): [
        {
            "id": "cult",
            "name": "Cult",
        },
        {
            "id": "abandoned",
            "name": "Abandoned",
        },
        {
            "id": "ruined",
            "name": "Ruined",
        },
    ],
}


def _unroll_options() -> dict[str, list[dict]]:
    """Unrolls the options for each location."""

    unrolled = {}

    for location_list, options in history.items():
        for location in location_list:
            unrolled[location] = options

    return unrolled


def pick(location: str) -> dict:
    """Picks a random history for a given location."""
    options = _unroll_options()
    return random.choice(options[location])
