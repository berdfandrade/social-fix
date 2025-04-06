import uuid
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.organizer import OrganizerService
from app.schemas.organizer import OrganizerResponse
from app.config.database import Connection

class OrganizerController:
    @staticmethod
    def become_organizer(
            user_id : uuid.UUID, db : Session = Depends(Connection)
    ) -> OrganizerResponse:
        """Transforma o usuário em organizdor"""

        try:
            organizer = OrganizerService.become_organizer(db, user_id)
            return OrganizerResponse.model_validate(organizer)
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))
        except:
            raise HTTPException(status_code=500, detail="Internal Server Error")