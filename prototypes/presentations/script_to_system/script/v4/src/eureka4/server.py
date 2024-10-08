"""Defines the FastAPI server."""

from contextlib import asynccontextmanager

import fastapi

from eureka4.enums import EurekaStatus
from eureka4.main import start_main_process


@asynccontextmanager
async def lifespan(app: fastapi.FastAPI):
    """Defines the lifespan of the server."""
    app.state.process = start_main_process()
    yield


app = fastapi.FastAPI(lifespan=lifespan)
app.state.status = EurekaStatus.ACTIVE


@app.get("/")
def healthcheck():
    """Asserts that the server is working as expected.

    This can be used as a basic health check.
    """
    return {
        "status": app.state.status.value,
    }


@app.get("/stats")
def stats():
    """Returns the server's statistics."""
    return {
        "rows": 0,  # TODO
        "average_processing_time": 0,  # TODO
    }


@app.post("/start")
def start():
    """Starts the main loop."""
    if not app.state.process.is_alive():
        app.state.process = start_main_process()

    app.state.status = EurekaStatus.ACTIVE

    return {
        "status": app.state.status.value,
    }


@app.post("/stop")
def stop():
    """Stops the main loop."""
    app.state.process.terminate()
    app.state.status = EurekaStatus.STOPPED

    return {
        "status": app.state.status.value,
    }
