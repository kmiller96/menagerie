"""Defines the CLI of the application."""

# pylint: disable=import-error,redefined-builtin

import sys
from pathlib import Path

import click

from . import main


@click.group()
def cli():
    pass


@cli.command()
@click.option("-f", "--format", type=click.Choice(["todo", "json"]), default="todo")
@click.argument("path", type=click.Path(exists=True))
def extract(path: str, *, format: str = "todo"):
    """Extracts all puzzles from the supplied path."""
    click.echo(main.extract(Path(path), format))


@cli.command()
@click.argument("path", type=click.Path(exists=True))
def assign(path: str):
    """Finds puzzles with IDs and assign them an ID."""
    main.assign(Path(path))


@cli.command()
@click.argument("path", type=click.Path(exists=True))
def check(path: str):
    """Validates that all puzzles have IDs."""
    errors = main.check(Path(path))

    if len(errors) > 0:
        for error in errors:
            click.echo(error[1], err=True)

        sys.exit(1)

    else:
        sys.exit(0)


@cli.command()
@click.option("-f", "--format", type=click.Choice(["todo", "json"]), default="todo")
@click.argument("path", type=click.Path(exists=True))
def run(path: str, *, format: str = "todo"):
    """Assigns all puzzles an ID and then extracts."""
    click.echo(main.run(Path(path), format))
