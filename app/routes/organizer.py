import uuid
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.controllers.organizer import OrganizerController
from app.schemas.organizer import OrganizerResponse
from app.config.database import Connection

router = APIRouter(prefix="/organizers", tags=["🧠 Organizers"])

@router.post("/organizer", response_model=OrganizerResponse)
def become_organizer(user_id : uuid.UUID, db : Session = Depends(Connection)):
    return OrganizerController.become_organizer(user_id, db)