from pydantic import BaseModel, ConfigDict
from datetime import datetime
from uuid import UUID


class EventBase(BaseModel):
    title: str
    description: str
    location: str
    date: datetime


class EventCreate(EventBase):
    organizer_id: UUID


class EventResponse(EventBase):
    id: UUID
    organizer_id: UUID

    model_config = ConfigDict(from_attributes=True)
