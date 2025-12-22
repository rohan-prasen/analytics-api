from contextlib import asynccontextmanager
from fastapi import FastAPI

from typing import Union
from api.db.session import init_db
from api.events import router as event_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # before app startup
    init_db()
    yield
    # clean up


app = FastAPI(title="Analytics API", version="0.1.0")
app.include_router(event_router, prefix="/api/events")
# /api/events

@app.get("/")
def read_root():
    return {"Message" : "Hello World!!!"}

@app.get("/items/{item_id}")
def read_items(item_id: int, q: Union[str, None] = None):
    return {"item_id" : item_id, "q": q}


@app.get("/healthz")
def read_api_health():
    return {"status" : "ok"}