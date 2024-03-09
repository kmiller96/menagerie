"""Injects in a custom stylesheet for a Notion site.

I've used python for this because Caddy was being a pain in the ass. This won't
scale, but I don't care...
"""

import re
import asyncio

from fastapi import FastAPI, Request, Response
import requests

URL = "https://prometheus-ai.notion.site/"
STYLE_STRING = "<style>h2 {color: red;} </style>"

app = FastAPI()


def notion_specific_path(path: str):
    prefixes = ["image", "katex", "_assets", "api", "f/refresh"]

    for p in prefixes:
        if path.startswith(p):
            return True


@app.api_route("/{path:path}", methods=["GET", "POST", "OPTIONS", "HEAD"])
def main(request: Request):
    path = str(request.url).replace(str(request.base_url), "")

    if request.method == "POST":
        response = requests.post(
            URL + path,
            headers={"Content-Type": "application/json"},
            data=asyncio.run(request.body()),
        )
    else:
        response = requests.request(request.method.upper(), URL + path)

    data = response.text

    if not notion_specific_path(path):
        data = re.sub(
            r"<head.*?>(.*?)<\/head.*?>",
            r"<head>\1" + STYLE_STRING + r"</head>",
            data,
            flags=re.DOTALL,
        )

    return Response(
        content=data,
        status_code=response.status_code,
    )
