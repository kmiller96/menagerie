"""Contains a set of data structures which store lists."""

import os

from hub.utils.file import StateStorageDisk 


class StatefulList:
    """List object that serialises to the disk after mutating operations."""

    def __init__(self, name, *items):
        self.name = name
        self.state = StateStorageDisk(self.name)

        if not os.path.exists(self.state.path):
            self.state.write({"items": []})

        for item in items:
            self.add(item)
    
    def __len__(self):
        return len(self.state.load()["items"])
    
    def __iter__(self):
        config = self.state.load()

        for item in config['items']:
            yield item
    
    def __getitem__(self, index):
        config = self.state.load()
        return config["items"][index]
    
    def __setitem__(self, index, value):
        config = self.state.load()
        config["items"][index] = value
    
    def add(self, item, index=0):
        config = self.state.load()

        config["items"].insert(index, item)

        self.state.write(config)
    
    def remove(self, index=-1):
        config = self.state.load()

        del config["items"][index]

        self.state.write(config)
    
    def undo(self):
        self.state.revert()
    