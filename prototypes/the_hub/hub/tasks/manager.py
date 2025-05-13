from hub.utils.state import StatefulList


class TasksManager:
    """Utility class. Manages the state of the tasks list."""

    def __init__(self):
        self.state = StatefulList(name="tasks")

    def __len__(self):
        return len(self.state)
    
    def __iter__(self):
        for item in self.state:
            yield item
    
    def __getitem__(self, index):
        return self.state[index]
    
    def __setitem__(self, index, value):
        self.state[index] = value 
        return
    
    def add(self, name, due_date=None, completed=False, index=None):
        if index is None:
            index = len(self.state)

        item = {
            "name": name,
            "completed": completed,
            "due_date": due_date
        }
        self.state.add(item, index=index)
        return self
    
    def remove(self, index=-1):
        self.state.remove(index=index)
        return self
    
    def undo(self):
        self.state.undo()
        return self

    def draw(self):
        terminal_string = ''

        for i, item in enumerate(self.state):
            task_state = "[X]" if item["completed"] else "[ ]"
            task_name = item["name"]

            terminal_string += f"{task_state}    {task_name}\n"

        return f"\n{terminal_string}"