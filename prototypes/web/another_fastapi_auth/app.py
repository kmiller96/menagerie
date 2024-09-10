from typing import Annotated

import fastapi
from fastapi.security.http import (
    HTTPBasic,
    HTTPBasicCredentials,
    HTTPBearer,
    HTTPAuthorizationCredentials,
)

from pydantic import BaseModel


app = fastapi.FastAPI()

basic = HTTPBasic()
bearer = HTTPBearer()

################
## Decorators ##
################


def require_auth(
    authorization: Annotated[HTTPAuthorizationCredentials, fastapi.Depends(bearer)],
):
    """Dependency that protects an endpoint to ensure that authentication is required."""

    if authorization.credentials != "abc123":
        raise fastapi.HTTPException(status_code=401, detail="Unauthorized")

    return True


##############
## Standard ##
##############


@app.get("/")
def unprotected():
    return {"message": "Unprotected route"}


@app.get("/protected")
def protected(auth: Annotated[bool, fastapi.Depends(require_auth)]):
    return {"message": "Protected route"}


##########
## Auth ##
##########


class User(BaseModel):
    username: str
    password: str  # NOTE: This is a hash in a real application


class LoginRequest(BaseModel):
    username: str
    password: str


@app.post("/login")
def login(
    credentials: Annotated[HTTPBasicCredentials, fastapi.Depends(basic)],
    response: fastapi.Response,
):
    if credentials.username == "test" and credentials.password == "test":
        response.status_code = 200
        return {"token": "abc123"}

    else:
        response.status_code = 401
        return {"message": "Login failed"}


@app.post("/logout")
def logout():
    return {"message": "Logout successful"}
