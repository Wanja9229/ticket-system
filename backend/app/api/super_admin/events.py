from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from typing import List, Optional
import math

from app.database import get_db
from app.dependencies import get_current_super_admin
from app.models.super_admin import SuperAdmin
from app.models.event import Event
from app.schemas.event import (
    EventCreate, 
    EventCreateInternal,  # 내부용 스키마 추가
    EventUpdate, 
    EventResponse, 
    EventListResponse
)
from app.crud.base import CRUDBase

router = APIRouter()

# CRUDBase 인스턴스 생성 - EventCreateInternal 사용
crud_event = CRUDBase[Event, EventCreateInternal, EventUpdate](Event)


@router.get("/", response_model=EventListResponse)
async def get_events(
    page: int = Query(1, ge=1, description="페이지 번호"),
    size: int = Query(10, ge=1, le=100, description="페이지 크기"),
    search: Optional[str] = Query(None, description="검색어 (제목, 코드)"),
    is_active: Optional[bool] = Query(None, description="활성화 상태 필터"),
    db: Session = Depends(get_db),
    current_admin: SuperAdmin = Depends(get_current_super_admin)
):
    """모든 이벤트 목록 조회"""
    try:
        # 기본 쿼리 (삭제되지 않은 것만)
        query = db.query(Event).filter(Event.is_deleted == 'N')
        
        # 검색 조건 추가
        if search:
            query = query.filter(
                (Event.title.ilike(f"%{search}%")) | 
                (Event.event_code.ilike(f"%{search}%"))
            )
        
        # 활성화 상태 필터
        if is_active is not None:
            query = query.filter(Event.is_active == is_active)
        
        # 전체 개수 계산
        total = query.count()
        
        # 페이지네이션
        offset = (page - 1) * size
        events = query.offset(offset).limit(size).all()
        
        # 전체 페이지 수 계산
        pages = math.ceil(total / size)
        
        return EventListResponse(
            items=events,
            total=total,
            page=page,
            size=size,
            pages=pages
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="이벤트 목록 조회 중 오류가 발생했습니다"
        )


@router.post("/", response_model=EventResponse, status_code=status.HTTP_201_CREATED)
async def create_event(
    event_data: EventCreate,
    db: Session = Depends(get_db),
    current_admin: SuperAdmin = Depends(get_current_super_admin)
):
    """새 이벤트 생성"""
    try:
        # 1. 중복 체크 (삭제되지 않은 것 중에서)
        existing_event = db.query(Event).filter(
            Event.event_code == event_data.event_code,
            Event.is_deleted == 'N'
        ).first()
        
        if existing_event:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"이미 존재하는 이벤트 코드입니다: {event_data.event_code}"
            )
        
        # 2. EventCreate를 EventCreateInternal로 변환 (created_by 추가)
        event_internal = EventCreateInternal(
            **event_data.dict(),
            created_by=current_admin.id
        )
        
        # 3. CRUDBase의 create 메서드 사용
        db_event = crud_event.create(db, obj_in=event_internal)
        
        return db_event
        
    except HTTPException:
        raise
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="데이터 무결성 오류가 발생했습니다"
        )
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="이벤트 생성 중 오류가 발생했습니다"
        )


@router.get("/{event_id}", response_model=EventResponse)
async def get_event(
    event_id: int,
    db: Session = Depends(get_db),
    current_admin: SuperAdmin = Depends(get_current_super_admin)
):
    """특정 이벤트 조회"""
    # CRUDBase의 get 메서드 사용
    event = crud_event.get(db, event_id)
    
    # 삭제된 이벤트는 조회하지 않음
    if not event or event.is_deleted == 'Y':
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="이벤트를 찾을 수 없습니다"
        )
    
    return event


@router.put("/{event_id}", response_model=EventResponse)
async def update_event(
    event_id: int,
    event_data: EventUpdate,
    db: Session = Depends(get_db),
    current_admin: SuperAdmin = Depends(get_current_super_admin)
):
    """이벤트 정보 수정"""
    try:
        # CRUDBase의 get 메서드로 이벤트 조회
        db_event = crud_event.get(db, event_id)
        
        if not db_event or db_event.is_deleted == 'Y':
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="이벤트를 찾을 수 없습니다"
            )
        
        # 이벤트 코드 중복 체크 (자신 제외)
        if event_data.event_code:
            existing_event = db.query(Event).filter(
                Event.event_code == event_data.event_code,
                Event.is_deleted == 'N',
                Event.id != event_id
            ).first()
            
            if existing_event:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"이미 존재하는 이벤트 코드입니다: {event_data.event_code}"
                )
        
        # CRUDBase의 update 메서드 사용
        db_event = crud_event.update(db, db_obj=db_event, obj_in=event_data)
        
        return db_event
        
    except HTTPException:
        raise
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="데이터 무결성 오류가 발생했습니다"
        )
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="이벤트 수정 중 오류가 발생했습니다"
        )


@router.delete("/{event_id}")
async def delete_event(
    event_id: int,
    db: Session = Depends(get_db),
    current_admin: SuperAdmin = Depends(get_current_super_admin)
):
    """이벤트 삭제 (소프트 삭제)"""
    try:
        # CRUDBase의 get 메서드로 이벤트 조회
        db_event = crud_event.get(db, event_id)
        
        if not db_event or db_event.is_deleted == 'Y':
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="이벤트를 찾을 수 없습니다"
            )
        
        # 소프트 삭제 - CRUDBase의 update 메서드 사용
        event_title = db_event.title  # 삭제 메시지용으로 저장
        update_data = {"is_deleted": 'Y', "is_active": False}
        crud_event.update(db, db_obj=db_event, obj_in=update_data)
        
        return {"message": f"이벤트 '{event_title}'이(가) 삭제되었습니다"}
        
    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="이벤트 삭제 중 오류가 발생했습니다"
        )