import click

from hub.utils import fuzzy_match
from .manager import TasksManager 

STATE = TasksManager()


@click.group(invoke_without_command=True)
@click.pass_context
def tasks(ctx):
    """Controls your current task list."""
    if ctx.invoked_subcommand is None:
        ctx.forward(show)


@tasks.command()
def undo():
    """Undoes your last action made."""
    STATE.undo()


@tasks.command()
def show():
    """Lists your current tasks."""
    terminal_string = STATE.draw()
    print(terminal_string)


@tasks.command()
@click.argument("task")
@click.option("-n", "--rank", type=int, help="Set the task position in the ranking.")
def add(task, rank):
    """Creates a new task."""
    if rank is None:
        index = len(STATE)
    else:
        index = rank - 1
    STATE.add(name=task, index=index)
    return


@tasks.command()
@click.argument("task", type=str, required=False)
@click.option("-n", "--rank", type=int, help="Update the task by rank number instead.")
@click.option("--complete", is_flag=True)
@click.option("--in-progress", is_flag=True)
def update(task, rank, complete, in_progress):
    """Update a task's state."""
    if rank is None and task is None:
        print("You must either provide the task string or a rank number.")
        return

    if rank is not None:
        task_index = rank - 1
    else:
        try:
            tasks_list = [t["name"] for t in STATE]
            full_task_string = fuzzy_match(task, tasks_list)
        except LookupError:
            print(
                f"Found multiple tasks that start with {task}.",
                "Please be more specific.",
            )
            return
        else:
            task_index = tasks_list.index(full_task_string)
    
    if complete and in_progress:
        print(
            'You can\'t have both the "--complete" and "--in-progress" flags at the same time.'
        )
    elif complete:
        STATE[task_index].update({"completed": True})
    elif in_progress:
        STATE[task_index].update({"completed": False})

    return


@tasks.command()
@click.argument("task", type=str, required=False)
@click.option(
    "-n", "--rank", type=int, help="Delete by rank number instead of my task string."
)
def remove(task, rank):
    """Deletes a task from the list."""
    if rank is None and task is None:
        print("You must either provide the task string or a rank number.")
        return

    if rank is not None:
        task_index = rank - 1
    else:
        try:
            tasks_list = [t["name"] for t in STATE]
            full_task_string = fuzzy_match(task, tasks_list)
        except LookupError:
            print(
                f"Found multiple tasks that start with {task}.",
                "Please be more specific.",
            )
            return
        else:
            task_index = tasks_list.index(full_task_string)

    STATE.remove(task_index)
    return


@tasks.command()
@click.option("--completed", is_flag=True)
def clean(completed):
    """Utility to remove multiple items at once."""
    if completed:
        remove_indices = [i for i, item in enumerate(STATE) if not item["completed"]]
    
        for index in sorted(remove_indices, reverse=True):
            STATE.remove(index=index)

    return
