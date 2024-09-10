import fastapi
from pydantic import BaseModel


app = fastapi.FastAPI()

##############
## Standard ##
##############


@app.get("/")
def unprotected():
    return {"message": "Unprotected route"}


@app.get("/protected")
def protected():
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
def login(req: LoginRequest, response: fastapi.Response):
    if req.username == "test" and req.password == "test":
        response.status_code = 200
        return {"message": "Login successful"}

    else:
        response.status_code = 401
        return {"message": "Login failed"}


@app.post("/logout")
def logout():
    return {"message": "Logout successful"}
