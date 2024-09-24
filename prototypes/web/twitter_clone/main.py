import fastapi

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


app = fastapi.FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def healthcheck(request: fastapi.Request):
    return templates.TemplateResponse(
        request=request,
        name="index.jinja",
    )
