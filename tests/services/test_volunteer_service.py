import pytest
from sqlalchemy.orm import Session
from tests.tools.wrapper import it, TestName
from app.services.user import UserService
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
