"""
Week 2 - Day 3: CRUD API 예제

실제 프로젝트에서 사용하는 CRUD 패턴
"""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from enum import Enum

app = FastAPI(title="이벤트 관리 API")

# === 데이터 모델 ===
class EventStatus(str, Enum):
    """이벤트 상태"""
    DRAFT = "draft"
    PUBLISHED = "published"
    CLOSED = "closed"

class EventBase(BaseModel):
    """이벤트 기본 모델"""
    name: str = Field(..., min_length=1, max_length=200, description="이벤트명")
    description: Optional[str] = Field(None, description="설명")
    location: str = Field(..., description="장소")
    start_date: datetime = Field(..., description="시작일")
    end_date: datetime = Field(..., description="종료일")
    max_attendees: int = Field(100, ge=1, le=10000, description="최대 참가자")
    status: EventStatus = EventStatus.DRAFT

class EventCreate(EventBase):
    """이벤트 생성 요청"""
    pass

class EventUpdate(BaseModel):
    """이벤트 수정 요청"""
    name: Optional[str] = Field(None, min_length=1, max_length=200)
    description: Optional[str] = None
    location: Optional[str] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    max_attendees: Optional[int] = Field(None, ge=1, le=10000)
    status: Optional[EventStatus] = None

class EventResponse(EventBase):
    """이벤트 응답"""
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    current_attendees: int = 0

    class Config:
        from_attributes = True  # Pydantic v2


# === 가짜 데이터베이스 ===
class FakeDB:
    def __init__(self):
        self.events = {}
        self.counter = 0
    
    def create(self, event: EventCreate) -> EventResponse:
        self.counter += 1
        event_data = event.dict()
        event_data.update({
            "id": self.counter,
            "created_at": datetime.now(),
            "updated_at": None,
            "current_attendees": 0
        })
        self.events[self.counter] = event_data
        return EventResponse(**event_data)
    
    def get(self, event_id: int) -> Optional[EventResponse]:
        event = self.events.get(event_id)
        if event:
            return EventResponse(**event)
        return None
    
    def get_all(self) -> List[EventResponse]:
        return [EventResponse(**event) for event in self.events.values()]
    
    def update(self, event_id: int, event_update: EventUpdate) -> Optional[EventResponse]:
        if event_id not in self.events:
            return None
        
        event = self.events[event_id]
        update_data = event_update.dict(exclude_unset=True)
        update_data["updated_at"] = datetime.now()
        event.update(update_data)
        return EventResponse(**event)
    
    def delete(self, event_id: int) -> bool:
        if event_id in self.events:
            del self.events[event_id]
            return True
        return False

# DB 인스턴스
db = FakeDB()


# === API 엔드포인트 ===

@app.post("/events/", response_model=EventResponse, status_code=status.HTTP_201_CREATED)
def create_event(event: EventCreate):
    """
    새 이벤트 생성
    
    - **name**: 이벤트명 (필수)
    - **location**: 장소 (필수)
    - **start_date**: 시작일시 (필수)
    - **end_date**: 종료일시 (필수)
    """
    # 날짜 검증
    if event.end_date <= event.start_date:
        raise HTTPException(
            status_code=400,
            detail="종료일은 시작일보다 늦어야 합니다"
        )
    
    return db.create(event)


@app.get("/events/", response_model=List[EventResponse])
def get_events(
    status: Optional[EventStatus] = None,
    skip: int = 0,
    limit: int = 100
):
    """이벤트 목록 조회"""
    events = db.get_all()
    
    # 상태 필터링
    if status:
        events = [e for e in events if e.status == status]
    
    # 페이지네이션
    return events[skip : skip + limit]


@app.get("/events/{event_id}", response_model=EventResponse)
def get_event(event_id: int):
    """특정 이벤트 조회"""
    event = db.get(event_id)
    if not event:
        raise HTTPException(
            status_code=404,
            detail=f"이벤트 {event_id}를 찾을 수 없습니다"
        )
    return event


@app.put("/events/{event_id}", response_model=EventResponse)
def update_event(event_id: int, event_update: EventUpdate):
    """이벤트 정보 수정"""
    # 날짜 검증 (둘 다 제공된 경우)
    if event_update.start_date and event_update.end_date:
        if event_update.end_date <= event_update.start_date:
            raise HTTPException(
                status_code=400,
                detail="종료일은 시작일보다 늦어야 합니다"
            )
    
    event = db.update(event_id, event_update)
    if not event:
        raise HTTPException(
            status_code=404,
            detail=f"이벤트 {event_id}를 찾을 수 없습니다"
        )
    return event


@app.delete("/events/{event_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_event(event_id: int):
    """이벤트 삭제"""
    if not db.delete(event_id):
        raise HTTPException(
            status_code=404,
            detail=f"이벤트 {event_id}를 찾을 수 없습니다"
        )
    # 204 No Content는 본문이 없어야 함
    return None


@app.patch("/events/{event_id}/publish", response_model=EventResponse)
def publish_event(event_id: int):
    """이벤트 공개"""
    event = db.get(event_id)
    if not event:
        raise HTTPException(
            status_code=404,
            detail=f"이벤트 {event_id}를 찾을 수 없습니다"
        )
    
    if event.status != EventStatus.DRAFT:
        raise HTTPException(
            status_code=400,
            detail="초안 상태의 이벤트만 공개할 수 있습니다"
        )
    
    update = EventUpdate(status=EventStatus.PUBLISHED)
    return db.update(event_id, update)


# === 유용한 팁 ===
@app.get("/")
def root():
    return {
        "message": "이벤트 관리 API",
        "docs": "/docs",
        "endpoints": {
            "POST /events/": "이벤트 생성",
            "GET /events/": "이벤트 목록",
            "GET /events/{id}": "이벤트 조회",
            "PUT /events/{id}": "이벤트 수정",
            "DELETE /events/{id}": "이벤트 삭제",
            "PATCH /events/{id}/publish": "이벤트 공개"
        }
    }


if __name__ == "__main__":
    print("""
    CRUD API 테스트 방법:
    
    1. 서버 실행:
       uvicorn crud_example:app --reload
    
    2. Swagger UI에서 테스트:
       http://localhost:8000/docs
    
    3. curl 예제:
       # 생성
       curl -X POST http://localhost:8000/events/ \\
         -H "Content-Type: application/json" \\
         -d '{
           "name": "Python 컨퍼런스",
           "location": "서울",
           "start_date": "2024-04-01T09:00:00",
           "end_date": "2024-04-02T18:00:00",
           "max_attendees": 500
         }'
       
       # 조회
       curl http://localhost:8000/events/
       
       # 수정
       curl -X PUT http://localhost:8000/events/1 \\
         -H "Content-Type: application/json" \\
         -d '{"status": "published"}'
    """)
