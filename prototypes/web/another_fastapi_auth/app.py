from __future__ import annotations

from functools import cache
from datetime import datetime, timezone, timedelta
from typing import Annotated

import fastapi
from fastapi.security.http import (
    HTTPBasic,
    HTTPBasicCredentials,
    HTTPBearer,
    HTTPAuthorizationCredentials,
)

import jwt


app = fastapi.FastAPI()

####################
## Authentication ##
####################

basic_auth = HTTPBasic()
bearer_auth = HTTPBearer()

BasicAuthDeps = Annotated[HTTPBasicCredentials, fastapi.Depends(basic_auth)]
BearerAuthDeps = Annotated[HTTPAuthorizationCredentials, fastapi.Depends(bearer_auth)]

USERS = [
    {"username": "test", "password": "test"},
]


class AuthenticationService:
    """Simple authentication service for the application using JWT."""

    ALGORITHM = "HS256"
    BLACKLIST = set()

    def __init__(self, secret: str) -> None:
        self.secret = secret

    def blacklist(self, token: str) -> None:
        """Blacklists a token."""
        self.BLACKLIST.add(token)

    def authenticate(self, username: str, password: str) -> str:
        """Authenticates a user. Raises an exception if the user is not found."""
        for user in USERS:
            if user["username"] == username and user["password"] == password:
                return self.create_access_token(username)
        else:
            raise fastapi.HTTPException(status_code=401, detail="Unauthorized")

    def create_access_token(self, user: str) -> str:
        """Generates an access token."""
        return jwt.encode(
            payload={
                "sub": user,
                "exp": datetime.now(timezone.utc) + timedelta(minutes=15),
            },
            key=self.secret,
            algorithm=self.ALGORITHM,
        )

    def decode_access_token(self, token: str) -> dict:
        """Decodes an access token."""
        return jwt.decode(token, self.secret, algorithms=[self.ALGORITHM])

    def validate(self, token: str) -> bool:
        """Validates an access token."""
        # -- Check if token is blacklisted -- #
        if token in self.BLACKLIST:
            raise fastapi.HTTPException(status_code=401, detail="Invalid token")

        # -- Check if token is valid -- #
        try:
            self.decode_access_token(token)
        except jwt.InvalidTokenError:
            raise fastapi.HTTPException(status_code=400, detail="Invalid token")

        except jwt.ExpiredSignatureError:
            raise fastapi.HTTPException(status_code=401, detail="Token expired")

        else:
            return True


@cache
def get_auth_service() -> AuthenticationService:
    """Retrieves the authentication service."""
    return AuthenticationService("secret")


def require_token(
    token: BearerAuthDeps,
    auth: Annotated[AuthenticationService, fastapi.Depends(get_auth_service)],
):
    """Dependency that protects an endpoint to ensure that a valid token is provided."""
    if not auth.validate(token.credentials):
        raise fastapi.HTTPException(status_code=401, detail="Unauthorized")

    return True


AuthDeps = Annotated[AuthenticationService, fastapi.Depends(get_auth_service)]
RequireTokenDeps = Annotated[bool, fastapi.Depends(require_token)]


@app.post("/login")
def login(
    credentials: BasicAuthDeps,
    auth: AuthDeps,
):
    """Logs a user into the application, issuing them a temporary access token."""
    return {"token": auth.authenticate(credentials.username, credentials.password)}


@app.get("/logout")
def logout(
    token: BearerAuthDeps,
    auth: AuthDeps,
):
    """Logs a user out of the application, invalidating their access token."""
    auth.blacklist(token.credentials)  # Invalidate token
    return {"message": "Logout successful"}


##############
## Standard ##
##############


@app.get("/")
def unprotected():
    return {"message": "Unprotected route"}


@app.get("/protected", dependencies=[fastapi.Depends(require_token)])
def protected():
    return {"message": "Protected route"}
