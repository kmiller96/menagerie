import fastapi


app = fastapi.FastAPI()


@app.get("/")
def unprotected():
    return {"message": "Unprotected route"}


@app.get("/protected")
def protected():
    return {"message": "Protected route"}
