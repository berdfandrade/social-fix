import pytest
from fastapi import status
from app.schemas.user import UserCreate
from app.services.user import UserService
from app.services.auth import AuthService
from app.models.user import User
from app.schemas.auth import LoginRequest
from app.security.hashing import hash_password
from tests.mocks.user import USER
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse
from tests.tools.wrapper import it, TestName


@pytest.fixture
def user_data():
    return USER


@TestName("🔓 AuthService")
class TestAuthService:

    @it("Should authenticate the user")
    def test_authenticate_user_success(self, db: Session):
        # Arrange: cria usuário no banco
        UserService.create_user(db, USER)

        # Act: login com email e senha corretos
        login_data = LoginRequest(email=USER.email, password=USER.password)
        response = AuthService.authenticate_user(db, login_data)

        # Assert
        assert hasattr(response, "access_token")
        assert hasattr(response, "token_type")
        assert response.token_type == "bearer"
        assert isinstance(response.access_token, str)
        assert len(response.access_token) > 10

    @it("Should fail to authenticate the user (wrong password)")
    def test_authenticate_the_user(self, db: Session):
        # Arrange : cria usuário no banco
        UserService.create_user(db, USER)

        # Act: login com email e senha corretos
        login_data = LoginRequest(email=USER.email, password="wrong_password")
        response = AuthService.authenticate_user(db, login_data)

        assert isinstance(response, JSONResponse)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
