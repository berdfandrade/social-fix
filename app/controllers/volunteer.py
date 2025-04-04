import uuid
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.volunteer import VolunteerService
from app.schemas.volunteer import VolunteerCreate, VolunteerResponse
from app.schemas.user import UserBase
from app.config.database import Connection


class VolunterController:

    @staticmethod
    def become_volunteer(
        user_id: uuid.UUID, db: Session = Depends(Connection)
    ) -> VolunteerResponse:
        """Transforma um usuário em voluntário"""

        try:
            volunteer = VolunteerService.become_volunteer(db, user_id)
            return VolunteerResponse.model_validate(volunteer)
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))
        except:
            raise HTTPException(status_code=500, detail="Internal Server Error")
