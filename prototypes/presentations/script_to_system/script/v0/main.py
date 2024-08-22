"""The absolute simplest approach."""

#############
## Imports ##
#############

import requests

from utils.database import Database
from utils.preprocessing import preprocess
from utils.config import URL

############
## Script ##
############

db = Database(__file__)

while True:
    response = requests.get(URL, timeout=5)

    data = preprocess(response.text)
    db.insert(data)
