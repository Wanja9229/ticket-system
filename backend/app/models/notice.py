from sqlalchemy import Column, String, DateTime, Text, Boolean, ForeignKey, Integer
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
import uuid

from app.database import Base


class Notice(Base):
    __tablename__ = "notices"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    event_id = Column(String, ForeignKey("events.id"), nullable=False)
    title = Column(String(200), nullable=False)
    content = Column(Text, nullable=False)
    is_important = Column(Boolean, default=False, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    view_count = Column(Integer, default=0)
    created_by = Column(String, nullable=False)  # manager_id or admin_id
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    event = relationship("Event", back_populates="notices")
    attachments = relationship("NoticeAttachment", back_populates="notice", cascade="all, delete-orphan")


class NoticeAttachment(Base):
    __tablename__ = "notice_attachments"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    notice_id = Column(String, ForeignKey("notices.id"), nullable=False)
    filename = Column(String(255), nullable=False)
    file_path = Column(String(500), nullable=False)
    file_size = Column(Integer, nullable=False)
    mime_type = Column(String(100))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    notice = relationship("Notice", back_populates="attachments")
