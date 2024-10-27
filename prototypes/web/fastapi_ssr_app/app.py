import fastapi
from fastapi.responses import HTMLResponse

app = fastapi.FastAPI()


@app.get("/")
def index():
    return HTMLResponse(content="<h1>Hello, World!</h1>", status_code=200)
