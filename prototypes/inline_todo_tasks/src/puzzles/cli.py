"""Defines the CLI of the application."""

from pathlib import Path

import click

OUTPATH = Path("PUZZLES.md")


@click.group()
def cli():
    pass


@cli.command()
@click.argument("path", type=click.Path(exists=True))
def run(path: Path):
    click.echo(path)
    OUTPATH.touch()
