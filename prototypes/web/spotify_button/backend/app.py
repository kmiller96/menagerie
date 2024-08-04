"""Defines the simple backend that interprets and proxies the requests to the Spotify API."""

import json
from functools import cache

import fastapi
from fastapi.middleware.cors import CORSMiddleware
import spotipy

app = fastapi.FastAPI()

#############
## Globals ##
#############

CREDENTIALS_PATH = "credentials.json"
SPOTIFY_SCOPE = (
    "user-read-playback-state user-modify-playback-state user-read-currently-playing"
)

################
## Middleware ##
################


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost",
        "http://localhost:8080",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


##################
## Dependencies ##
##################


@cache
def get_spotify_client() -> spotipy.Spotify:
    """Gets the Spotify client from the spotipy library."""
    with open(CREDENTIALS_PATH, "r") as f:
        credentials = json.load(f)

    return spotipy.Spotify(
        auth_manager=spotipy.SpotifyOAuth(
            client_id=credentials["client_id"],
            client_secret=credentials["client_secret"],
            redirect_uri=credentials["redirect_uri"],
            scope=SPOTIFY_SCOPE,
        )
    )


############
## Routes ##
############


@app.get("/")
def healthcheck():
    return {"status": "ok"}


@app.get("/callback")
def callback(code: str):
    return {"code": code}


@app.get("/user")
def get_user(
    client: spotipy.Spotify = fastapi.Depends(get_spotify_client),
):
    """Gets the current user."""
    return client.current_user()


@app.get("/song/{link:path}")
def play_song(
    link: str,
    client: spotipy.Spotify = fastapi.Depends(get_spotify_client),
):
    """Plays a song by its ID."""
    track = client.track(link)

    client.start_playback(
        device_id=client.devices()["devices"][0]["id"],
        uris=[f"spotify:track:{track['id']}"],
    )
    return {"status": "success"}
