import json

import fastapi
from fastapi_sso.sso.google import GoogleSSO


# -- Load secrets -- #
with open("secrets.json") as f:
    obj = json.load(f)

    CLIENT_ID = obj["client_id"]
    CLIENT_SECRET = obj["client_secret"]


# -- Define app -- #
app = fastapi.FastAPI()

google_sso = GoogleSSO(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri="http://localhost:8000/google/callback",
    allow_insecure_http=True,
)


@app.get("/google/login")
async def google_login():
    with google_sso:
        return await google_sso.get_login_redirect()


@app.get("/google/callback")
async def google_callback(request: fastapi.Request):
    with google_sso:
        user = await google_sso.verify_and_process(request)
    return user
