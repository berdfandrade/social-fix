import uuid
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.config.database import Base

class Volunteer(Base):
    
    __tablename__ = "volunteers"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4) 
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False) 
    phone = Column(String, nullable=True)
    
    user = relationship("User", back_populates="volunteer")
