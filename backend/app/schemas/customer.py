from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime

class CustomerCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    phone: str = Field(..., pattern=r"^\d{3}-\d{3,4}-\d{4}$")
    password: str = Field(..., min_length=8)
    email: Optional[EmailStr] = None

class CustomerLogin(BaseModel):
    phone : str
    password : str

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
