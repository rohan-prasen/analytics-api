from fastapi import APIRouter
from .schemas import EventSchema, EventListSchema

router = APIRouter()

# List view
# get data
# GET /api/events/
@router.get("/")
def read_events() -> EventListSchema:
    # a bunch of items in a table
    return {
        "results" : [
            {"id": 1}, 
            {"id": 2}, 
            {"id": 3}
            ],
            "count": 3
    }

# Send data here
# create view
# POST /api/events/
@router.post("/")
def create_events(data:dict = {}) -> EventSchema:
    print(data)
    # a bunch of items in a table
    return {"id" : 123}

# GET /api/events/12
@router.get("/{event_id}")
def get_event(event_id:int) -> EventSchema:
    # a single row
    return {"id" : event_id}