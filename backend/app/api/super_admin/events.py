from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.dependencies import get_current_super_admin
from app.models.super_admin import SuperAdmin

router = APIRouter()


@router.get("/")
async def get_events(
    db: Session = Depends(get_db),
    current_admin: SuperAdmin = Depends(get_current_super_admin)
):
    """모든 이벤트 목록 조회"""
    # TODO: Implement event list logic
    return {"message": "Event list", "admin": current_admin.username}


@router.post("/")
async def create_event(
    db: Session = Depends(get_db),
    current_admin: SuperAdmin = Depends(get_current_super_admin)
):
    """새 이벤트 생성"""
    # TODO: Implement event creation logic
    return {"message": "Event created"}
