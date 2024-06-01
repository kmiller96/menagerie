import json
import uuid
from pathlib import Path
from typing import Union

from fastapi import HTTPException, Request


from src.models import User, Session


class Database:
    def __init__(self, fpath: Path, *, lazy: bool = False):
        self.fpath = Path(fpath)

        if not lazy:
            self.load()

    def load(self):
        """Loads the data from the file."""
        if not self.fpath.exists():
            self.data = {}
            return

        with self.fpath.open() as f:
            self.data = json.load(f)

    def save(self):
        """Saves the data to the file."""
        with self.fpath.open("w") as f:
            json.dump(self.data, f)

    def create_table(self, name: str) -> "Database":
        """Creates a table in the database."""
        if name not in self.data:
            self.data[name] = {}

        self.save()
        return self

    ###########
    ## Users ##
    ###########

    def get_user(self, username: str) -> User:
        """Gets a user from the database."""
        user = self.data["users"].get(username)

        return None if user is None else User(**user)

    def add_user(self, user: User):
        """Adds a user to the database."""
        self.data["users"][user.username] = user.model_dump()

        self.save()
        return self

    ##############
    ## Sessions ##
    ##############

    def authenticate(self, request: Request) -> Session:
        """Authenticates a session. Raises a HTTPException if the session is invalid."""
        session = self.get_session_by_id(request.cookies.get("session_id"))

        if session is None:
            raise HTTPException(status_code=401, detail="Not authenticated")

        return session

    def get_session_by_id(self, session_id: str) -> Union[Session, None]:
        """Gets a session from the database."""
        session = self.data["sessions"].get(session_id)

        return None if session is None else Session(**session)

    def get_session(self, username: str) -> Union[Session, None]:
        """Gets a session from the database using the username."""
        for session in self.data["sessions"].values():
            if session["user"] == username:
                return Session(**session)

        return None

    def create_session(self, user: User) -> Session:
        """Creates a session for the user."""
        session = Session(
            id=uuid.uuid4().hex,
            user=user.username,
            expiration=0,
        )

        self.data["sessions"][session.id] = session.model_dump()

        self.save()
        return session

    def get_or_create_session(self, user: User) -> Session:
        """Gets or creates a session for the user."""
        session = self.get_session(user.username)

        if session is None:
            session = self.create_session(user)

        return session


def get_db() -> Database:
    """Returns the database. Used in the FastAPI application."""
    db = Database("db.json")

    db.create_table("users")
    db.create_table("sessions")

    return db
