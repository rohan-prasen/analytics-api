from typing import List, Optional
from pydantic import BaseModel

"""
id
path
description
"""
class EventCreateSchema(BaseModel):
    path: str

class EventUpdateSchema(BaseModel):
    description: str

class EventSchema(BaseModel):
    id: int
    page: Optional[str] = ""



# {"id": 12}


class EventListSchema(BaseModel):
    results: List[EventSchema]
    count: int