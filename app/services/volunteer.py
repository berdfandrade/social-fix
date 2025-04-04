import uuid
from uuid import UUID
from sqlalchemy.orm import Session
from app.models.user import User
from app.models.volunteer import Volunteer
from app.schemas.user import UserCreate
from app.schemas.volunteer import VolunteerCreate
from app.security.hashing import hash_password


class VolunteerService:

    @staticmethod
    def become_volunteer(
        db: Session, user_id: UUID, volunteer, volunteer_data: VolunteerCreate
    ):
        """Transforma o usuário em vonluntário"""

        # Verifica se o usuário existe
        user = db.query(User).filter(User.id == user_id).first()

        if not user:
            raise ValueError("User not found")

        # Verfica se o usuário já é um voluntário
        if user.is_volunteer:
            raise ValueError("User already a volunteer")

        # Cria o voluntário
        volunteer = Volunteer(
            id=uuid.uuid4(),
            user_id=user_id,
            phone=volunteer_data.phone,
        )

        user.is_volunteer = True

        db.add(volunteer)
        db.commit()
        db.refresh(volunteer)

        return volunteer

    @staticmethod
    def get_volunteer_by_id(db: Session, volunteer_id: uuid.UUID):
        """Obtém um voluntário pelo ID"""
        return db.query(Volunteer).filter(Volunteer.id == volunteer_id).first()

    @staticmethod
    def get_volunteer_by_user_id(db: Session, user_id: uuid.UUID):
        """Obtém um voluntário pelo ID do usuário."""
        return db.query(Volunteer).filter(Volunteer.user_id == user_id).first()

    @staticmethod
    def remove_volunteer(db: Session, volunteer_id: uuid.UUID):
        """Remove um voluntário (mas não exclui o usuário)."""
        volunteer = db.query(Volunteer).filter(Volunteer.id == volunteer_id).first()
        if not volunteer:
            raise ValueError("Volunteer not found")

        db.delete(volunteer)
        db.commit()

        return {"message": "Volunteer successfully removed"}
