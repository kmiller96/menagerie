from typing import Annotated

import fastapi
from pydantic import BaseModel


app = fastapi.FastAPI()

############
## Models ##
############


class AddRequest(BaseModel):
    a: int
    b: int


############
## Routes ##
############


@app.post("/with/add")
def pydantic_add(request: AddRequest):
    return {"result": request.a + request.b}


@app.post("/without/add")
def no_pydantic_add(
    a: Annotated[int, fastapi.Body()],
    b: Annotated[int, fastapi.Body()],
):
    return {"result": a + b}
