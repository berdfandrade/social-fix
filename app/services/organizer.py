import uuid
from app.models.user import User
from app.models.organizer import Organizer
from sqlalchemy.orm import Session

class OrganizerService:
    @staticmethod
    def become_organizer(db : Session, user_id : str):
        """Transforma o usuário em um organizador"""

        # Verifica se o usuário existe
        user = db.query(User).filter(User.id == user_id).first()

        if not user:
            raise ValueError("User not found")

        # Verifica se o usuário já é um organizador
        if user.is_organizer:
            raise  ValueError("User already a organizer")

        # Cria o organizador
        organizer = Organizer(
            id=uuid.uuid4(),
            user_id=user_id
        )

        user.is_organizer = True

        db.add(organizer)
        db.commit()
        db.refresh(organizer)

        return organizer
    @staticmethod
    def get_volunteer_by_id(db: Session, volunteer_id: uuid.UUID):
        """Obtém um Organizador pelo ID"""
        return db.query(Organizer).filter(Organizer.id == volunteer_id).first()

    @staticmethod
    def get_volunteer_by_user_id(db: Session, user_id: uuid.UUID):
        """Obtém um organizador pelo ID do usuário."""
        return db.query(Organizer).filter(Organizer.user_id == user_id).first()

    @staticmethod
    def remove_organizer(db : Session, organizer_id : uuid.UUID):
        """Remove um organizador (mas não exclui o usuário)"""
        organizer = db.query(Organizer).filter(Organizer.id == organizer_id).first()
        if not organizer:
            raise ValueError("Organizer not found")

        db.delete(organizer)
        db.commit()

        return {"message" : "Organizer sucessfully removed"}

