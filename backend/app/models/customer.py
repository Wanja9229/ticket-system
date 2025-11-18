from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.database import Base


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    phone = Column(String(20), unique=True, nullable=False, index=True)
    password_hash = Column(String(255), nullable=False)
    email = Column(String(100), unique=True, nullable=True, index=True)
    
    is_active = Column(Boolean, default =True)
    is_verified = Column(Boolean, default =True)

    last_login = Column(DateTime, nullable=True)
    failed_login_attempts = Column(Integer, default=0)
    
    created_at = Column(DateTime, server_default=func.current_timestamp())
    updated_at = Column(DateTime, server_default=func.current_timestamp())
    
    # Relationships
    orders = relationship("Order", back_populates="customer")