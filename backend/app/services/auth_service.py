from typing import Optional
from sqlalchemy.orm import Session

from app.models.super_admin import SuperAdmin
from app.models.event_manager import EventManager
from app.core.security import verify_password


class AuthService:
    @staticmethod
    def authenticate_super_admin(
        db: Session, username: str, password: str
    ) -> Optional[SuperAdmin]:
        """슈퍼 관리자 인증"""
        admin = db.query(SuperAdmin).filter(
            SuperAdmin.username == username
        ).first()
        
        if not admin or not verify_password(password, admin.password_hash):
            return None
        
        if not admin.is_active:
            return None
            
        return admin
    
    @staticmethod
    def authenticate_event_manager(
        db: Session, username: str, password: str
    ) -> Optional[EventManager]:
        """이벤트 관리자 인증"""
        manager = db.query(EventManager).filter(
            EventManager.username == username
        ).first()
        
        if not manager or not verify_password(password, manager.password_hash):
            return None
        
        if not manager.is_active:
            return None
            
        return manager
