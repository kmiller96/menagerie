"""Defines the authentication for the application."""

from fastapi import APIRouter, Depends, HTTPException, Response

from src.models import User, LoginRequest
from src.db import Database, get_db


router = APIRouter()


@router.get("/")
def get_current_user() -> User:
    """Returns the current user, if they are logged in."""
    return User(username="fakeuser", hash="1234", salt="5678")


@router.post("/register")
def register(
    login_request: LoginRequest,
    response: Response,
    db: Database = Depends(get_db),
):
    """Registers a new user.

    This endpoint will take the user's username and password, and create a new user
    in the database.
    """

    # -- Check if user exists -- #
    if db.get_user(username=login_request.username) is not None:
        raise HTTPException(status_code=400, detail="User already exists")

    # -- Create the user -- #
    user = User.from_login_request(login_request)

    # -- Add user to database -- #
    db.add_user(user)

    # -- Attach session cookie -- #
    session = db.get_or_create_session(user)
    response.set_cookie(key="session_id", value=session.id)

    return {"message": "Successfully registered."}


@router.post("/login")
def login(
    login_request: LoginRequest,
    response: Response,
    db: Database = Depends(get_db),
):
    """Logs in the user.

    This endpoint will take the user's username and password, and attach a session
    cookie if the credentials are correct.
    """

    request = User.from_login_request(login_request)
    user = db.get_user(username=login_request.username)

    # -- Check if valid login -- #
    if user is None or request.hash != user.hash:
        raise HTTPException(status_code=401, detail="Invalid username or password")

    # -- Attach session cookie -- #
    session = db.get_or_create_session(user)
    response.set_cookie(key="session_id", value=session.id)

    return {"message": "Successfully logged in."}
