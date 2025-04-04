import pytest
from sqlalchemy.orm import Session
from app.models.user import User
from tests.tools.wrapper import it, TestName
from app.models.volunteer import Volunteer
from app.services.user import UserService
from app.schemas.volunteer import VolunteerCreate
from app.security.hashing import hash_password
from app.services.volunteer import VolunteerService
from tests.mocks.user import USER


@pytest.fixture
def user_data():
    return USER


@TestName("🙋‍♂️ VolunteerService")
class TestVolunteerService:

    @it("User should become volunteer")
    def test_become_volunteer_sucess(self, db: Session, user_data):
        
        user = UserService.create_user(db, user_data)
        VolunteerService.become_volunteer(db, user.id)

        assert user.is_volunteer == True
