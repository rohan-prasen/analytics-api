from fastapi import APIRouter, Depends
from api.db.session import get_session
from sqlmodel import Session
from .models import (
    EventModel, 
    EventListSchema, 
    EventCreateSchema,
    EventUpdateSchema
)
from api.db.config import DATABASE_URL

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
@router.post("/", response_model=EventModel)
def create_events(
        payload:EventCreateSchema, 
        session: Session = Depends(get_session)):
    # a bunch of items in a table
    # print(payload)
    data = payload.model_dump() # payload -> dict -> pydantic
    obj = EventModel.model_validate(data)
    session.add(obj)
    session.commit()
    session.refresh(obj)
    return obj


# GET /api/events/12
@router.get("/{event_id}")
def get_event(event_id:int) -> EventModel:
    # a single row
    return {"id" : event_id}

# Update this data
# PUT /api/events/12
@router.put("/{event_id}")
def update_event(event_id:int, payload:EventUpdateSchema) -> EventModel:
    # # a single row
    # print(payload)
    data = payload.model_dump()
    return {"id" : event_id, **data}



# @router.delete("/{event_id}")
# def get_event(event_id:int) -> EventModel:
#     # a single row
#     return {"id": event_id}