from hub.utils.state import StatefulDictionary 


class ProjectsManager:
    """Utility class. Manages the state of the tasks list."""

    def __init__(self):
        self.state = StatefulDictionary(name="projects")
    
    def __iter__(self):
        for key, item in self.state:
            yield key, item
    
    def __contains__(self, value):
        return value in self.state
    
    def __getitem__(self, key):
        return self.state[key]
    
    def __setitem__(self, key, value):
        self.state[key] = value 
        return
    
    def add(self, name, path):
        definition = {
            "name": name,
            "path": path,
        }
        self.state.add(name, definition)
        return self
    
    def remove(self, name):
        self.state.remove(key=name)
        return self
    
    def undo(self):
        self.state.undo()
        return self

    def draw(self):
        terminal_string = ''

        for key, item in self.state:
            terminal_string += f"{key}\n"

        return f"\n{terminal_string}"