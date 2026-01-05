"""Defines the API service for the room booking system.

Start the development server with:

```bash
(uv run) fastapi dev
```

Run the production server with:

```bash
(uv run) fastapi run
```
"""

from fastapi import FastAPI

import common

app = FastAPI()


@app.get("/")
def healthcheck():
    return {"status": "ok"}


@app.get("/rooms")
def list_rooms():
    """List all of the rooms that can be booked."""
    return common.list_rooms()


@app.get("/rooms/available")
def list_available_slots(time: str):
    """List all available rooms for a given time."""
    return common.find_available_rooms(time)


@app.get("/rooms/{id}/available")
def list_room_available_slots(id: str):
    """List all available slots for a given room."""
    return common.list_available_slots_for_room(id)


@app.get("/rooms/{id}")
def room_info(id: str):
    """Retrieve full information for a specific room."""
    return common.get_room(id)


@app.get("/rooms/{id}/{time}")
def room_availablity(id: str, time: str):
    """Retrieve availability for a room at a specific booking time."""
    status = common.get_room_availability(id, time)
    return {"status": status}


@app.post("/rooms/{id}/{time}/book")
def book_room(id: str, time: str):
    """Book a room at a specific time."""
    if common.book_room(id, time):
        return {
            "status": "success",
            "message": f"Room {id} booked for {time}.",
        }

    status = common.get_room_availability(id, time)
    if status == "unknown":
        message = f"Room {id} has no slot defined at {time}."
    else:
        message = f"Room {id} is not available at {time}."

    return {
        "status": "error",
        "message": message,
    }
