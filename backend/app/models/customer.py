"""
고객 정보 관리 모델
"""

from typing import List, Optional
from sqlalchemy import Integer, String, DateTime, UniqueConstraint, Index, PrimaryKeyConstraint, text
from sqlalchemy.orm import Mapped, mapped_column, relationship
import datetime

from .base import Base


class Customers(Base):
    __tablename__ = 'customers'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='customers_pkey'),
        UniqueConstraint('phone', name='customers_phone_key'),
        Index('idx_customers_email', 'email'),
        Index('idx_customers_name', 'name'),
        Index('idx_customers_phone', 'phone', unique=True)
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    phone: Mapped[str] = mapped_column(String(20))
    email: Mapped[Optional[str]] = mapped_column(String(100))
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    updated_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))

    # Relationships
    orders: Mapped[List['Orders']] = relationship('Orders', back_populates='customer')
