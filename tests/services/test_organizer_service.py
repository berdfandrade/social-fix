import pytest
from app.services.organizer import OrganizerService
from app.services.user import UserService
from tests.mocks.user import USER
from sqlalchemy.orm import Session
from tests.tools.wrapper import it, TestName

@pytest.fixture()
def user_data():
    return USER

@TestName("🧠 OrganizerService")
class TestOrganizerService:

    @it("User should become organizer")
    def test_become_organizer_sucess(self, db : Session, user_data):

        user = UserService.create_user(db, user_data)
        OrganizerService.become_organizer(db, user.id)

        assert user.is_organizer == True