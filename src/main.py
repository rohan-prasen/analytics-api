from fastapi import FastAPI
from typing import Union
from api.events import router as event_router

app = FastAPI(title="Analytics API", version="0.1.0")
app.include_router(event_router, prefix="/api/events")

@app.get("/")
def read_root():
    return {"Message" : "Hello World!!!"}

@app.get("/items/{item_id}")
def read_items(item_id: int, q: Union[str, None] = None):
    return {"item_id" : item_id, "q": q}


@app.get("/healthz")
def read_api_health():
    return {"status" : "ok"}