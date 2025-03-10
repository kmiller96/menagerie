from dnd_dungeon_generator import generators


def generate() -> None:
    """Generates a new, procedurally generated dungeon."""
    location_choice = generators.pick_location()
    history_choice = generators.pick_history(location_choice.id)
    monster_choice = generators.pick_monster(
        location=location_choice.id,
        history=history_choice.id,
    )

    print(f"Location: {location_choice.name}")
    print(f"History: {history_choice.name}")
    print(f"Monster: {monster_choice.name}")
