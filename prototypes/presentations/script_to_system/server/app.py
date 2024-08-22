import asyncio
import random

import fastapi
from fastapi.responses import PlainTextResponse

PRECISION = 1000
SLEEP_RANGE = (0, 4)

TIMEOUT_SLEEP = 60
TIMEOUT_RATE = 20

DATA_MISFORMAT_RATE = 20

####################
## Data Generator ##
####################


def sample_coordinate() -> tuple[int, int]:
    """Returns a random coordinate."""
    return random.randint(0, PRECISION), random.randint(0, PRECISION)


def is_in_circle(x: int, y: int) -> bool:
    """Returns whether the coordinate is inside the circle."""
    return x**2 + y**2 <= PRECISION**2


############
## Server ##
############

app = fastapi.FastAPI()
app.state.counter = 0


@app.get("/", response_class=PlainTextResponse)
async def data(debug: bool = False):
    """Returns a random data point.

    This server simulates a very slow data source, such as querying data from
    across the galaxy. We do this by sleeping for a random amount of time
    defined by SLEEP_RANGE.

    We also want to simulate a random "drop out" rate, where the server fails
    to respond. We do this forcing a client timeout by taking a long time to
    respond every TIMEOUT_RATE requests.
    """
    # -- Increment counter -- #
    app.state.counter += 1

    # -- Determine wait time -- #
    if debug:
        pass  # In debug mode, don't wait
    elif app.state.counter % TIMEOUT_RATE == 0:
        await asyncio.sleep(TIMEOUT_SLEEP)  # Simulate a timeout
    else:
        lower, upper = SLEEP_RANGE
        await asyncio.sleep(random.random() * (upper - lower) + lower)

    # -- Determine if data is misformatted -- #
    if app.state.counter % DATA_MISFORMAT_RATE == 0:
        return "⤽⟗⼭✠⎥⯜⃩◲♺⢠┣ⶇ⯉⃭◴⹆╍◨⏿⺥⳷⨰⮛⫍⿔ⴾ⃋☢⺛⻜⃭℞⼅␌◊⯯⭥✂⒔⏘ⷾ⃇⌐♽⩮⼚⁚⿸⮒"

    # -- Generate data -- #
    x, y = sample_coordinate()
    return f"{x},{y},{int(is_in_circle(x, y))}"
