"""Defines the CLI of the application."""

from pathlib import Path

import click

from . import main, algorithms  # pylint: disable=import-error

OUTPATH = Path("PUZZLES")


@click.group()
def cli():
    pass


@cli.command()
@click.argument("path", type=click.Path(exists=True))
def run(path: str):
    puzzles = main.search(Path(path))

    output = ""

    for t, puzzle in algorithms.groupby(puzzles, lambda p: p.type):
        output += f"{t}:\n"

        for p in puzzle:
            output += f"    [ ] {p.description}\n"

        output += "\n"

    OUTPATH.write_text(output, encoding="utf-8")
