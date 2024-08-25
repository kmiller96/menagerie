from typing import Annotated

import fastapi

from my_auth.auth import SessionManager


def get_session_manager() -> SessionManager:
    return SessionManager()


def verify_authentication(
    requests: fastapi.Request,
    manager: Annotated[SessionManager, fastapi.Depends(get_session_manager)],
):
    """Dependable function the checks that the user is authenticated.

    If the user is authenticated, this will return a `User` model.
    """

    if not (session_id := requests.cookies.get("session_id")):
        raise fastapi.HTTPException(
            status_code=401,
            detail="Unauthenticated",
        )

    if not (user := manager.get_user(session_id)):
        raise fastapi.HTTPException(
            status_code=404,
            detail="Session not found.",
        )

    return user
