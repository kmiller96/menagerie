from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/")
def get_sum(n: Annotated[list[int], Query()]):
    return {"result": sum(n)}