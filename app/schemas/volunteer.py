from pydantic import BaseModel, ConfigDict
from app.schemas.user import UserResponse


class VolunteerBase(BaseModel):
    phone: str | None = None


class VolunteerCreate(VolunteerBase):
    pass


class VolunteerResponse(VolunteerBase):
    id: int
    user: "UserResponse"
    model_config = ConfigDict(from_attributes=True)
