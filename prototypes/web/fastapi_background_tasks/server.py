import time

import fastapi

app = fastapi.FastAPI()

############
## Routes ##
############


@app.get("/")
def index() -> str:
    return "Hello World!"


@app.get("/start/{id}")
def start(id: str, background_jobs: fastapi.BackgroundTasks) -> None:
    background_jobs.add_task(long_running_job, id)


##########
## Jobs ##
##########


def long_running_job(id: str) -> None:
    print(f"Start: {id}")
    time.sleep(10)
    print(f"End: {id}")
