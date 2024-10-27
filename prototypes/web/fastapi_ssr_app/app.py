from typing import Generator

import sqlite3
from contextlib import contextmanager

import fastapi
from fastapi.templating import Jinja2Templates

import pydantic

###############
## Constants ##
###############

DATABASE = "database.db"

############
## Models ##
############


class Post(pydantic.BaseModel):
    id: int
    author: str
    title: str
    content: str


###############
## Utilities ##
###############


@contextmanager
def connect_to_db() -> Generator[sqlite3.Connection]:
    """Connects to the database and returns a connection object."""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row

    yield conn

    conn.close()


##############
## Lifespan ##
##############


def lifespan(app: fastapi.FastAPI):
    # -- Create DB Tables -- #
    with connect_to_db() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS posts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                author TEXT NOT NULL,
                title TEXT NOT NULL,
                content TEXT NOT NULL
            )
            """
        )

        # -- Seed Data -- #
        # TODO: Remove seeding data
        posts_raw = [
            {
                "id": 1,
                "author": "author1",
                "title": "title1",
                "content": "content1",
            },
            {
                "id": 2,
                "author": "author2",
                "title": "title2",
                "content": "content2",
            },
        ]

        for record in posts_raw:
            conn.execute(
                "INSERT OR IGNORE INTO posts (id, author, title, content) VALUES (?, ?, ?, ?)",
                (record["id"], record["author"], record["title"], record["content"]),
            )

    yield


######################
## App & Middleware ##
######################

app = fastapi.FastAPI(lifespan=lifespan)

templates = Jinja2Templates(directory="templates")


@app.get("/")
def index(request: fastapi.Request):
    # -- Fetch Data -- #
    with connect_to_db() as conn:
        conn.row_factory = sqlite3.Row

        cursor = conn.execute("SELECT * FROM posts limit 20")
        posts = [Post.model_validate(dict(obj)) for obj in cursor.fetchall()]

    # -- Render -- #
    return templates.TemplateResponse(
        request=request,
        name="index.jinja",
        context={"posts": posts},
    )
