import time
from collections import deque
from contextlib import contextmanager

from utils.database import Database


class ServerStatistics:
    __state = {}

    db: Database

    def __init__(self):
        self.__dict__ = self.__state

        self._times = deque(maxlen=10)

    def register_db(self, db: Database):
        self.db = db

    @contextmanager
    def timeit(self):
        """Times the execution of a job."""
        start = time.time()
        yield
        end = time.time()

        self._times.append(end - start)

    def average_processing_time(self) -> float:
        """Returns the average processing time of the last 10 jobs."""
        return sum(self._times) / len(self._times)

    def rows(self) -> int:
        """Returns the number of rows in the database currently."""
        return self.db.count()
