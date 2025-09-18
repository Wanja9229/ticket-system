from pydantic import BaseModel, Field, ConfigDict, validator
from typing import Optional, List
from datetime import datetime
from decimal import Decimal


# ProductOption schemas
class ProductOptionBase(BaseModel):
    option_name: str = Field(..., min_length=1, max_length=100, description="옵션명")
    price_adjustment: Decimal = Field(default=0, ge=-999999.99, le=999999.99, description="가격 조정")
    stock_quantity: int = Field(..., ge=0, description="재고 수량")
    is_active: bool = Field(default=True, description="활성화 여부")


class ProductOptionCreate(ProductOptionBase):
    current_stock: Optional[int] = None
    
    @validator('current_stock', always=True)
    def validate_current_stock(cls, v, values):
        return v if v is not None else values.get('stock_quantity', 0)


class ProductOptionUpdate(BaseModel):
    option_name: Optional[str] = Field(None, min_length=1, max_length=100)
    price_adjustment: Optional[Decimal] = Field(None, ge=-999999.99, le=999999.99)
    stock_quantity: Optional[int] = Field(None, ge=0)
    current_stock: Optional[int] = Field(None, ge=0)
    is_active: Optional[bool] = None


class ProductOptionResponse(ProductOptionBase):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    product_id: int
    current_stock: int
    is_deleted: str
    created_at: datetime
    updated_at: datetime


# Product schemas - Level 1 버전 (단순화)
class ProductBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=200, description="상품명")
    description: Optional[str] = Field(None, description="상품 설명")
    base_price: Decimal = Field(..., ge=0, le=9999999.99, description="기본 가격")
    base_stock: int = Field(..., ge=0, description="기본 재고")
    is_active: bool = Field(default=True, description="활성화 여부")


class ProductCreate(ProductBase):
    event_id: int = Field(..., description="이벤트 ID")
    current_stock: Optional[int] = None
    
    @validator('current_stock', always=True)
    def validate_current_stock(cls, v, values):
        return v if v is not None else values.get('base_stock', 0)


class ProductUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=200)
    description: Optional[str] = None
    base_price: Optional[Decimal] = Field(None, ge=0, le=9999999.99)
    base_stock: Optional[int] = Field(None, ge=0)
    current_stock: Optional[int] = Field(None, ge=0)
    is_active: Optional[bool] = None


class ProductResponse(ProductBase):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    event_id: int
    current_stock: int
    is_deleted: str
    created_by: int
    created_at: datetime
    updated_at: datetime


class ProductListResponse(BaseModel):
    """상품 목록 응답"""
    items: List[ProductResponse]
    total: int
    page: int
    size: int
    pages: int
