from pydantic import BaseModel, Field, ConfigDict, validator
from typing import Optional, List
from datetime import datetime, date


# Base schemas
class EventBase(BaseModel):
    event_code: str = Field(..., min_length=1, max_length=20, description="이벤트 고유 코드")
    title: str = Field(..., min_length=1, max_length=200, description="이벤트 제목")
    description: Optional[str] = Field(None, description="이벤트 설명")
    image_url: Optional[str] = Field(None, max_length=500, description="이벤트 이미지 URL")
    start_date: date = Field(..., description="이벤트 시작일")
    end_date: date = Field(..., description="이벤트 종료일")
    is_active: bool = Field(default=True, description="활성화 여부")


# Create schema (클라이언트용)
class EventCreate(EventBase):
    @validator('end_date')
    def validate_date_range(cls, v, values):
        if 'start_date' in values and v < values['start_date']:
            raise ValueError('종료일은 시작일보다 이후여야 합니다')
        return v
    
    @validator('event_code')
    def validate_event_code(cls, v):
        if not v.isupper():
            raise ValueError('이벤트 코드는 대문자여야 합니다')
        if not v.isalnum():
            raise ValueError('이벤트 코드는 영문자와 숫자만 포함해야 합니다')
        return v
    
    @validator('title')
    def validate_title(cls, v):
        if not v.strip():
            raise ValueError('이벤트 제목은 필수입니다')
        return v.strip()


# Internal Create schema (서버 내부용 - created_by 포함)
class EventCreateInternal(EventCreate):
    """서버 내부에서 사용하는 이벤트 생성 스키마 - created_by 필드 포함"""
    created_by: int = Field(..., description="이벤트 생성자 ID")
    
    # EventCreate의 모든 validator를 상속받음
    # 추가 validator가 필요하다면 여기에 정의


# Update schema
class EventUpdate(BaseModel):
    event_code: Optional[str] = Field(None, min_length=1, max_length=20)
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    description: Optional[str] = None
    image_url: Optional[str] = Field(None, max_length=500)
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    is_active: Optional[bool] = None
    
    @validator('end_date')
    def validate_date_range(cls, v, values):
        if v and 'start_date' in values and values['start_date'] and v < values['start_date']:
            raise ValueError('종료일은 시작일보다 이후여야 합니다')
        return v


# Response schema
class EventResponse(EventBase):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    is_deleted: str  # 'Y' or 'N'
    created_by: int
    created_at: datetime
    updated_at: datetime


# List response with pagination
class EventListResponse(BaseModel):
    items: List[EventResponse]
    total: int
    page: int
    size: int
    pages: int