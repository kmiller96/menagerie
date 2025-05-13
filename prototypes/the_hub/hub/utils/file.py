import json
import os
import shutil

from hub import defines


class StateStorageDisk:
    """Persists state to the disk."""

    def __init__(self, name):
        self._config = JSONConfigurationFile(fname=f"{name}.json", path_prefix="state")
        self._backup = JSONConfigurationFile(fname=f"{name}.backup.json", path_prefix="state")

        self.name = name
        self.path = self._config.path
        return
    
    def checkpoint(self):
        """Copies the current configuration state to a backup copy."""
        try:
            shutil.copyfile(self._config.path, self._backup.path)
        except FileNotFoundError:
            pass  # Nothing to checkpoint. Skip.
        return self

    def load(self):
        """Loads the state into a Python data structure."""
        return self._config.load()
    
    def revert(self):
        """Rolls back to a previous copy of the configuration file."""
        tmp = self._config.path.replace(".json", ".tmp.json")

        shutil.copyfile(self._config.path, tmp)                # Main -> Tempfile
        shutil.copyfile(self._backup.path, self._config.path)  # Backup -> Main
        shutil.copyfile(tmp, self._backup.path)                # Tempfile -> Backup

        os.remove(tmp)
        
        return self

    def write(self, configuration, checkpoint=True):
        """Writes the state down to persistent storage."""
        if checkpoint: 
            self.checkpoint()

        return self._config.write(configuration)


class JSONConfigurationFile:
    """Manages the file I/O for the configuration files expressed in JSON."""

    def __init__(self, fname, path_prefix=""):
        self.fpath = os.path.join(defines.USER_HUB_PATH, path_prefix, fname)

    @property
    def path(self):
        return self.fpath

    def load(self):
        with open(self.fpath, "r") as f:
            return json.load(f)

    def write(self, config):
        prefix, _ = os.path.split(self.fpath)
        os.makedirs(prefix, exist_ok=True)

        with open(self.fpath, "w") as f:
            json.dump(config, f, indent=2)
