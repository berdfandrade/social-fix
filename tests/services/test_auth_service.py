from app.schemas.user import UserCreate
from app.services.user import UserService
from tests.mocks.user import USER
from sqlalchemy.orm import Session


def test_login_user(db: Session):
    pass
