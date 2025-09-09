from sqlalchemy import Column, String, DateTime, ForeignKey, Boolean, Integer
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.database import Base


class QRTicket(Base):
    __tablename__ = "qr_tickets"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    order_item_id = Column(Integer, ForeignKey("order_items.id"), nullable=False)
    qr_code = Column(String(100), unique=True, nullable=False)
    ticket_type = Column(String(50), nullable=False)
    is_used = Column(Boolean, default=False, nullable=False)
    used_at = Column(DateTime)
    used_by = Column(Integer)
    created_at = Column(DateTime, server_default=func.current_timestamp())
    updated_at = Column(DateTime, server_default=func.current_timestamp())
    
    # Relationships
    order = relationship("Order", back_populates="qr_tickets")
    order_item = relationship("OrderItem", back_populates="qr_tickets")
    entrance_logs = relationship("EntranceLog", back_populates="qr_ticket")