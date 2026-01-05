"""Defines an MCP server for an email responder application."""

from mcp.server.fastmcp import FastMCP

import common

mcp = FastMCP("Email Responder", json_response=True)

###########
## Tools ##
###########


@mcp.tool()
def send_email(recipient: str, subject: str, body: str) -> str:
    """Simulates sending an email.

    In practice, this would probably do something like send an email with Outlook.
    However this might be easier to orchestrate in Power Automate or similar
    instead.
    """
    return f"Email sent to {recipient} with subject '{subject}'."


@mcp.tool()
def book_room(id: str, time: str) -> dict:
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


@mcp.tool()
def cancel_booking(id: str, time: str) -> dict:
    """Cancel a room booking at a specific time."""
    if common.cancel_booking(id, time):
        return {
            "status": "success",
            "message": f"Room {id} booking canceled for {time}.",
        }

    status = common.get_room_availability(id, time)
    if status == "unknown":
        message = f"Room {id} has no slot defined at {time}."
    else:
        message = f"Room {id} is not booked at {time}."

    return {
        "status": "error",
        "message": message,
    }


###############
## Resources ##
###############


@mcp.resource("rooms://list")
def list_rooms() -> list[dict]:
    """Retrieves a list of rooms that can be booked."""
    return common.list_rooms()


@mcp.resource("rooms://available/{time}")
def list_available_slots(time: str) -> list[str]:
    """Retrieves all available slots for a given time."""
    return common.find_available_rooms(time)


@mcp.resource("rooms://{id}/available")
def list_room_available_slots(id: str) -> list[str]:
    """Retrieves all available slots for a given room."""
    return common.list_available_slots_for_room(id)


@mcp.resource("rooms://{id}/{time}")
def room_availablity(id: str, time: str) -> dict:
    """Retrieves availability for a room at a specific booking time."""
    status = common.get_room_availability(id, time)
    return {"status": status}


@mcp.resource("rooms://{id}")
def room_info(id: str) -> dict:
    """Retrieve full information for a specific room."""
    return common.get_room(id)


#############
## Prompts ##
#############

# TODO: What prompts should I define?

########################
## Run the MCP server ##
########################

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
