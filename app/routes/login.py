from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.auth import LoginRequest, LoginResponse
from app.services.auth import AuthService
from app.config.database import Connection

router = APIRouter(prefix="/auth", tags=["🔒 Auth"])


@router.post("/login", response_model=LoginResponse)
def login(login_data: LoginRequest, db: Session = Depends(Connection)):
    """
    Endpoint para autenticação do usuários. Retorna um token válido
    """
    return AuthService.authenticate_user(db, login_data)
