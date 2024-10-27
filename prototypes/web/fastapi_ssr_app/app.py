from typing import Annotated, Generator

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
    id: None | int = None
    author: str = pydantic.Field(default="Anonymous")
    title: str = pydantic.Field(min_length=1)
    content: str = pydantic.Field(min_length=1)


###############
## Utilities ##
###############


@contextmanager
def connect_to_db() -> Generator[sqlite3.Connection, None, None]:
    """Connects to the database and returns a connection object."""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row

    yield conn

    conn.commit()
    conn.close()


def insert_post(conn: sqlite3.Connection, post: Post):
    conn.execute(
        "INSERT OR REPLACE INTO posts (id, author, title, content) VALUES (?, ?, ?, ?)",
        (post.id, post.author, post.title, post.content),
    )


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

        # -- Seed Data -- #  TODO: Remove seeding data
        posts = [
            Post(id=1, author="author1", title="title1", content="content1"),
            Post(id=2, author="author2", title="title2", content="content2"),
        ]

        for record in posts:
            insert_post(conn, Post.model_validate(record))

    yield


######################
## App & Middleware ##
######################

app = fastapi.FastAPI(lifespan=lifespan)

templates = Jinja2Templates(directory="templates")


@app.get("/")
def index(
    request: fastapi.Request,
    response: fastapi.Response,
    error: Annotated[None | str, fastapi.Cookie(alias="X-Error")] = None,
):
    # -- Fetch Data -- #
    with connect_to_db() as conn:
        conn.row_factory = sqlite3.Row

        cursor = conn.execute("SELECT * FROM posts limit 20")
        posts = [Post.model_validate(dict(obj)) for obj in cursor.fetchall()]

    # -- Render -- #
    response = templates.TemplateResponse(
        request=request,
        name="index.jinja",
        context={"posts": posts, "error": error},
    )

    if error:
        response.delete_cookie("X-Error")

    return response


@app.post("/post")
def create_post(
    response: fastapi.Response,
    author: Annotated[str, fastapi.Form()],
    title: Annotated[str, fastapi.Form()],
    content: Annotated[str, fastapi.Form()],
):
    error: None | str = None

    # -- Save Data -- #
    try:
        post = Post(author=author, title=title, content=content)

        with connect_to_db() as conn:
            insert_post(conn, post)

    except pydantic.ValidationError:
        error = "Invalid form submission."

    except Exception as e:
        error = str(e)

    # -- Redirect -- #
    response = fastapi.responses.RedirectResponse(
        url="/",
        status_code=fastapi.status.HTTP_303_SEE_OTHER,
    )

    if error:
        response.set_cookie("X-Error", error)

    return response
