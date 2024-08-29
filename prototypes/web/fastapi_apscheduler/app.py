import time
from contextlib import asynccontextmanager

import fastapi

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.executors.pool import ProcessPoolExecutor

MAX_WAIT = 5

###############
## Utilities ##
###############


class DiskBasedCounter:
    def __init__(self, path: str):
        self.path = path
        self.count = 0

    def __str__(self):
        return str(self.count)

    def read(self) -> int:
        try:
            with open(self.path, "r") as f:
                content = f.read()
                self.count = int(content)
        except FileNotFoundError:
            pass

    def increment(self):
        self.count += 1

    def write(self):
        with open(self.path, "w") as f:
            f.write(str(self.count))


##########
## Jobs ##
##########


def job(name: str, wait: float):
    counter = DiskBasedCounter(f"state.{name}")
    counter.read()

    print(f"[{name.upper()} #{counter}] Starting.")
    time.sleep(wait)
    print(f"[{name.upper()} #{counter}] Finished.")

    counter.increment()
    counter.write()


##############
## Lifespan ##
##############


@asynccontextmanager
async def lifespan(app: fastapi.FastAPI):
    scheduler = BackgroundScheduler(
        executors={"default": ProcessPoolExecutor(max_workers=10_000)}
    )

    with open("state.quick", "w") as f:
        f.write("0")

    with open("state.slow", "w") as f:
        f.write("0")

    scheduler.add_job(
        job,
        args=("quick", 0.01),
        trigger="interval",
        seconds=0.1,
        max_instances=1000,
    )
    scheduler.add_job(
        job,
        args=("slow", 1),
        trigger="interval",
        seconds=0.1,
        max_instances=1000,
    )

    scheduler.start()
    yield
    scheduler.shutdown()


#################
## Application ##
#################

app = fastapi.FastAPI(lifespan=lifespan)


@app.get("/")
def healthcheck():
    return {}
