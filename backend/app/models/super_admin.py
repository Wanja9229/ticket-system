from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.sql import func

from app.database import Base


class SuperAdmin(Base):
    __tablename__ = "super_admins"

    id = Column(Integer, primary_key=True, index=True)  # SERIAL -> Integer, UUID에서 변경
    username = Column(String(50), unique=True, nullable=False, index=True)
    email = Column(String(100), unique=True, nullable=False)  # 길이 255->100으로 변경
    password_hash = Column(String(255), nullable=False)
    full_name = Column(String(100), nullable=False)  # name -> full_name으로 변경
    is_active = Column(Boolean, default=True, nullable=False)
    created_at = Column(DateTime, server_default=func.current_timestamp())  # timezone 제거, func.now() -> func.current_timestamp()
    updated_at = Column(DateTime, server_default=func.current_timestamp())  # onupdate 제거 (트리거에서 처리)