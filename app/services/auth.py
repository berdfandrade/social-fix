import os
from jose import jwt, JWTError
from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta, timezone
from sqlalchemy.orm import Session
from app.models.user import User
from app.security.hashing import verify_password
from app.schemas.auth import LoginRequest, LoginResponse


class AuthService:
    AUTH_SCHEME = OAuth2PasswordBearer(tokenUrl="token")
    SECRET_KEY = os.getenv("JWT_SECRET", "defaultsecret")
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30

    @staticmethod
    def authenticate_user(db: Session, login_data: LoginRequest):
        """Autentica um usuário com email e senha, retornando um token JWT"""
        user = db.query(User).filter(User.email == login_data.email).first()

        if not user or not verify_password(login_data.password, user.hashed_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )

        # Gera token JWT
        access_token = AuthService.create_access_token(data={"sub": str(user.id)})
        return LoginResponse(access_token=access_token, token_type="bearer")

    @staticmethod
    def decode_user(token: str = Depends(AUTH_SCHEME)):
        """Verifica e retorna o usuário autenticado a partir do token"""
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"},
        )

        payload = AuthService.decode_token(token)
        if not payload:
            raise credentials_exception

        return payload

    @staticmethod
    def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
        """Gera um token JWT"""
        to_encode = data.copy()
        expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=15))
        to_encode.update({"exp": expire})

        encoded_jwt = jwt.encode(
            to_encode, AuthService.SECRET_KEY, algorithm=AuthService.ALGORITHM
        )
        print(encoded_jwt)
        return encoded_jwt

    @staticmethod
    def decode_token(token: str):
        """Decodifica um token JWT"""
        try:
            return jwt.decode(
                token, AuthService.SECRET_KEY, algorithms=[AuthService.ALGORITHM]
            )
        except JWTError:
            return None
