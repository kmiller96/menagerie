from typing import Annotated

import fastapi

from my_auth import models, auth

app = fastapi.FastAPI()


@app.get("/")
def healthcheck():
    """Health check."""
    return {}


@app.post("/login")
def login(
    req: models.UserLoginRequest,
    request: fastapi.Request,
    response: fastapi.Response,
    manager: Annotated[auth.SessionManager, fastapi.Depends(auth.get_session_manager)],
):
    """Allows the user to authenticate."""

    user = manager.verify_user(req.username, req.password)

    if not user:
        raise fastapi.HTTPException(
            status_code=401,
            detail="Invalid username or password",
        )
    else:
        session_id = manager.create_session(user)
        response.set_cookie(key="session_id", value=session_id)
        return {"status": "logged in"}


@app.post("/logout")
def logout(
    request: fastapi.Request,
    response: fastapi.Response,
    manager: Annotated[auth.SessionManager, fastapi.Depends(auth.get_session_manager)],
):
    """Allows the user to logout."""

    if session_id := request.cookies.get("session_id"):
        manager.delete_session(session_id)
        response.delete_cookie("session_id")
        return {"status": "logged out"}
    else:
        raise fastapi.HTTPException(
            status_code=401,
            detail="Unauthenticated",
        )


@app.get("/unprotected")
def unprotected():
    """An unprotected route."""
    return {"message": "Unprotected route"}


@app.get("/protected")
def protected(
    user: Annotated[models.User, fastapi.Depends(auth.verify_authentication)],
):
    """A protected route."""
    return {"user": user}
