import uuid
from sqlalchemy import Column, String, Text, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from datetime import datetime
from app.config.database import Base

class Event(Base):
    
    __tablename__ = "events"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    location = Column(String, nullable=False)
    date = Column(DateTime, nullable=False, default=datetime.now)
    organizer_id = Column(UUID(as_uuid=True), ForeignKey("organizers.id"), nullable=False)

    organizer = relationship("Organizer", back_populates="events")