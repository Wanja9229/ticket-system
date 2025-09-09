from sqlalchemy import Column, String, DateTime, Text, Boolean, Integer, ForeignKey, Numeric, CHAR
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(Integer, ForeignKey("events.id"), nullable=False)
    name = Column(String(200), nullable=False)
    description = Column(Text)
    base_price = Column(Numeric(10, 2), nullable=False)
    base_stock = Column(Integer, nullable=False, default=0)
    current_stock = Column(Integer, nullable=False, default=0)
    is_active = Column(Boolean, default=True, nullable=False)
    is_deleted = Column(CHAR(1), default='N', nullable=False)
    created_by = Column(Integer, nullable=False)
    created_at = Column(DateTime, server_default=func.current_timestamp())
    updated_at = Column(DateTime, server_default=func.current_timestamp())
    
    # Relationships
    event = relationship("Event", back_populates="products")
    options = relationship("ProductOption", back_populates="product", cascade="all, delete-orphan")
    order_items = relationship("OrderItem", back_populates="product")


class ProductOption(Base):
    __tablename__ = "product_options"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    option_name = Column(String(100), nullable=False)
    price_adjustment = Column(Numeric(10, 2), default=0)
    stock_quantity = Column(Integer, nullable=False, default=0)
    current_stock = Column(Integer, nullable=False, default=0)
    is_active = Column(Boolean, default=True, nullable=False)
    is_deleted = Column(CHAR(1), default='N', nullable=False)
    created_at = Column(DateTime, server_default=func.current_timestamp())
    updated_at = Column(DateTime, server_default=func.current_timestamp())
    
    # Relationships
    product = relationship("Product", back_populates="options")