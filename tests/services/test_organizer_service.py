import pytest
from fastapi import status
from app.services.organizer import OrganizerService
from app.services.auth import AuthService
from app.schemas.auth import LoginRequest
from app.services.user import UserService
from app.services.volunteer import VolunteerService
from tests.mocks.user import USER
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse
from tests.tools.wrapper import it, TestName

@pytest.fixture()
def user_data():
    return USER

@TestName("OrganizerService")
class OrganizerService:

    @it("User should become organizer")
    def test_become_organizer_sucess(self, db : Session, user_data):

        user = UserService.create_user(db, user_data)
        VolunteerService.become_volunteer(db, user.id)

        assert user.is_organizer == True