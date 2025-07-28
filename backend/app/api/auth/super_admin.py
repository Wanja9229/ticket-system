from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import timedelta

from app.database import get_db
from app.schemas.auth import LoginSchema, TokenSchema
from app.core.security import verify_password, create_access_token
from app.config import settings
from app.models.super_admin import SuperAdmin

router = APIRouter()


@router.post("/login", response_model=TokenSchema)
async def login(login_data: LoginSchema, db: Session = Depends(get_db)):
    """슈퍼 관리자 로그인"""
    # Find super admin by username
    admin = db.query(SuperAdmin).filter(
        SuperAdmin.username == login_data.username
    ).first()
    
    if not admin or not verify_password(login_data.password, admin.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password"
        )
    
    if not admin.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Account is disabled"
        )
    
    # Create access token
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": admin.id, "type": "super_admin"},
        expires_delta=access_token_expires
    )
    
    return TokenSchema(access_token=access_token)
