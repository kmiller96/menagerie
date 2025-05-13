import os

import click

from .manager import ProjectsManager 


STATE = ProjectsManager()


@click.group(invoke_without_command=True)
@click.pass_context
def projects(ctx):
    """Manages metadata about projects."""
    if ctx.invoked_subcommand is None:
        ctx.forward(show)


@projects.command()
def undo():
    """Undoes your last action made."""
    STATE.undo()
    return


@projects.command()
@click.option("--name", help="Project name. Defaults to root directory name.")
def init(name):
    """Initialises information about a project."""
    path = os.getcwd()
    if name is None:
        _, name = os.path.split(path)

    if name in STATE:
        print("This directory is already a project. Updating the metadata.")

    STATE.add(name, path)
    return


@projects.command()
def show():
    """Lists the currently tracked projects."""
    print(STATE.draw())
    return


@projects.command()
@click.argument("name")
def remove(name):
    STATE.remove(name)
    return


@projects.command(name="get-path")
@click.argument("name")
def get_path(name):
    """Returns the local path to the project directory."""
    print(STATE[name]["path"])
    return
