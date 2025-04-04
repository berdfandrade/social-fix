import uuid
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.models.event import Event
from app.config.database import Base

class Organizer(Base):
    
    __tablename__ = "organizers"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4) 
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    phone = Column(String, nullable=True)
    
    events = relationship("Event", back_populates="organizer", cascade="all, delete-orphan")
    user = relationship("User", back_populates="organizer")
