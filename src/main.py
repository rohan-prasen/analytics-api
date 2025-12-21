from fastapi import FastAPI
from typing import Union

app = FastAPI(title="Analytics API", version="0.1.0")

@app.get("/")
def read_root():
    return {"Message" : "Hello World!!!"}

@app.get("/items/{item_id}")
def read_items(item_id: int, q: Union[str, None] = None):
    return {"item_id" : item_id, "q": q}