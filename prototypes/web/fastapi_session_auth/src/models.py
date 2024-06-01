"""Defines the models for the application."""

import hashlib

from pydantic import BaseModel


####################
## Authentication ##
####################


class LoginRequest(BaseModel):
    """The request made to the login endpoint."""

    username: str
    password: str


class User(BaseModel):
    """A user in the system."""

    username: str

    hash: str
    salt: str

    @classmethod
    def from_login_request(cls, request: "LoginRequest") -> "User":
        """Creates a user from a login request."""
        # -- Hash plaintext password -- #
        salt = ""  # TODO: Generate a salt
        hash = hashlib.sha256((request.password + salt).encode()).hexdigest()

        # -- Return User object -- #
        return cls(
            username=request.username,
            hash=hash,
            salt=salt,
        )


class Session(BaseModel):
    """A session for a user."""

    id: str
    user: str
    expiration: int
