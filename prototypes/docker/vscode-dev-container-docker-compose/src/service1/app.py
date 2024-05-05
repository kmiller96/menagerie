import requests
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return "ok"

@app.get("/sum")
def get_sum():
    response: requests.Response = requests.get("http://service2?n=1&n=2&n=3&n=4")
    return {"result": response.json()["result"]}

@app.get("/product")
def get_product():
    response: requests.Response = requests.get("http://service3?n=1&n=2&n=3&n=4")
    return {"result": response.json()["result"]}
