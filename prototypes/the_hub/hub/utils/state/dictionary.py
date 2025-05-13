"""Contains data structures for storing dictionaries as JSON configuration files."""

import os

from hub.utils.file import StateStorageDisk 


class StatefulDictionary:
    """Dictionary object that serialises to the disk after mutating operations."""

    def __init__(self, name, **objects):
        self.name = name
        self.state = StateStorageDisk(self.name)

        if not os.path.exists(self.state.path):
            self.state.write({"items": {}})

        for key, item in objects.items():
            self.add(key, item)
    
    def __iter__(self):
        config = self.state.load()

        for k, v in config['items'].items():
            yield k, v
    
    def __contains__(self, value):
        config = self.state.load()
        return value in config["items"]
    
    def __getitem__(self, key):
        config = self.state.load()
        return config["items"][key]
    
    def __setitem__(self, key, value):
        self.add(key, value)
    
    def add(self, key, item):
        config = self.state.load()

        config["items"][key] = item 

        self.state.write(config)
    
    def remove(self, key):
        config = self.state.load()

        del config["items"][key]

        self.state.write(config)
    
    def undo(self):
        self.state.revert()
    