import click

from hub.utils import fuzzy_match
from .manager import GoalsManager

STATE = GoalsManager()


@click.group(invoke_without_command=True)
@click.pass_context
def goals(ctx):
    """Controls your current goals list."""
    if ctx.invoked_subcommand is None:
        ctx.forward(show)


@goals.command()
def undo():
    """Undoes your last action made."""
    STATE.undo()


@goals.command()
def show():
    """Presents your current goals you wish to work on."""
    terminal_string = STATE.draw()
    print(terminal_string)
    return


@goals.command()
@click.argument("goal")
@click.option("-n", "--rank", type=int, help="Set the goal position in the ranking.")
def add(goal, rank):
    """Creates a new goal."""
    if rank is None:
        index = len(STATE)
    else:
        index = rank - 1

    STATE.add(name=goal, index=index)
    return


@goals.command()
@click.argument("goal", type=str, required=False)
@click.option(
    "-n", "--rank", type=int, help="Delete by rank number instead of my task string."
)
def remove(goal, rank):
    """Deletes a goal."""
    if rank is None and goal is None:
        print("You must either provide the goal or a rank number.")
        return

    if rank is None:
        try:
            goals_list = [t["name"] for t in STATE]
            full_goal_string = fuzzy_match(goal, goals_list)
        except LookupError:
            print(
                f"Found multiple goals that start with {goal}.",
                "Please be more specific.",
            )
            return  # Graceful early exit if failed.
        else:
            goal_index = goals_list.index(full_goal_string)
    else:
        goal_index = rank - 1

    STATE.remove(index=goal_index)
    return


@goals.command()
@click.argument("src")
@click.argument("dst")
def move():
    """Changes a goal's rank."""
    raise NotImplementedError()
