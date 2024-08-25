"""Defines the Pydantic models."""

import secrets
import hashlib
from pydantic import BaseModel, Field


class UserPassword(BaseModel):
    """Pydantic model for the user password."""

    algorithm: str = "sha256"
    hash: str
    salt: str = Field(default_factory=lambda: str(secrets.randbits(32)))

    @classmethod
    def from_string(cls, password: str):
        """Create a new instance from a string."""
        return cls(hash=hashlib.sha256(password.encode()).hexdigest())

    def verify(self, password: str) -> bool:
        """Verify the password against the stored hash."""
        if self.algorithm != "sha256":
            raise ValueError("Unsupported algorithm")

        return self.hash == hashlib.sha256(password.encode()).hexdigest()


class User(BaseModel):
    """Pydantic model for the user."""

    username: str
    password: UserPassword


class UserLoginRequest(BaseModel):
    """Pydantic model for the user login request."""

    username: str
    password: str
