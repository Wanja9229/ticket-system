# ==================== app/dependencies/auth.py ====================
from typing import Optional
from fastapi import Depends, HTTPException, status, Cookie
from jose import JWTError, jwt
from sqlalchemy.orm import Session

from app.database import get_db
from app.config import settings
from app.core.security import ALGORITHM
from app.models.super_admin import SuperAdmin
from app.models.event_manager import EventManager


def get_current_super_admin(
    access_token: str = Cookie(...),  # ← Header → Cookie로 변경!
    db: Session = Depends(get_db)
) -> SuperAdmin:
    """
    현재 슈퍼 관리자 가져오기
    
    쿠키에서 access_token을 자동으로 추출하여 검증
    """
    try:
        # JWT 토큰 디코딩
        payload = jwt.decode(access_token, settings.SECRET_KEY, algorithms=[ALGORITHM])
        admin_id: str = payload.get("sub")
        
        # 토큰 타입 확인
        if admin_id is None or payload.get("type") != "super_admin":
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Invalid authentication credentials"
            )
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid authentication credentials"
        )
    
    # DB에서 슈퍼 관리자 조회
    admin = db.query(SuperAdmin).filter(SuperAdmin.id == admin_id).first()
    if admin is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Super admin not found"
        )
    
    # 활성 상태 확인
    if not admin.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin account is disabled"
        )
    
    return admin


def get_current_event_manager(
    access_token: str = Cookie(...),  # ← Header → Cookie로 변경!
    db: Session = Depends(get_db)
) -> EventManager:
    """
    현재 이벤트 관리자 가져오기
    
    쿠키에서 access_token을 자동으로 추출하여 검증
    """
    try:
        # JWT 토큰 디코딩
        payload = jwt.decode(access_token, settings.SECRET_KEY, algorithms=[ALGORITHM])
        manager_id: str = payload.get("sub")
        
        # 토큰 타입 확인
        if manager_id is None or payload.get("type") != "event_manager":
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Invalid authentication credentials"
            )
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid authentication credentials"
        )
    
    # DB에서 이벤트 관리자 조회
    manager = db.query(EventManager).filter(EventManager.id == manager_id).first()
    if manager is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event manager not found"
        )
    
    # 활성 상태 확인
    if not manager.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Manager account is disabled"
        )
    
    return manager


def get_redis_client():
    """Redis 클라이언트 의존성"""
    from app.core.redis_client import redis_client
    return redis_client