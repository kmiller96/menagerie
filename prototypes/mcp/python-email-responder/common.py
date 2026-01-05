# NOTE: In practice, this data would come from a room booking system.
ROOMS = {
    "101": {
        "details": {
            "max_occupants": 2,
            "size_m2": 8,
            "features": [],
        },
        "availability": {
            "09:00": "available",
            "10:00": "booked",
            "11:00": "available",
            "12:00": "available",
            "13:00": "booked",
            "14:00": "available",
            "15:00": "available",
            "16:00": "booked",
            "17:00": "available",
        },
    },
    "102": {
        "details": {
            "max_occupants": 4,
            "size_m2": 12,
            "features": ["whiteboard"],
        },
        "availability": {
            "09:00": "booked",
            "10:00": "booked",
            "11:00": "available",
            "12:00": "available",
            "13:00": "available",
            "14:00": "booked",
            "15:00": "available",
            "16:00": "available",
            "17:00": "booked",
        },
    },
    "103": {
        "details": {
            "max_occupants": 6,
            "size_m2": 18,
            "features": ["whiteboard"],
        },
        "availability": {
            "09:00": "available",
            "10:00": "available",
            "11:00": "booked",
            "12:00": "booked",
            "13:00": "available",
            "14:00": "available",
            "15:00": "booked",
            "16:00": "available",
            "17:00": "available",
        },
    },
    "104": {
        "details": {
            "max_occupants": 8,
            "size_m2": 24,
            "features": ["whiteboard", "projector"],
        },
        "availability": {
            "09:00": "available",
            "10:00": "booked",
            "11:00": "available",
            "12:00": "available",
            "13:00": "booked",
            "14:00": "available",
            "15:00": "available",
            "16:00": "booked",
            "17:00": "available",
        },
    },
    "105": {
        "details": {
            "max_occupants": 20,
            "size_m2": 45,
            "features": ["projector"],
        },
        "availability": {
            "09:00": "booked",
            "10:00": "available",
            "11:00": "available",
            "12:00": "available",
            "13:00": "booked",
            "14:00": "available",
            "15:00": "booked",
            "16:00": "available",
            "17:00": "available",
        },
    },
}


def list_rooms() -> list[dict]:
    """Retrieves details for all rooms without availability."""
    return [
        {"id": room_id, "details": data.get("details", {})}
        for room_id, data in ROOMS.items()
    ]


def list_available_slots_for_room(id: str) -> list[str]:
    """Retrieves all available slots for a given room."""
    room = ROOMS.get(id, {})
    availability = room.get("availability", {})
    available_slots = [
        time for time, status in availability.items() if status == "available"
    ]
    return available_slots


def find_available_rooms(time: str) -> list[str]:
    """Finds all rooms that are available at a specific booking time."""
    available_rooms = []

    for room_id, schedule in ROOMS.items():
        availability = schedule.get("availability", {})
        if availability.get(time) == "available":
            available_rooms.append(room_id)

    return available_rooms


def get_room_availability(id: str, time: str) -> str:
    """Retrieves availability for a room at a specific booking time."""
    room = ROOMS.get(id, {})
    availability = room.get("availability", {})
    status = availability.get(time, "unknown")
    return status


def get_room_details(id: str) -> dict:
    """Retrieves details for a specific room."""
    room = ROOMS.get(id, {})
    return room.get("details", {})


def get_room(id: str) -> dict:
    """Retrieves full information for a specific room."""
    room = ROOMS.get(id, {})
    return {"id": id, **room} if room else {}


def update_room_status(id: str, time: str, status: str) -> bool:
    """Updates the in-memory availability status for a room/time slot."""
    room = ROOMS.get(id, {})
    availability = room.get("availability")
    if availability is None:
        return False

    availability[time] = status
    return True


def book_room(id: str, time: str) -> bool:
    """Marks a room/time slot as booked if available."""
    if get_room_availability(id, time) != "available":
        return False

    return update_room_status(id, time, "booked")


def cancel_booking(id: str, time: str) -> bool:
    """Marks a room/time slot as available if currently booked."""
    if get_room_availability(id, time) != "booked":
        return False

    return update_room_status(id, time, "available")
