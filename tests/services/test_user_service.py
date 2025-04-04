import pytest
from tests.tools.wrapper import it, TestName
from app.schemas.user import UserCreate
from app.services.user import UserService
from tests.mocks.user import USER
from sqlalchemy.orm import Session


@pytest.fixture
def user_data():
    return USER


@TestName("UserService")
class TestUserService:

    @it("Should return user")
    def test_create_user(self, db: Session, user_data):

        user_data = USER
        new_user = UserService.create_user(db, user_data)

        assert new_user is not None
        assert new_user.username == user_data.username
        assert new_user.email == user_data.email
        assert new_user.full_name == user_data.full_name
        assert new_user.hashed_password != user_data.password

    @it("Should return a user by email")
    def test_get_user_by_email(self, db: Session, user_data):
        created_user = UserService.create_user(db, user_data)
        db.commit()
        db.refresh(created_user)

        response = UserService.get_user_by_email(db, user_data.email)

        assert response is not None
        assert response.email == user_data.email

    @it("Should return user by ID")
    def test_get_user_by_id(self, db: Session, user_data):
        created_user = UserService.create_user(db, user_data)
        db.commit()
        db.refresh(created_user)

        response = UserService.get_user_by_id(db, created_user.id)

        assert response is not None
        assert response.id == created_user.id

    @it("Should return user by username")
    def test_get_user_by_username(self, db: Session, user_data):
        created_user = UserService.create_user(db, user_data)
        db.commit()
        db.refresh(created_user)

        response = UserService.get_user_by_username(db, user_data.username)

        assert response is not None
        assert response.username == user_data.username

    @it("Should delete user")
    def test_delete_user(self, db: Session, user_data):
        created_user = UserService.create_user(db, user_data)
        db.commit()
        db.refresh(created_user)

        deleted = UserService.delete_user(db, created_user.id)

        assert deleted is True
        assert UserService.get_user_by_id(db, created_user.id) is None
