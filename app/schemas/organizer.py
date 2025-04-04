from pydantic import BaseModel, ConfigDict
from app.schemas.user import UserResponse


class OrganizerBase(BaseModel):
    phone: str | None = None


class OrganizerCreate(OrganizerBase):
    pass


class OrganizerResponse(OrganizerBase):
    id: int
    user: "UserResponse"
    model_config = ConfigDict(from_attributes=True)
