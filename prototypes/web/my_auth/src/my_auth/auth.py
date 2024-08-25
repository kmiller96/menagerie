import secrets
import json
from pathlib import Path
from contextlib import contextmanager
from typing import Annotated

import fastapi

from my_auth import models

USERS = [
    models.User(username="kale", password=models.UserPassword.from_string("miller")),
    models.User(username="katie", password=models.UserPassword.from_string("tobin")),
]


class SessionManager:
    def __init__(self, path: Path = "./sessions.json"):
        self.path = Path(path)
        self.sessions: dict[str, models.User] = {}

        self.load()

    def __getitem__(self, session_id: str) -> models.User:
        return self.get_user(session_id)

    def load(self):
        """Loads the session state from disk."""
        if Path(self.path).exists():
            with self.path.open() as f:
                self.sessions = {
                    session_id: models.User.model_validate(user_data)
                    for session_id, user_data in json.load(f).items()
                }

    def save(self):
        """Saves the session state to disk."""
        with open(self.path, "w") as f:
            json.dump(
                {
                    session_id: user.model_dump()
                    for session_id, user in self.sessions.items()
                },
                f,
            )

    @contextmanager
    def transaction(self):
        """Saves the session state to disk after a transaction."""
        self.load()
        yield
        self.save()

    def verify_user(self, username: str, password: str) -> models.User | None:
        for user in USERS:
            if user.username == username and user.password.verify(password):
                return user

        return None

    def create_session(self, user: models.User) -> str:
        with self.transaction():
            session_id = str(secrets.randbits(32))
            self.sessions[session_id] = user
            return session_id

    def get_user(self, session_id: str) -> models.User | None:
        return self.sessions.get(session_id)

    def delete_session(self, session_id: str):
        with self.transaction():
            if session_id in self.sessions:
                del self.sessions[session_id]


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
