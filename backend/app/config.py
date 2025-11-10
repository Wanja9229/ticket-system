from pydantic_settings import BaseSettings
from typing import List
import secrets
import os

class Settings(BaseSettings):
    # Database
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/ticket_system")
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://localhost:6379/0")
    
    # Security
    SECRET_KEY: str = os.getenv("SECRET_KEY", secrets.token_urlsafe(32))
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # Server
    SERVER_HOST: str = "0.0.0.0"
    SERVER_PORT: int = int(os.getenv("PORT", "8000"))  # Render는 PORT 환경변수 사용
    PROJECT_NAME: str = "Ticket System"
    VERSION: str = "1.0.0"
    DEBUG: bool = os.getenv("DEBUG", "True") == "True"
    
    # External APIs
    TOSS_PAYMENTS_CLIENT_KEY: str = os.getenv("TOSS_PAYMENTS_CLIENT_KEY", "")
    TOSS_PAYMENTS_SECRET_KEY: str = os.getenv("TOSS_PAYMENTS_SECRET_KEY", "")
    KAKAO_ALIMTALK_API_KEY: str = os.getenv("KAKAO_ALIMTALK_API_KEY", "")
    
    # File Upload
    UPLOAD_DIR: str = os.getenv("UPLOAD_DIR", "./uploads")
    MAX_UPLOAD_SIZE: int = 10485760  # 10MB
    
    # CORS
    CORS_ORIGINS: List[str] = [
        "http://localhost:3000", 
        "http://localhost:3001",
        os.getenv("FRONTEND_URL", "")  # 프론트엔드 배포 주소
    ]
    
    class Config:
        env_file = ".env"
        case_sensitive = True
        extra = "allow"  # 추가 환경 변수 허용


settings = Settings()