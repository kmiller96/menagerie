from fastapi import FastAPI, Depends, Request

from src.db import Database, get_db

app = FastAPI()


@app.get("/")
def root(request: Request, db: Database = Depends(get_db)):
    db.authenticate(request)

    return {"Hello": "World"}
