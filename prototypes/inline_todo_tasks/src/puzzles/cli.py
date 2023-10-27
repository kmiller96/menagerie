"""Defines the CLI of the application."""

from pathlib import Path

import click

from . import main, formatter  # pylint: disable=import-error


@click.group()
def cli():
    pass


@cli.command()
@click.option("-f", "--format", type=click.Choice(["todo", "json"]), default="todo")
@click.argument("outpath", type=click.Path(file_okay=True, dir_okay=False))
@click.argument("path", type=click.Path(exists=True))
def run(format: str, outpath: str, path: str):
    """Extracts all puzzles from the supplied path."""
    outpath: Path = Path(outpath)
    path: Path = Path(path)

    puzzles = main.search(path)
    fmt = formatter.Formatter(puzzles)

    if format == "json":
        outpath.write_text(fmt.to_json(), encoding="utf-8")
    elif format == "todo":
        outpath.write_text(fmt.to_todo(), encoding="utf-8")
    else:
        raise ValueError(f"Unknown format: {format}")
