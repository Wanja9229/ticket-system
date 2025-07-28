from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db

router = APIRouter()


@router.get("/")
async def get_active_events(db: Session = Depends(get_db)):
    """활성화된 이벤트 목록 조회 (공개)"""
    # TODO: Implement public event list logic
    return {"message": "Public event list"}


@router.get("/{event_code}")
async def get_event_detail(event_code: str, db: Session = Depends(get_db)):
    """이벤트 상세 정보 조회 (공개)"""
    # TODO: Implement event detail logic
    return {"message": f"Event detail for {event_code}"}
