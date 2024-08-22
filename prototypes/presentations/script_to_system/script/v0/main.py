"""The absolute simplest approach."""

#############
## Imports ##
#############

from pathlib import Path

import requests

from utils.database import Database
from utils.preprocessing import preprocess
from utils.config import URL, DB_PATH

############
## Script ##
############

db = Database(DB_PATH or Path(__file__).parent / "database.db")

while True:
    response = requests.get(URL, timeout=5)

    data = preprocess(response.text)
    db.insert(data)
