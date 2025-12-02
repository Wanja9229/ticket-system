from fastapi import APIRouter, Depends, HTTPException, status, Response, Cookie
from sqlalchemy.orm import Session
from datetime import timedelta
from typing import Optional

from app.database import get_db
from app.schemas.auth import LoginSchema
from app.core.security import verify_password, create_access_token
from app.config import settings
from app.models.super_admin import SuperAdmin
from app.dependencies import get_current_super_admin

router = APIRouter()


@router.post("/login")
async def login(
    login_data: LoginSchema, 
    response: Response,
    db: Session = Depends(get_db)
):
    """슈퍼 관리자 로그인"""
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
    
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": str(admin.id), "type": "super_admin"},
        expires_delta=access_token_expires
    )
    
    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,
        secure=settings.ENVIRONMENT == "production",  # ✅ 환경별 분기
        samesite="lax",
        max_age=settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60,
        path="/"
    )
    
    return {"message": "Login successful"}


@router.get("/me")
async def get_current_admin_info(
    current_admin: SuperAdmin = Depends(get_current_super_admin)
):
    """현재 로그인한 관리자 정보"""
    return {
        "id": current_admin.id,
        "username": current_admin.username,
        "type": "super_admin",
        "is_active": current_admin.is_active,
        "created_at": current_admin.created_at
    }


@router.post("/logout")
async def logout(
    response: Response,
    access_token: Optional[str] = Cookie(None)
):
    """슈퍼 관리자 로그아웃"""
    if not access_token:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Already logged out"
        )
    
    response.delete_cookie(
        key="access_token",
        path="/",
        secure=settings.ENVIRONMENT == "production",  # ✅ 환경별 분기
        httponly=True,
        samesite="lax"
    )
    
    return {"message": "Logout successful"}