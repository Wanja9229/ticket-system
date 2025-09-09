from sqlalchemy import Column, String, DateTime, Text, ForeignKey, Integer
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.database import Base


class EntranceLog(Base):
    __tablename__ = "entrance_logs"

    id = Column(Integer, primary_key=True, index=True)
    qr_ticket_id = Column(Integer, ForeignKey("qr_tickets.id"), nullable=False)
    processed_by = Column(Integer, nullable=False)
    entrance_type = Column(String(20), default='normal', nullable=False)
    device_info = Column(Text)
    processed_at = Column(DateTime, server_default=func.current_timestamp())
    
    # Relationships
    qr_ticket = relationship("QRTicket", back_populates="entrance_logs")