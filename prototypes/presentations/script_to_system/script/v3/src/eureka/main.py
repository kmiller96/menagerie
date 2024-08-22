"""Added logging to the script"""

from loguru import logger

from utils.database import Database
from utils.config import URL, DB_PATH

from eureka.contexts import allow_ctrl_c
from eureka.requests import fetch
from eureka.processing import parse

ERROR_MSG = "An error occurred. Skipping."


def main():
    with allow_ctrl_c():
        db = Database(DB_PATH or "./database.db")

        i = 0
        while True:
            i += 1

            logger.info(f"Initiating loop #{i}")

            with logger.catch(onerror=lambda _: logger.error(ERROR_MSG)):
                response = fetch(URL)
                data = parse(response)
                db.insert(data)

            logger.debug(f"Loop #{i} completed")
