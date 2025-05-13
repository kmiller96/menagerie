from hub.utils import fuzzy_match


def fuzzy_search(task_string, task_state_dictionary):
    """Tries to find the task via a fuzzy lookup."""
    try:
        tasks_list = [t["name"] for t in task_state_dictionary["tasks"]]
        full_task_string = fuzzy_match(task_string, tasks_list)
    except LookupError:
        return None 
    else:
        return tasks_list.index(full_task_string)