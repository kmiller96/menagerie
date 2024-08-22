"""Added logging to the script"""

#############
## Imports ##
#############

import requests
from loguru import logger

from utils.database import Database
from utils.preprocessing import preprocess
from utils.config import URL

############
## Script ##
############

db = Database(__file__)

i = 0
while True:
    i += 1
    logger.info(f"Initiating loop #{i}")

    response = requests.get(URL, timeout=5)

    content = response.text
    logger.debug(f"Content: {content}")

    data = preprocess(content)
    logger.debug(f"Data: {data}")

    db.insert(data)

    logger.debug(f"Loop #{i} completed")
