from pydantic import EmailStr
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate
from app.security.hashing import hash_password


class UserService:
    @staticmethod
    def get_user_by_id(db: Session, user_id: str):
        """Busca um usuário por ID"""
        return db.query(User).filter(User.id == user_id).first()

    @staticmethod
    def get_user_by_username(db: Session, username: str):
        """Busca um usuário pelo nome de usuário"""
        return db.query(User).filter(User.username == username).first()

    @staticmethod
    def get_user_by_email(db: Session, email: EmailStr):
        """Busca um usuário pelo e-mail"""
        return db.query(User).filter(User.email == email).first()

    @staticmethod
    def create_user(db: Session, user_data: UserCreate):
        """Cria um novo usuário no banco de dados"""

        hashed_pwd = hash_password(user_data.password)

        new_user = User(
            username=user_data.username,
            email=user_data.email,
            full_name=user_data.full_name,
            hashed_password=hashed_pwd,
            phone=user_data.phone,
            birth_date=user_data.birth_date,
            gender=user_data.gender,
            country=user_data.country,
            state=user_data.state,
            city=user_data.city,
            zip_code=user_data.zip_code,
            bio=user_data.bio,
            skills=user_data.skills,
            interests=user_data.interests,
            profile_picture=user_data.profile_picture,
        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return new_user

    @staticmethod
    def delete_user(db: Session, user_id: str):
        """Deleta um usuário pelo ID"""
        user = db.query(User).filter(User.id == user_id).first()
        if user:
            db.delete(user)
            db.commit()
            return True
        return False
