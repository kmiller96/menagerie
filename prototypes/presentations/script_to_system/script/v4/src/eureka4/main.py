"""Added logging to the script"""

import multiprocessing

import uvicorn
from loguru import logger

from utils.database import Database
from utils.config import URL, DB_PATH

from eureka4.requests import fetch
from eureka4.processing import parse

ERROR_MSG = "An error occurred. Skipping."


def main(db_path: str):
    db = Database(db_path)

    i = 0
    while True:
        i += 1

        logger.info(f"Initiating loop #{i}")

        with logger.catch(onerror=lambda _: logger.error(ERROR_MSG)):
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
