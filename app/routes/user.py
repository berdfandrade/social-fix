from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.controllers.user import UserController
from app.schemas.user import UserCreate, UserResponse
from app.config.database import Connection

router = APIRouter(prefix="/users", tags=["👤 Users"])


@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(Connection)):
    return UserController.create_user(user, db)


@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: str, db: Session = Depends(Connection)):
    return UserController.get_user(user_id, db)


@router.get("/username/{username}", response_model=UserResponse)
def get_user_by_username(username: str, db: Session = Depends(Connection)):
    return UserController.get_user_by_username(username, db)


@router.get("/email/{email}", response_model=UserResponse)
def get_user_by_email(email: str, db: Session = Depends(Connection)):
    return UserController.get_user_by_email(email, db)


@router.delete("/{user_id}")
def delete_user(user_id: str, db: Session = Depends(Connection)):
    return UserController.delete_user(user_id, db)
