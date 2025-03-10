from dnd_dungeon_generator import history, locations


def generate() -> None:
    """Generates a new, procedurally generated dungeon."""
    location_choice = locations.pick()
    history_choice = history.pick(location_choice["id"])

    print(f"Location: {location_choice['name']}")
    print(f"History: {history_choice['name']}")
