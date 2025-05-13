"""Enables the user to customise their H.U.B. using a JSON configuration file."""

import os

from hub import defines
from hub.utils.file import JSONConfigurationFile


class Configuration:

    def __init__(self):
        self._config = JSONConfigurationFile(fname="configuration.json")
        if not os.path.exists(self._config.path):
            self._config.write({})

    def __getitem__(self, key):
        config = self._config.load()
        return config[key]

    def __setitem__(self, key, value):
        config = self._config.load()
        config[key] = value
        self._config.write(config)
        return