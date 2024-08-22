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

    # -- Log -- #
    logger.info(f"Initiating loop #{i}")

    # -- Fetch -- #
    try:
        response = requests.get(URL, timeout=5)
        response.raise_for_status()

    except requests.Timeout:
        logger.error("Request timed out. Retrying.")
        continue

    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP error occurred: {e}. Retrying.")
        continue

    # -- Process -- #
    content = response.text
    logger.debug(f"Content: {content}")

    try:
        data = preprocess(content)
        logger.debug(f"Data: {data}")
    except ValueError:
        logger.error("Data misformatted. Skipping.")
        continue

    # -- Insert -- #
    db.insert(data)

    # -- Log & Continue -- #
    logger.debug(f"Loop #{i} completed")
