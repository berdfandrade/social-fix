from fastapi import Depends, HTTPException
from pydantic.v1 import EmailStr
from sqlalchemy.orm import Session
from app.services.user import UserService
from app.schemas.user import UserCreate, UserResponse
from app.config.database import Connection


class UserController:
    @staticmethod
    def create_user(
        user: UserCreate, db: Session = Depends(Connection)
    ) -> UserResponse:
        """Cria um novo usuário"""
        if UserService.get_user_by_email(db, user.email):
            raise HTTPException(status_code=400, detail="E-mail already registered")
        new_user = UserService.create_user(db, user)
        return new_user

    @staticmethod
    def get_user(user_id: str, db: Session = Depends(Connection)) -> UserResponse:
        """Busca um usuário pelo ID"""
        user = UserService.get_user_by_id(db, user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    @staticmethod
    def get_user_by_username(
        username: str, db: Session = Depends(Connection)
    ) -> UserResponse:
        """Busca um usuário pelo nome de usuário"""
        user = UserService.get_user_by_username(db, username)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    @staticmethod
    def get_user_by_email(
        email: str, db: Session = Depends(Connection)
    ) -> UserResponse:
        """Busca um usuário pelo e-mail"""
        email = EmailStr(email)
        user = UserService.get_user_by_email(db, email)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    @staticmethod
    def delete_user(user_id: str, db: Session = Depends(Connection)) -> dict:
        """Deleta um usuário pelo ID"""
        deleted = UserService.delete_user(db, user_id)
        if not deleted:
            raise HTTPException(status_code=404, detail="User not found")
        return {"message": "User deleted successfully"}
