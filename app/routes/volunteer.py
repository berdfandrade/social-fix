from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.controllers.volunteer import VolunterController
from app.schemas.user import UserBase
from app.schemas.volunteer import VolunteerCreate, VolunteerResponse
from app.config.database import Connection

router = APIRouter(prefix="/volunteers", tags=["🙋 Volunteers"])


@router.post("/volunteer/{user_id}", response_model=VolunteerResponse)
def become_volunteer(user: UserBase, db: Session = Depends(Connection)):
    return VolunterController.become_volunteer(user, db)

@router.post("/volunteer/remove_user", response_model=VolunteerResponse)
def remove_user_as_volunteer():
    pass