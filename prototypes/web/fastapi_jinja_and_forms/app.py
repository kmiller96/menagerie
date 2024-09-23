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


@app.get("/{id}")
def get_id_page(request: fastapi.Request, id: int):
    return templates.TemplateResponse(
        request=request,
        name="page.jinja",
        context={
            "id": id,
            # "emotion": "sad",
        },
    )
