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
