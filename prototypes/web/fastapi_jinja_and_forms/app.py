from typing import Annotated

import fastapi
from fastapi.templating import Jinja2Templates


app = fastapi.FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/")
def index(request: fastapi.Request):
    return templates.TemplateResponse(
        request=request,
        name="index.jinja",
    )


@app.get("/page/{id}")
def get_id_page(request: fastapi.Request, id: int):
    return templates.TemplateResponse(
        request=request,
        name="page.jinja",
        context={
            "id": id,
            # "emotion": "sad",
        },
    )


@app.get("/form")
def get_form(request: fastapi.Request):
    return templates.TemplateResponse(
        request=request,
        name="form.jinja",
    )


@app.post("/form")
async def post_form(
    request: fastapi.Request,
    username: Annotated[str, fastapi.Form()],
    password: Annotated[str, fastapi.Form()],
):
    return templates.TemplateResponse(
        request=request,
        name="form.submitted.jinja",
        context={
            "username": username,
            "password": password,
        },
    )
