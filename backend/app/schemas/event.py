from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, List
from datetime import datetime


# Base schemas
class EventBase(BaseModel):
    code: str = Field(..., min_length=3, max_length=50)
    name: str = Field(..., min_length=1, max_length=200)
    description: Optional[str] = None
    location: Optional[str] = None
    start_date: datetime
    end_date: datetime
    image_url: Optional[str] = None
    is_active: bool = True
    max_tickets_per_order: int = Field(default=4, ge=1, le=10)


# Create schema
class EventCreate(EventBase):
    pass


# Update schema
class EventUpdate(BaseModel):
    code: Optional[str] = Field(None, min_length=3, max_length=50)
    name: Optional[str] = Field(None, min_length=1, max_length=200)
    description: Optional[str] = None
    location: Optional[str] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    image_url: Optional[str] = None
    is_active: Optional[bool] = None
    max_tickets_per_order: Optional[int] = Field(None, ge=1, le=10)


# Response schema
class EventResponse(EventBase):
    model_config = ConfigDict(from_attributes=True)
    
    id: str
    is_deleted: bool
    created_at: datetime
    updated_at: Optional[datetime]


# List response with pagination
class EventListResponse(BaseModel):
    items: List[EventResponse]
    total: int
    page: int
    size: int
    pages: int
