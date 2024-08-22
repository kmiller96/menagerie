"""Added logging to the script"""

import multiprocessing

import uvicorn
from loguru import logger

from utils.database import Database
from utils.config import URL, DB_PATH, ENABLE_PUSH_NOTIFICATIONS

from eureka4.requests import fetch
from eureka4.processing import parse
from eureka4.notifications import notify


def _error_handler(exception: Exception):
    """Error handler for the main loop"""
    msg = f"Exception raised: {exception}."

    logger.error(msg + " Skipping.")

    if ENABLE_PUSH_NOTIFICATIONS:
        notify(message=msg)


def main(db_path: str):
    db = Database(db_path)

    i = 0
    while True:
        i += 1

        logger.info(f"Initiating loop #{i}")

        with logger.catch(onerror=_error_handler):
            response = fetch(URL)
            data = parse(response)
            db.insert(data)

        logger.debug(f"Loop #{i} completed")


def start_main_process() -> multiprocessing.Process:
    process = multiprocessing.Process(
        target=main,
        name="main",
        args=(DB_PATH or "./database.db",),
    )
    process.start()
    return process


def start_main_server():
    uvicorn.run("eureka4.server:app", port=8080)
