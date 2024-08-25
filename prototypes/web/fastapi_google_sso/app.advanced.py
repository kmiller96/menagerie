import datetime
import json

from jose import jwt

from fastapi import FastAPI, Depends, HTTPException, Security, Request
from fastapi.responses import RedirectResponse
from fastapi.security import APIKeyCookie
from fastapi_sso.sso.google import GoogleSSO
from fastapi_sso.sso.base import OpenID


# -- Load secrets -- #
with open("secrets.json") as f:
    secrets = json.load(f)

    CLIENT_ID = secrets["client_id"]
    CLIENT_SECRET = secrets["client_secret"]
    SECRET_KEY = secrets["secret_key"]


## -- Define app -- #
sso = GoogleSSO(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri="http://localhost:8000/auth/callback",
)

app = FastAPI()


async def get_logged_user(cookie: str = Security(APIKeyCookie(name="token"))) -> OpenID:
    """Get user's JWT stored in cookie 'token', parse it and return the user's OpenID."""
    try:
        claims = jwt.decode(cookie, key=SECRET_KEY, algorithms=["HS256"])
        return OpenID(**claims["pld"])
    except Exception as error:
        raise HTTPException(
            status_code=401, detail="Invalid authentication credentials"
        ) from error


@app.get("/protected")
async def protected_endpoint(user: OpenID = Depends(get_logged_user)):
    """This endpoint will say hello to the logged user.
    If the user is not logged, it will return a 401 error from `get_logged_user`."""
    return {
        "message": f"You are very welcome, {user.email}!",
    }


@app.get("/auth/login")
async def login():
    """Redirect the user to the Google login page."""
    with sso:
        return await sso.get_login_redirect()


@app.get("/auth/logout")
async def logout():
    """Forget the user's session."""
    response = RedirectResponse(url="/protected")
    response.delete_cookie(key="token")
    return response


@app.get("/auth/callback")
async def login_callback(request: Request):
    """Process login and redirect the user to the protected endpoint."""
    with sso:
        openid = await sso.verify_and_process(request)
        if not openid:
            raise HTTPException(status_code=401, detail="Authentication failed")
    # Create a JWT with the user's OpenID
    expiration = datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(
        days=1
    )
    token = jwt.encode(
        {"pld": openid.model_dump(), "exp": expiration, "sub": openid.id},
        key=SECRET_KEY,
        algorithm="HS256",
    )
    response = RedirectResponse(url="/protected")
    response.set_cookie(
        key="token", value=token, expires=expiration
    )  # This cookie will make sure /protected knows the user
    return response


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
