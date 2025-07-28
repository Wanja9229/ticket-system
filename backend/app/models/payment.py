from sqlalchemy import Column, String, DateTime, ForeignKey, Numeric, JSON
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
import uuid

from app.database import Base


class Payment(Base):
    __tablename__ = "payments"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    order_id = Column(String, ForeignKey("orders.id"), unique=True, nullable=False)
    payment_key = Column(String(200), unique=True, nullable=False, index=True)
    method = Column(String(50), nullable=False)  # card, transfer, etc.
    amount = Column(Numeric(10, 2), nullable=False)
    status = Column(String(20), nullable=False)  # ready, approved, cancelled, failed
    approved_at = Column(DateTime(timezone=True))
    raw_data = Column(JSON)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    order = relationship("Order", back_populates="payment")
