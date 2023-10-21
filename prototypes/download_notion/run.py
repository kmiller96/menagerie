"""Pulls a page from Notion and downloads it to the disk."""

import json
from pathlib import Path

import typer
from notion_client import Client

HERE = Path(__file__).parent


##################
## Main Routine ##
##################


def main(url: str):
    client = init_client()
    page_id = url_to_id(url)

    metadata = client.pages.retrieve(page_id=page_id)
    content = client.blocks.children.list(block_id=page_id)

    typer.echo(
        format_output(
            metadata=metadata,
            content=content,
        )
    )


#############
## Helpers ##
#############


def init_client() -> Client:
    try:
        secret = (HERE / "secret.txt").read_text()
    except FileNotFoundError:
        raise FileNotFoundError("`secret.txt` not found. Did you create it?")
    else:
        return Client(auth=secret)


def url_to_id(url: str) -> str:
    return url.split("/")[-1].split("-")[-1]


def format_output(metadata: dict, content: str) -> str:
    return json.dumps({"metadata": metadata, "content": content})


if __name__ == "__main__":
    typer.run(main)
