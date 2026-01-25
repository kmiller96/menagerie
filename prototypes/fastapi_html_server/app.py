from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        "page.jinja",
        {
            "request": request,
            "title": "Home Page",
        },
    )


@app.get("/subpage/{id}")
async def subpage(request: Request, id: int):
    return templates.TemplateResponse(
        "subpage/page.jinja",
        {
            "request": request,
            "title": f"Subpage {id}",
            "id": id,
        },
    )
