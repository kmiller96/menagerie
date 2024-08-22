"""The absolute simplest approach."""

#############
## Imports ##
#############

import requests

from utils import database

#############
## Globals ##
#############

URL = "http://localhost:8000"

############
## Script ##
############

db = database.Database(__file__)

while True:
    response = requests.get(URL, timeout=5)

    data = response.text.split(",")
    db.insert(data)
