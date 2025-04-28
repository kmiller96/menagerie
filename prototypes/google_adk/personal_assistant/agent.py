import json
from functools import wraps
from textwrap import dedent
from google.adk.agents import Agent

#############
## Helpers ##
#############


def load_tasks():
    """Loads the tasks from a JSON file."""
    global tasks
    try:
        with open("tasks.json", "r") as f:
            tasks = json.load(f)
    except FileNotFoundError:
        tasks = {}


def save_tasks():
    """Saves the tasks to a JSON file."""
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=4)


def read(func):
    """Decorator to ensure tasks are loaded before executing a function."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        load_tasks()
        return func(*args, **kwargs)

    return wrapper


def write(func):
    """Decorator to ensure tasks are both loaded and saved after executing a function."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        load_tasks()
        result = func(*args, **kwargs)
        save_tasks()
        return result

    return wrapper


###########
## Tools ##
###########


@read
def list_tasks(incompleted_only: bool = False, completed_only: bool = False):
    """Returns a list of all tasks.

    Args:
        incompleted_only (Optional, bool): If True, only returns incompleted tasks.
        completed_only (Optional, bool): If True, only returns completed tasks.

    Returns:
        list[str]: A list of all tasks.
    """

    if incompleted_only and completed_only:
        raise ValueError("Cannot filter for both completed and incompleted tasks.")
    elif incompleted_only:
        return [task["text"] for task in tasks.values() if not task["completed"]]
    elif completed_only:
        return [task["text"] for task in tasks.values() if task["completed"]]
    else:
        return [task["text"] for task in tasks.values()]


@read
def search_tasks(query: str) -> list[str]:
    """Returns a list of tasks that match the query.

    Args:
        query (str): The query to search for.

    Returns:
        list[str]: A list of tasks that match the query.
    """
    return [
        task["text"] for task in tasks.values() if query.lower() in task["text"].lower()
    ]


@read
def get_task(task_id: str) -> str:
    """Returns a task by its ID.

    Args:
        task_id (str): The ID of the task to return.

    Returns:
        str: The task text.
    """
    if task_id in tasks:
        return tasks[task_id]["text"]
    else:
        raise ValueError(f"Task with ID {task_id} not found.")


@write
def update_task(task_id: str, new_text: str) -> bool:
    """Updates a task's text by its ID.

    Args:
        task_id (str): The ID of the task to update.
        new_text (str): The new text for the task.

    Returns:
        bool: True if the task was updated, False otherwise.
    """
    if task_id in tasks:
        tasks[task_id]["text"] = new_text
        return True
    else:
        return False


@write
def add_task(task: str) -> str:
    """Adds a task to the list of tasks. Initially marks the task as incomplete.

    Args:
        task (str): The task to add.

    Returns:
        str: The task ID that was added.
    """
    task_id = str(len(tasks) + 1)
    tasks[task_id] = {"text": task, "completed": False}
    return task_id


@write
def mark_task_complete(task_id: str) -> bool:
    """Marks a task as completed.

    Args:
        task_id (str): The ID of the task to mark as completed.

    Returns:
        bool: True if the task was marked as completed, False otherwise.
    """
    if task_id in tasks:
        tasks[task_id]["completed"] = True
        return True

    else:
        return False


@write
def mark_task_incomplete(task_id: str) -> bool:
    """Marks a task as incompleted.

    Args:
        task_id (str): The ID of the task to mark as incompleted.

    Returns:
        bool: True if the task was marked as incompleted, False otherwise.
    """
    if task_id in tasks:
        tasks[task_id]["completed"] = False
        return True

    else:
        return False


@write
def remove_task(task_id: str) -> bool:
    """Removes a task from the list of tasks.

    Args:
        task_id (str): The ID of the task to remove.

    Returns:
        bool: True if the task was removed, False otherwise.
    """
    if task_id in tasks:
        del tasks[task_id]
        return True

    else:
        return False


###########
## Agent ##
###########

load_tasks()

root_agent = Agent(
    name="personal_assistant",
    model="gemini-2.0-flash",
    description="Helps you manage your tasks.",
    instruction=dedent(
        """
        You are a personal assistant that helps users manage their tasks.
        
        You can only perform tasks related to the tools you have access to. Do 
        not attempt to perform tasks outside of your capabilities. 
        
        Do not tell the user the task ID or any other internal information. 

        If the user asks for a list of tasks, you should return all of the tasks.
        Only filter the tasks if the user specifically asks for incompleted or
        completed tasks.
        
        If the user wants to update or remove a task, you should search for the 
        task and then confirm with them before updating it. 

        If returning multiple tasks, return them in a checked list format.
        For example:

        - [ ] Task 1
        - [x] Task 2
        - [ ] Task 3
        """
    ),
    tools=[
        list_tasks,
        search_tasks,
        get_task,
        update_task,
        add_task,
        mark_task_complete,
        mark_task_incomplete,
        remove_task,
    ],
)
