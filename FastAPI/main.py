from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/hello")
def hello(name:str):
    return {"Hello": name}

@app.get("/test")
def test(request:str, reply:str):
    return {"Request": request, "Reply": reply}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

