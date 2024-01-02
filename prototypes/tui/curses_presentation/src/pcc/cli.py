"""Defines the CLI for the package."""

import curses

import typer

import pcc.demos.hello_world
import pcc.demos.counter
import pcc.demos.maze
import pcc.demos.typist
import pcc.demos.screensaver


cli = typer.Typer()


@cli.command()
def hello():
    """Runs the hello world script."""
    curses.wrapper(pcc.demos.hello_world.main)


@cli.command()
def counter():
    """Run the counter prototype."""
    curses.wrapper(pcc.demos.counter.main)


@cli.command()
def screensaver():
    """Run the typist game."""
    curses.wrapper(pcc.demos.screensaver.main)


@cli.command()
def maze():
    """Run the maze game."""
    game = pcc.demos.maze.GameLoop()
    curses.wrapper(game.run)


@cli.command()
def typist():
    """Run the typist game."""
    curses.wrapper(pcc.demos.typist.main)
