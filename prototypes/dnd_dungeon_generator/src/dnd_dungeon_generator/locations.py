import random

locations = [
    {
        "id": "castle",
        "name": "Castle",
    },
    {
        "id": "outpost",
        "name": "Outpost",
    },
    {
        "id": "mine",
        "name": "Mine",
    },
    {
        "id": "temple",
        "name": "Temple",
    },
    {
        "id": "cave",
        "name": "Cave",
    },
]


def pick() -> dict:
    return random.choice(locations)
