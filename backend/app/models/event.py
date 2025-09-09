from sqlalchemy import Column, String, DateTime, Text, Boolean, Integer, Date, CHAR, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.database import Base


class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    event_code = Column(String(20), unique=True, nullable=False, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text)
    image_url = Column(String(500))
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    is_deleted = Column(CHAR(1), default='N', nullable=False)
    created_by = Column(Integer, ForeignKey('super_admins.id'))
    created_at = Column(DateTime, server_default=func.current_timestamp())
    updated_at = Column(DateTime, server_default=func.current_timestamp())
    
    # Relationships
    creator = relationship("SuperAdmin")
    managers = relationship("EventManager", back_populates="event", cascade="all, delete-orphan")
    products = relationship("Product", back_populates="event", cascade="all, delete-orphan")
    orders = relationship("Order", back_populates="event")
    notices = relationship("Notice", back_populates="event", cascade="all, delete-orphan")