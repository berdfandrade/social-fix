from pydantic import BaseModel, EmailStr, ConfigDict
from datetime import datetime
import uuid


class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None
    phone: str | None = None
    birth_date: datetime | None = None
    gender: str | None = None

    country: str | None = None
    state: str | None = None
    city: str | None = None
    zip_code: str | None = None

    bio: str | None = None
    skills: str | None = None
    interests: str | None = None
    profile_picture: str | None = None
    is_volunteer: bool | None = None
    is_organizer: bool | None = None


class UserCreate(UserBase):
    password: str


class UserResponse(UserBase):
    id: uuid.UUID
    is_active: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
