"""Added logging to the script"""

#############
## Imports ##
#############

import requests
from loguru import logger

from utils import database

#############
## Globals ##
#############

URL = "http://localhost:8000"

############
## Script ##
############

db = database.Database(__file__)

i = 0
while True:
    i += 1
    logger.info(f"Initiating loop #{i}")

    response = requests.get(URL, timeout=5)

    if not response.ok:
        logger.error(f"Failed to fetch data: {response.status_code}")
        continue

    content = response.text
    logger.debug(f"Content: {content}")

    data = response.text.split(",")
    logger.debug(f"Data: {data}")

    db.insert(data)

    logger.debug(f"Loop #{i} completed")
