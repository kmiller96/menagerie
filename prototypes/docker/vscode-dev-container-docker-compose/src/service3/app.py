import functools
from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/")
def get_product(n: Annotated[list[int], Query()]):
    return {"result": functools.reduce(lambda x, y: x * y, n)}