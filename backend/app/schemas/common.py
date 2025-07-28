from pydantic import BaseModel, ConfigDict
from typing import Generic, TypeVar, Optional
from datetime import datetime

T = TypeVar('T')


class ResponseSchema(BaseModel, Generic[T]):
    success: bool = True
    message: Optional[str] = None
    data: Optional[T] = None


class PaginationSchema(BaseModel):
    page: int = 1
    size: int = 20
    total: Optional[int] = None


class TimestampSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    created_at: datetime
    updated_at: Optional[datetime] = None
