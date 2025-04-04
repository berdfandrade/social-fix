import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from app.models.volunteer import Volunteer
from app.models.organizer import Organizer
from app.config.database import Base


class User(Base):
    
    __tablename__ = "users"

    # User info
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)

    # Person info
    full_name = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    birth_date = Column(DateTime, nullable=True)
    gender = Column(String, nullable=True)

    # Address
    country = Column(String, nullable=True)
    state = Column(String, nullable=True)
    city = Column(String, nullable=True)
    zip_code = Column(String, nullable=True)

    # Personal info
    bio = Column(String, nullable=True)
    skills = Column(String, nullable=True)
    interests = Column(String, nullable=True)
    profile_picture = Column(String, nullable=True)

    # DB info
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    # Relationships
    is_volunteer = Column(Boolean, default=False)
    is_organizer = Column(Boolean, default=False)
    volunteer = relationship("Volunteer", uselist=False, back_populates="user")
    organizer = relationship("Organizer", uselist=False, back_populates="user")
