from sqlalchemy import Column, String, DateTime, Boolean, ForeignKey, Integer, CHAR
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.database import Base


class EventManager(Base):
    __tablename__ = "event_managers"

    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(Integer, ForeignKey("events.id"), nullable=False)
    username = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False)
    password_hash = Column(String(255), nullable=False)
    full_name = Column(String(100), nullable=False)
    permission_level = Column(Integer, default=2, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    is_deleted = Column(CHAR(1), default='N', nullable=False)
    created_by = Column(Integer, ForeignKey('super_admins.id'))
    created_at = Column(DateTime, server_default=func.current_timestamp())
    updated_at = Column(DateTime, server_default=func.current_timestamp())
    
    # Relationships
    event = relationship("Event", back_populates="managers")
    creator = relationship("SuperAdmin")