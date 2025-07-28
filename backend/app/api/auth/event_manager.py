from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import timedelta

from app.database import get_db
from app.schemas.auth import LoginSchema, TokenSchema
from app.core.security import verify_password, create_access_token
from app.config import settings
from app.models.event_manager import EventManager

router = APIRouter()


@router.post("/login", response_model=TokenSchema)
async def login(login_data: LoginSchema, db: Session = Depends(get_db)):
    """이벤트 관리자 로그인"""
    # Find event manager by username
    manager = db.query(EventManager).filter(
        EventManager.username == login_data.username
    ).first()
    
    if not manager or not verify_password(login_data.password, manager.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password"
        )
    
    if not manager.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Account is disabled"
        )
    
    # Create access token
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": manager.id, "type": "event_manager", "event_id": manager.event_id},
        expires_delta=access_token_expires
    )
    
    return TokenSchema(access_token=access_token)
