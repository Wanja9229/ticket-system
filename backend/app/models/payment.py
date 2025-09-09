from sqlalchemy import Column, String, DateTime, ForeignKey, Numeric, JSON, Integer
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.database import Base


class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    payment_key = Column(String(100), unique=True, nullable=False)
    payment_method = Column(String(50), nullable=False)
    amount = Column(Numeric(10, 2), nullable=False)
    status = Column(String(20), default='pending', nullable=False)
    toss_payment_id = Column(String(100))
    payment_data = Column(JSON)
    created_at = Column(DateTime, server_default=func.current_timestamp())
    updated_at = Column(DateTime, server_default=func.current_timestamp())
    
    # Relationships
    order = relationship("Order", back_populates="payments")