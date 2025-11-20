from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import Optional
from datetime import datetime

class CustomerCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    phone: str = Field(..., min_length=10, max_length=20)  # ✅ 유연하게
    password: str = Field(..., min_length=8)
    email: Optional[EmailStr] = None
    
    @field_validator('phone')
    @classmethod
    def normalize_phone(cls, v):
        # 전화번호 정규화 (숫자만 추출)
        return ''.join(filter(str.isdigit, v))

class CustomerLogin(BaseModel):
    phone: str
    password: str

class CustomerResponse(BaseModel):
    id: int
    name: str
    phone: str
    email: Optional[str]
    is_active: bool
    is_verified: bool
    last_login: Optional[datetime]
    created_at: datetime

    class Config:
        from_attributes = True

class CustomerUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None