# NOTE: In practice, this data would come from a room booking system.
ROOMS = {
    "101": {
        "09:00": "available",
        "10:00": "booked",
        "11:00": "available",
    },
    "102": {
        "09:00": "booked",
        "10:00": "booked",
        "11:00": "available",
    },
}


def list_rooms() -> list[str]:
    """Retrieves a list of rooms that can be booked."""
    return list(ROOMS.keys())


def list_available_slots_for_room(id: str) -> list[str]:
    """Retrieves all available slots for a given room."""
    room = ROOMS.get(id, {})
    available_slots = [time for time, status in room.items() if status == "available"]
    return available_slots


def find_available_rooms(time: str) -> list[str]:
    """Finds all rooms that are available at a specific booking time."""
    available_rooms = []

    for room_id, schedule in ROOMS.items():
        if schedule.get(time) == "available":
            available_rooms.append(room_id)

    return available_rooms


def get_room_availability(id: str, time: str) -> str:
    """Retrieves availability for a room at a specific booking time."""
    room = ROOMS.get(id, {})
    status = room.get(time, "unknown")
    return status


def update_room_status(id: str, time: str, status: str) -> bool:
    """Updates the in-memory availability status for a room/time slot."""
    room = ROOMS.get(id)
    if room is None:
        return False

    room[time] = status
    return True


def book_room(id: str, time: str) -> bool:
    """Marks a room/time slot as booked if available."""
    if get_room_availability(id, time) != "available":
        return False

    return update_room_status(id, time, "booked")
