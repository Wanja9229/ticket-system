# 전시회 티켓 예약 시스템 - 백엔드 API 및 서비스

> **프로젝트명**: ticket-system  
> **목표**: 다중 관리자 지원 고성능 FastAPI 백엔드  
> **작성일**: 2025.07.25  
> **버전**: v2.0 (권한 기반 API 시스템)

## 📋 목차

1. [백엔드 아키텍처 개요](#-백엔드-아키텍처-개요)
2. [프로젝트 구조](#-프로젝트-구조)
3. [권한 기반 인증 시스템](#-권한-기반-인증-시스템)
4. [슈퍼 관리자 API](#-슈퍼-관리자-api)
5. [이벤트 관리자 API](#-이벤트-관리자-api)
6. [공통 API (고객용)](#-공통-api-고객용)
7. [외부 API 연동](#-외부-api-연동)
8. [비즈니스 로직 서비스](#-비즈니스-로직-서비스)
9. [미들웨어 및 보안](#-미들웨어-및-보안)
10. [설정 및 환경변수](#-설정-및-환경변수)

---

## 🏗 백엔드 아키텍처 개요

### 🎯 설계 원칙

```mermaid
graph TB
    subgraph "Client Layer"
        PWA[PWA 앱]
        Web[웹 브라우저]
        Admin[관리자 대시보드]
    end
    
    subgraph "API Gateway"
        Nginx[nginx Reverse Proxy]
        RateLimit[Rate Limiting]
        SSL[SSL/TLS]
    end
    
    subgraph "FastAPI Application"
        Auth[권한 미들웨어]
        Router[API Router]
        Validation[Pydantic 검증]
    end
    
    subgraph "Business Logic"
        SuperAdmin[슈퍼 관리자 서비스]
        EventManager[이벤트 관리자 서비스]
        Booking[예약 서비스]
        Payment[결제 서비스]
        QR[QR 티켓 서비스]
        Notification[알림 서비스]
    end
    
    subgraph "Data Layer"
        PostgreSQL[(PostgreSQL)]
        Redis[(Redis)]
        FileSystem[파일 시스템]
    end
    
    subgraph "External APIs"
        TossAPI[토스페이먼츠]
        KakaoAPI[카카오 알림톡]
    end
    
    PWA --> Nginx
    Web --> Nginx
    Admin --> Nginx
    
    Nginx --> Auth
    Auth --> Router
    Router --> Validation
    
    Validation --> SuperAdmin
    Validation --> EventManager
    Validation --> Booking
    Validation --> Payment
    Validation --> QR
    Validation --> Notification
    
    SuperAdmin --> PostgreSQL
    EventManager --> PostgreSQL
    Booking --> Redis
    Booking --> PostgreSQL
    Payment --> TossAPI
    Notification --> KakaoAPI
    
    QR --> FileSystem
```

### 🔧 핵심 컴포넌트

**1. 권한 기반 라우팅 시스템**
- JWT 토큰 검증
- 권한 레벨별 접근 제어
- 이벤트별 데이터 격리

**2. 비동기 처리 최적화**
- `async/await` 패턴
- 비동기 데이터베이스 연결
- 동시 처리 최적화

**3. 실시간 재고 관리**
- Redis 기반 캐시
- 원자적 연산 보장
- 오버셀링 방지

**4. 확장 가능한 서비스 레이어**
- 모듈화된 비즈니스 로직
- 의존성 주입 패턴
- 테스트 가능한 구조

---

## 📁 프로젝트 구조

### 디렉토리 구조

```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py                    # FastAPI 애플리케이션 진입점
│   ├── config.py                  # 설정 관리
│   ├── database.py                # 데이터베이스 연결
│   ├── dependencies.py            # 공통 의존성
│   │
│   ├── models/                    # SQLAlchemy 모델
│   │   ├── __init__.py
│   │   ├── super_admin.py         # 슈퍼 관리자 모델
│   │   ├── event.py               # 이벤트 모델
│   │   ├── event_manager.py       # 이벤트 관리자 모델
│   │   ├── product.py             # 상품 모델
│   │   ├── order.py               # 주문 모델
│   │   ├── payment.py             # 결제 모델
│   │   ├── qr_ticket.py           # QR 티켓 모델
│   │   ├── notice.py              # 공지사항 모델
│   │   └── activity_log.py        # 활동 로그 모델
│   │
│   ├── schemas/                   # Pydantic 스키마
│   │   ├── __init__.py
│   │   ├── super_admin.py         # 슈퍼 관리자 스키마
│   │   ├── event.py               # 이벤트 스키마
│   │   ├── event_manager.py       # 이벤트 관리자 스키마
│   │   ├── product.py             # 상품 스키마
│   │   ├── order.py               # 주문 스키마
│   │   ├── payment.py             # 결제 스키마
│   │   ├── qr_ticket.py           # QR 티켓 스키마
│   │   ├── notice.py              # 공지사항 스키마
│   │   ├── auth.py                # 인증 스키마
│   │   └── common.py              # 공통 스키마
│   │
│   ├── api/                       # API 라우터
│   │   ├── __init__.py
│   │   ├── deps.py                # API 의존성
│   │   ├── super_admin/           # 슈퍼 관리자 API
│   │   │   ├── __init__.py
│   │   │   ├── events.py          # 이벤트 관리
│   │   │   ├── managers.py        # 관리자 관리
│   │   │   ├── analytics.py       # 전체 통계
│   │   │   └── system.py          # 시스템 설정
│   │   ├── event_manager/         # 이벤트 관리자 API
│   │   │   ├── __init__.py
│   │   │   ├── products.py        # 상품 관리
│   │   │   ├── orders.py          # 주문 관리
│   │   │   ├── entrance.py        # 입장 관리
│   │   │   ├── notices.py         # 공지사항 관리
│   │   │   └── analytics.py       # 이벤트 통계
│   │   ├── public/                # 공개 API (고객용)
│   │   │   ├── __init__.py
│   │   │   ├── events.py          # 이벤트 정보
│   │   │   ├── products.py        # 상품 조회
│   │   │   ├── booking.py         # 예약 처리
│   │   │   ├── payment.py         # 결제 처리
│   │   │   └── notices.py         # 공지사항 조회
│   │   └── auth/                  # 인증 API
│   │       ├── __init__.py
│   │       ├── super_admin.py     # 슈퍼 관리자 인증
│   │       └── event_manager.py   # 이벤트 관리자 인증
│   │
│   ├── services/                  # 비즈니스 로직 서비스
│   │   ├── __init__.py
│   │   ├── auth_service.py        # 인증 서비스
│   │   ├── super_admin_service.py # 슈퍼 관리자 서비스
│   │   ├── event_service.py       # 이벤트 서비스
│   │   ├── product_service.py     # 상품 서비스
│   │   ├── booking_service.py     # 예약 서비스
│   │   ├── payment_service.py     # 결제 서비스
│   │   ├── qr_service.py          # QR 티켓 서비스
│   │   ├── notification_service.py # 알림 서비스
│   │   ├── cache_service.py       # 캐시 서비스
│   │   └── file_service.py        # 파일 서비스
│   │
│   ├── core/                      # 핵심 모듈
│   │   ├── __init__.py
│   │   ├── security.py            # 보안 관련
│   │   ├── permissions.py         # 권한 관리
│   │   ├── middleware.py          # 미들웨어
│   │   ├── exceptions.py          # 예외 처리
│   │   ├── redis_client.py        # Redis 클라이언트
│   │   └── logger.py              # 로깅 설정
│   │
│   ├── crud/                      # CRUD 작업
│   │   ├── __init__.py
│   │   ├── base.py                # 기본 CRUD
│   │   ├── super_admin.py         # 슈퍼 관리자 CRUD
│   │   ├── event.py               # 이벤트 CRUD
│   │   ├── event_manager.py       # 이벤트 관리자 CRUD
│   │   ├── product.py             # 상품 CRUD
│   │   ├── order.py               # 주문 CRUD
│   │   ├── payment.py             # 결제 CRUD
│   │   ├── qr_ticket.py           # QR 티켓 CRUD
│   │   ├── notice.py              # 공지사항 CRUD
│   │   └── activity_log.py        # 활동 로그 CRUD
│   │
│   └── utils/                     # 유틸리티 함수
│       ├── __init__.py
│       ├── date_utils.py          # 날짜 처리
│       ├── qr_generator.py        # QR 코드 생성
│       ├── order_number.py        # 주문번호 생성
│       ├── email_validator.py     # 이메일 검증
│       └── file_utils.py          # 파일 처리
│
├── alembic/                       # 데이터베이스 마이그레이션
│   ├── versions/
│   ├── env.py
│   └── script.py.mako
│
├── tests/                         # 테스트 코드
│   ├── __init__.py
│   ├── conftest.py                # 테스트 설정
│   ├── test_auth.py               # 인증 테스트
│   ├── test_super_admin.py        # 슈퍼 관리자 테스트
│   ├── test_booking.py            # 예약 테스트
│   └── test_payment.py            # 결제 테스트
│
├── requirements.txt               # Python 의존성
├── requirements-dev.txt           # 개발 의존성
├── .env.example                   # 환경변수 예시
├── .env                           # 환경변수 (실제)
├── alembic.ini                    # Alembic 설정
├── pytest.ini                    # pytest 설정
└── Dockerfile                     # Docker 설정 (옵션)
```

---

## 🔐 권한 기반 인증 시스템

### JWT 토큰 구조

```python
# app/core/security.py
from datetime import datetime, timedelta
from typing import Optional, Union
import jwt
from passlib.context import CryptContext
from app.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_access_token(
    subject: Union[str, int], 
    admin_type: str,  # 'super_admin' or 'event_manager'
    event_id: Optional[int] = None,
    permission_level: Optional[int] = None,
    expires_delta: Optional[timedelta] = None
) -> str:
    """JWT 액세스 토큰 생성"""
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    
    to_encode = {
        "exp": expire,
        "sub": str(subject),
        "admin_type": admin_type,
        "event_id": event_id,
        "permission_level": permission_level,
        "iat": datetime.utcnow()
    }
    
    encoded_jwt = jwt.encode(
        to_encode, 
        settings.SECRET_KEY, 
        algorithm=settings.ALGORITHM
    )
    return encoded_jwt

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """비밀번호 검증"""
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    """비밀번호 해싱"""
    return pwd_context.hash(password)

def decode_token(token: str) -> dict:
    """JWT 토큰 디코딩"""
    try:
        payload = jwt.decode(
            token, 
            settings.SECRET_KEY, 
            algorithms=[settings.ALGORITHM]
        )
        return payload
    except jwt.PyJWTError:
        return None
```

### 권한 검증 시스템

```python
# app/core/permissions.py
from enum import IntEnum
from typing import Optional
from fastapi import HTTPException, status

class PermissionLevel(IntEnum):
    """권한 레벨 정의"""
    VIEWER = 1          # 조회 전용
    STAFF = 2           # 일반 관리자
    MANAGER = 3         # 담당자
    SUPER_ADMIN = 9     # 슈퍼 관리자

class Permission:
    """권한 검증 클래스"""
    
    @staticmethod
    def check_super_admin(admin_type: str) -> bool:
        """슈퍼 관리자 권한 확인"""
        return admin_type == "super_admin"
    
    @staticmethod
    def check_event_access(
        admin_type: str, 
        admin_event_id: Optional[int], 
        target_event_id: int
    ) -> bool:
        """이벤트 접근 권한 확인"""
        if admin_type == "super_admin":
            return True
        return admin_event_id == target_event_id
    
    @staticmethod
    def check_permission_level(
        current_level: int, 
        required_level: PermissionLevel
    ) -> bool:
        """권한 레벨 확인"""
        return current_level >= required_level.value
    
    @staticmethod
    def require_permission(
        admin_type: str,
        permission_level: int,
        required_level: PermissionLevel,
        event_id: Optional[int] = None,
        target_event_id: Optional[int] = None
    ):
        """권한 요구사항 검증"""
        # 슈퍼 관리자는 모든 권한 허용
        if admin_type == "super_admin":
            return True
        
        # 권한 레벨 확인
        if not Permission.check_permission_level(permission_level, required_level):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"권한이 부족합니다. 필요 권한: {required_level.name}"
            )
        
        # 이벤트 접근 권한 확인
        if target_event_id and not Permission.check_event_access(
            admin_type, event_id, target_event_id
        ):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="해당 이벤트에 대한 접근 권한이 없습니다."
            )
        
        return True
```

### 의존성 주입을 통한 권한 검증

```python
# app/api/deps.py
from typing import Generator, Optional
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.core.security import decode_token
from app.core.permissions import Permission, PermissionLevel
from app.crud import super_admin as crud_super_admin
from app.crud import event_manager as crud_event_manager

security = HTTPBearer()

def get_db() -> Generator:
    """데이터베이스 세션 의존성"""
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):
    """현재 사용자 정보 가져오기"""
    token = credentials.credentials
    payload = decode_token(token)
    
    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="유효하지 않은 토큰입니다."
        )
    
    admin_id = payload.get("sub")
    admin_type = payload.get("admin_type")
    
    if admin_type == "super_admin":
        admin = crud_super_admin.get(db, id=admin_id)
    else:
        admin = crud_event_manager.get(db, id=admin_id)
    
    if admin is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="사용자를 찾을 수 없습니다."
        )
    
    return {
        "admin": admin,
        "admin_type": admin_type,
        "event_id": payload.get("event_id"),
        "permission_level": payload.get("permission_level", 1)
    }

def require_super_admin(
    current_user: dict = Depends(get_current_user)
):
    """슈퍼 관리자 권한 필요"""
    if not Permission.check_super_admin(current_user["admin_type"]):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="슈퍼 관리자 권한이 필요합니다."
        )
    return current_user

def require_manager_or_above(
    current_user: dict = Depends(get_current_user)
):
    """담당자 이상 권한 필요"""
    Permission.require_permission(
        current_user["admin_type"],
        current_user["permission_level"],
        PermissionLevel.MANAGER
    )
    return current_user

def require_staff_or_above(
    current_user: dict = Depends(get_current_user)
):
    """일반 관리자 이상 권한 필요"""
    Permission.require_permission(
        current_user["admin_type"],
        current_user["permission_level"],
        PermissionLevel.STAFF
    )
    return current_user

def check_event_access(event_id: int):
    """특정 이벤트 접근 권한 확인 데코레이터"""
    def dependency(current_user: dict = Depends(get_current_user)):
        Permission.require_permission(
            current_user["admin_type"],
            current_user["permission_level"],
            PermissionLevel.VIEWER,
            current_user["event_id"],
            event_id
        )
        return current_user
    return dependency
```

---

## 👑 슈퍼 관리자 API

### 이벤트 관리 API

```python
# app/api/super_admin/events.py
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.api.deps import get_db, require_super_admin
from app.schemas import event as event_schemas
from app.services import event_service
from app.services import super_admin_service

router = APIRouter(prefix="/super-admin/events", tags=["슈퍼관리자-이벤트"])

@router.get("/", response_model=List[event_schemas.EventDetail])
async def get_all_events(
    skip: int = 0,
    limit: int = 100,
    is_active: bool = None,
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_super_admin)
):
    """모든 이벤트 조회"""
    events = await event_service.get_all_events(
        db=db, 
        skip=skip, 
        limit=limit, 
        is_active=is_active
    )
    return events

@router.post("/", response_model=event_schemas.EventDetail)
async def create_event(
    event_data: event_schemas.EventCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_super_admin)
):
    """새 이벤트 생성"""
    event = await super_admin_service.create_event(
        db=db,
        event_data=event_data,
        created_by=current_user["admin"].id
    )
    return event

@router.get("/{event_id}", response_model=event_schemas.EventDetail)
async def get_event(
    event_id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_super_admin)
):
    """특정 이벤트 상세 조회"""
    event = await event_service.get_event_by_id(db=db, event_id=event_id)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="이벤트를 찾을 수 없습니다."
        )
    return event

@router.put("/{event_id}", response_model=event_schemas.EventDetail)
async def update_event(
    event_id: int,
    event_data: event_schemas.EventUpdate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_super_admin)
):
    """이벤트 정보 수정"""
    event = await super_admin_service.update_event(
        db=db,
        event_id=event_id,
        event_data=event_data,
        updated_by=current_user["admin"].id
    )
    return event

@router.delete("/{event_id}")
async def delete_event(
    event_id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_super_admin)
):
    """이벤트 삭제 (Soft Delete)"""
    await super_admin_service.delete_event(
        db=db,
        event_id=event_id,
        deleted_by=current_user["admin"].id
    )
    return {"message": "이벤트가 삭제되었습니다."}

@router.post("/{event_id}/activate")
async def activate_event(
    event_id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_super_admin)
):
    """이벤트 활성화"""
    await super_admin_service.toggle_event_status(
        db=db,
        event_id=event_id,
        is_active=True,
        updated_by=current_user["admin"].id
    )
    return {"message": "이벤트가 활성화되었습니다."}

@router.post("/{event_id}/deactivate")
async def deactivate_event(
    event_id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_super_admin)
):
    """이벤트 비활성화"""
    await super_admin_service.toggle_event_status(
        db=db,
        event_id=event_id,
        is_active=False,
        updated_by=current_user["admin"].id
    )
    return {"message": "이벤트가 비활성화되었습니다."}
```

### 관리자 관리 API

```python
# app/api/super_admin/managers.py
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.api.deps import get_db, require_super_admin
from app.schemas import event_manager as manager_schemas
from app.services import super_admin_service

router = APIRouter(prefix="/super-admin/managers", tags=["슈퍼관리자-관리자"])

@router.get("/", response_model=List[manager_schemas.EventManagerDetail])
async def get_all_managers(
    skip: int = 0,
    limit: int = 100,
    event_id: int = None,
    permission_level: int = None,
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_super_admin)
):
    """모든 이벤트 관리자 조회"""
    managers = await super_admin_service.get_all_managers(
        db=db,
        skip=skip,
        limit=limit,
        event_id=event_id,
        permission_level=permission_level
    )
    return managers

@router.post("/", response_model=manager_schemas.EventManagerDetail)
async def create_manager(
    manager_data: manager_schemas.EventManagerCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_super_admin)
):
    """새 이벤트 관리자 생성"""
    manager = await super_admin_service.create_event_manager(
        db=db,
        manager_data=manager_data,
        created_by=current_user["admin"].id
    )
    return manager

@router.get("/{manager_id}", response_model=manager_schemas.EventManagerDetail)
async def get_manager(
    manager_id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_super_admin)
):
    """특정 관리자 상세 조회"""
    manager = await super_admin_service.get_manager_by_id(
        db=db, 
        manager_id=manager_id
    )
    if not manager:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="관리자를 찾을 수 없습니다."
        )
    return manager

@router.put("/{manager_id}", response_model=manager_schemas.EventManagerDetail)
async def update_manager(
    manager_id: int,
    manager_data: manager_schemas.EventManagerUpdate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_super_admin)
):
    """관리자 정보 수정"""
    manager = await super_admin_service.update_event_manager(
        db=db,
        manager_id=manager_id,
        manager_data=manager_data,
        updated_by=current_user["admin"].id
    )
    return manager

@router.delete("/{manager_id}")
async def delete_manager(
    manager_id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_super_admin)
):
    """관리자 삭제 (Soft Delete)"""
    await super_admin_service.delete_event_manager(
        db=db,
        manager_id=manager_id,
        deleted_by=current_user["admin"].id
    )
    return {"message": "관리자가 삭제되었습니다."}

@router.post("/{manager_id}/reset-password")
async def reset_manager_password(
    manager_id: int,
    new_password: str,
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_super_admin)
):
    """관리자 비밀번호 초기화"""
    await super_admin_service.reset_manager_password(
        db=db,
        manager_id=manager_id,
        new_password=new_password,
        reset_by=current_user["admin"].id
    )
    return {"message": "비밀번호가 초기화되었습니다."}
```

### 전체 통계 API

```python
# app/api/super_admin/analytics.py
from typing import List, Optional
from datetime import date, datetime
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.api.deps import get_db, require_super_admin
from app.schemas import analytics as analytics_schemas
from app.services import analytics_service

router = APIRouter(prefix="/super-admin/analytics", tags=["슈퍼관리자-통계"])

@router.get("/overview", response_model=analytics_schemas.SystemOverview)
async def get_system_overview(
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_super_admin)
):
    """시스템 전체 개요 통계"""
    overview = await analytics_service.get_system_overview(db=db)
    return overview

@router.get("/events-stats", response_model=List[analytics_schemas.EventStats])
async def get_events_statistics(
    start_date: Optional[date] = Query(None),
    end_date: Optional[date] = Query(None),
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_super_admin)
):
    """이벤트별 통계"""
    stats = await analytics_service.get_events_statistics(
        db=db,
        start_date=start_date,
        end_date=end_date
    )
    return stats

@router.get("/revenue-analysis", response_model=analytics_schemas.RevenueAnalysis)
async def get_revenue_analysis(
    period: str = Query("monthly", regex="^(daily|weekly|monthly|yearly)$"),
    start_date: Optional[date] = Query(None),
    end_date: Optional[date] = Query(None),
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_super_admin)
):
    """매출 분석"""
    analysis = await analytics_service.get_revenue_analysis(
        db=db,
        period=period,
        start_date=start_date,
        end_date=end_date
    )
    return analysis

@router.get("/real-time-dashboard", response_model=analytics_schemas.RealTimeDashboard)
async def get_real_time_dashboard(
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_super_admin)
):
    """실시간 대시보드 데이터"""
    dashboard = await analytics_service.get_real_time_dashboard(db=db)
    return dashboard

@router.get("/activity-logs", response_model=List[analytics_schemas.ActivityLog])
async def get_activity_logs(
    skip: int = 0,
    limit: int = 100,
    admin_type: Optional[str] = Query(None),
    action_type: Optional[str] = Query(None),
    event_id: Optional[int] = Query(None),
    start_date: Optional[datetime] = Query(None),
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_super_admin)
):
    """활동 로그 조회"""
    logs = await analytics_service.get_activity_logs(
        db=db,
        skip=skip,
        limit=limit,
        admin_type=admin_type,
        action_type=action_type,
        event_id=event_id,
        start_date=start_date
    )
    return logs

---

## 🎪 이벤트 관리자 API

### 상품 관리 API

```python
# app/api/event_manager/products.py
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.api.deps import get_db, require_staff_or_above, check_event_access
from app.schemas import product as product_schemas
from app.services import product_service

router = APIRouter(prefix="/admin/products", tags=["이벤트관리자-상품"])

@router.get("/", response_model=List[product_schemas.ProductDetail])
async def get_products(
    skip: int = 0,
    limit: int = 100,
    is_active: bool = None,
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_staff_or_above)
):
    """이벤트 상품 목록 조회"""
    event_id = current_user["event_id"]
    products = await product_service.get_products_by_event(
        db=db,
        event_id=event_id,
        skip=skip,
        limit=limit,
        is_active=is_active
    )
    return products

@router.post("/", response_model=product_schemas.ProductDetail)
async def create_product(
    product_data: product_schemas.ProductCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_staff_or_above)
):
    """새 상품 생성"""
    event_id = current_user["event_id"]
    product = await product_service.create_product(
        db=db,
        event_id=event_id,
        product_data=product_data,
        created_by=current_user["admin"].id
    )
    return product

@router.get("/{product_id}", response_model=product_schemas.ProductDetail)
async def get_product(
    product_id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_staff_or_above)
):
    """상품 상세 정보 조회"""
    product = await product_service.get_product_by_id(
        db=db, 
        product_id=product_id
    )
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="상품을 찾을 수 없습니다."
        )
    
    # 이벤트 접근 권한 확인
    if current_user["admin_type"] != "super_admin":
        if product.event_id != current_user["event_id"]:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="해당 상품에 대한 접근 권한이 없습니다."
            )
    
    return product

@router.put("/{product_id}", response_model=product_schemas.ProductDetail)
async def update_product(
    product_id: int,
    product_data: product_schemas.ProductUpdate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_staff_or_above)
):
    """상품 정보 수정"""
    product = await product_service.update_product(
        db=db,
        product_id=product_id,
        product_data=product_data,
        updated_by=current_user["admin"].id,
        event_id=current_user["event_id"]  # 권한 확인용
    )
    return product

@router.delete("/{product_id}")
async def delete_product(
    product_id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_manager_or_above)  # 삭제는 담당자 이상
):
    """상품 삭제 (Soft Delete)"""
    await product_service.delete_product(
        db=db,
        product_id=product_id,
        deleted_by=current_user["admin"].id,
        event_id=current_user["event_id"]
    )
    return {"message": "상품이 삭제되었습니다."}

@router.post("/{product_id}/options", response_model=product_schemas.ProductOptionDetail)
async def create_product_option(
    product_id: int,
    option_data: product_schemas.ProductOptionCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_staff_or_above)
):
    """상품 옵션 생성"""
    option = await product_service.create_product_option(
        db=db,
        product_id=product_id,
        option_data=option_data,
        event_id=current_user["event_id"]
    )
    return option

@router.put("/options/{option_id}", response_model=product_schemas.ProductOptionDetail)
async def update_product_option(
    option_id: int,
    option_data: product_schemas.ProductOptionUpdate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_staff_or_above)
):
    """상품 옵션 수정"""
    option = await product_service.update_product_option(
        db=db,
        option_id=option_id,
        option_data=option_data,
        event_id=current_user["event_id"]
    )
    return option

@router.delete("/options/{option_id}")
async def delete_product_option(
    option_id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_manager_or_above)
):
    """상품 옵션 삭제"""
    await product_service.delete_product_option(
        db=db,
        option_id=option_id,
        event_id=current_user["event_id"]
    )
    return {"message": "상품 옵션이 삭제되었습니다."}

@router.post("/{product_id}/stock/adjust")
async def adjust_stock(
    product_id: int,
    adjustment: product_schemas.StockAdjustment,
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_staff_or_above)
):
    """재고 조정"""
    await product_service.adjust_stock(
        db=db,
        product_id=product_id,
        adjustment=adjustment,
        adjusted_by=current_user["admin"].id,
        event_id=current_user["event_id"]
    )
    return {"message": "재고가 조정되었습니다."}
```

### 주문 관리 API

```python
# app/api/event_manager/orders.py
from typing import List, Optional
from datetime import date
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from app.api.deps import get_db, require_staff_or_above
from app.schemas import order as order_schemas
from app.services import order_service

router = APIRouter(prefix="/admin/orders", tags=["이벤트관리자-주문"])

@router.get("/", response_model=List[order_schemas.OrderDetail])
async def get_orders(
    skip: int = 0,
    limit: int = 100,
    status: Optional[str] = Query(None),
    visit_date: Optional[date] = Query(None),
    customer_name: Optional[str] = Query(None),
    order_number: Optional[str] = Query(None),
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_staff_or_above)
):
    """주문 목록 조회"""
    event_id = current_user["event_id"]
    orders = await order_service.get_orders_by_event(
        db=db,
        event_id=event_id,
        skip=skip,
        limit=limit,
        status=status,
        visit_date=visit_date,
        customer_name=customer_name,
        order_number=order_number
    )
    return orders

@router.get("/{order_id}", response_model=order_schemas.OrderDetail)
async def get_order(
    order_id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_staff_or_above)
):
    """주문 상세 정보 조회"""
    order = await order_service.get_order_by_id(
        db=db,
        order_id=order_id,
        event_id=current_user["event_id"]
    )
    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="주문을 찾을 수 없습니다."
        )
    return order

@router.post("/{order_id}/refund")
async def process_refund(
    order_id: int,
    refund_data: order_schemas.RefundRequest,
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_manager_or_above)  # 환불은 담당자 이상
):
    """주문 환불 처리"""
    result = await order_service.process_refund(
        db=db,
        order_id=order_id,
        refund_data=refund_data,
        processed_by=current_user["admin"].id,
        event_id=current_user["event_id"]
    )
    return result

@router.put("/{order_id}/status")
async def update_order_status(
    order_id: int,
    status_data: order_schemas.OrderStatusUpdate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_staff_or_above)
):
    """주문 상태 변경"""
    order = await order_service.update_order_status(
        db=db,
        order_id=order_id,
        status_data=status_data,
        updated_by=current_user["admin"].id,
        event_id=current_user["event_id"]
    )
    return order

@router.get("/{order_id}/tickets", response_model=List[order_schemas.QRTicketDetail])
async def get_order_tickets(
    order_id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_staff_or_above)
):
    """주문의 QR 티켓 목록 조회"""
    tickets = await order_service.get_order_tickets(
        db=db,
        order_id=order_id,
        event_id=current_user["event_id"]
    )
    return tickets

@router.post("/export")
async def export_orders(
    export_data: order_schemas.OrderExportRequest,
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_staff_or_above)
):
    """주문 데이터 엑셀 내보내기"""
    file_path = await order_service.export_orders_to_excel(
        db=db,
        event_id=current_user["event_id"],
        export_data=export_data,
        exported_by=current_user["admin"].id
    )
    return {"download_url": f"/downloads/{file_path}"}
```

### 입장 관리 API

```python
# app/api/event_manager/entrance.py
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.api.deps import get_db, require_staff_or_above
from app.schemas import qr_ticket as qr_schemas
from app.services import qr_service

router = APIRouter(prefix="/admin/entrance", tags=["이벤트관리자-입장"])

@router.post("/scan", response_model=qr_schemas.QRScanResult)
async def scan_qr_ticket(
    scan_data: qr_schemas.QRScanRequest,
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_staff_or_above)
):
    """QR 티켓 스캔 및 검증"""
    result = await qr_service.scan_qr_ticket(
        db=db,
        qr_code=scan_data.qr_code,
        scanned_by=current_user["admin"].id,
        event_id=current_user["event_id"],
        device_info=scan_data.device_info
    )
    return result

@router.post("/validate", response_model=qr_schemas.QRValidationResult)
async def validate_qr_ticket(
    qr_code: str,
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_staff_or_above)
):
    """QR 티켓 유효성 검증 (입장 처리 전 확인)"""
    result = await qr_service.validate_qr_ticket(
        db=db,
        qr_code=qr_code,
        event_id=current_user["event_id"]
    )
    return result

@router.post("/process-entrance", response_model=qr_schemas.EntranceResult)
async def process_entrance(
    entrance_data: qr_schemas.EntranceRequest,
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_staff_or_above)
):
    """입장 처리 (QR 티켓 사용 처리)"""
    result = await qr_service.process_entrance(
        db=db,
        qr_code=entrance_data.qr_code,
        processed_by=current_user["admin"].id,
        event_id=current_user["event_id"],
        entrance_type=entrance_data.entrance_type,
        device_info=entrance_data.device_info
    )
    return result

@router.get("/logs", response_model=List[qr_schemas.EntranceLog])
async def get_entrance_logs(
    skip: int = 0,
    limit: int = 100,
    start_date: date = None,
    end_date: date = None,
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_staff_or_above)
):
    """입장 로그 조회"""
    logs = await qr_service.get_entrance_logs(
        db=db,
        event_id=current_user["event_id"],
        skip=skip,
        limit=limit,
        start_date=start_date,
        end_date=end_date
    )
    return logs

@router.get("/stats", response_model=qr_schemas.EntranceStats)
async def get_entrance_stats(
    target_date: date = None,
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_staff_or_above)
):
    """입장 통계"""
    stats = await qr_service.get_entrance_stats(
        db=db,
        event_id=current_user["event_id"],
        target_date=target_date
    )
    return stats

@router.post("/manual-entry")
async def manual_entry(
    entry_data: qr_schemas.ManualEntryRequest,
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_manager_or_above)  # 수동 입장은 담당자 이상
):
    """수동 입장 처리 (QR 없이 입장)"""
    result = await qr_service.process_manual_entry(
        db=db,
        entry_data=entry_data,
        processed_by=current_user["admin"].id,
        event_id=current_user["event_id"]
    )
    return result

---

## 🌐 공통 API (고객용)

### 이벤트 정보 API

```python
# app/api/public/events.py
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status, Path
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.schemas import event as event_schemas
from app.services import event_service

router = APIRouter(prefix="/public/{event_code}", tags=["공개-이벤트"])

@router.get("/info", response_model=event_schemas.EventPublicInfo)
async def get_event_info(
    event_code: str = Path(..., description="이벤트 코드 (AAA, BBB, CCC 등)"),
    db: Session = Depends(get_db)
):
    """이벤트 기본 정보 조회"""
    event = await event_service.get_event_by_code(db=db, event_code=event_code)
    if not event or not event.is_active:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="이벤트를 찾을 수 없거나 비활성 상태입니다."
        )
    return event

@router.get("/products", response_model=List[event_schemas.ProductPublicInfo])
async def get_event_products(
    event_code: str = Path(...),
    db: Session = Depends(get_db)
):
    """이벤트 상품 목록 조회"""
    products = await event_service.get_public_products(
        db=db, 
        event_code=event_code
    )
    return products

@router.get("/notices", response_model=List[event_schemas.NoticePublicInfo])
async def get_event_notices(
    event_code: str = Path(...),
    skip: int = 0,
    limit: int = 20,
    db: Session = Depends(get_db)
):
    """이벤트 공지사항 목록 조회"""
    notices = await event_service.get_public_notices(
        db=db,
        event_code=event_code,
        skip=skip,
        limit=limit
    )
    return notices

@router.get("/notices/{notice_id}", response_model=event_schemas.NoticePublicDetail)
async def get_notice_detail(
    event_code: str = Path(...),
    notice_id: int,
    db: Session = Depends(get_db)
):
    """공지사항 상세 조회"""
    notice = await event_service.get_public_notice_detail(
        db=db,
        event_code=event_code,
        notice_id=notice_id
    )
    if not notice:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="공지사항을 찾을 수 없습니다."
        )
    return notice
```

### 예약 처리 API

```python
# app/api/public/booking.py
from fastapi import APIRouter, Depends, HTTPException, status, Path, BackgroundTasks
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.schemas import booking as booking_schemas
from app.services import booking_service

router = APIRouter(prefix="/public/{event_code}/booking", tags=["공개-예약"])

@router.post("/check-availability", response_model=booking_schemas.AvailabilityCheck)
async def check_availability(
    event_code: str = Path(...),
    check_data: booking_schemas.AvailabilityRequest,
    db: Session = Depends(get_db)
):
    """재고 확인 및 가격 계산"""
    result = await booking_service.check_availability(
        db=db,
        event_code=event_code,
        check_data=check_data
    )
    return result

@router.post("/reserve", response_model=booking_schemas.ReservationResult)
async def create_reservation(
    event_code: str = Path(...),
    reservation_data: booking_schemas.ReservationRequest,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db)
):
    """예약 생성 (재고 임시 확보)"""
    result = await booking_service.create_reservation(
        db=db,
        event_code=event_code,
        reservation_data=reservation_data
    )
    
    # 백그라운드에서 예약 만료 처리 스케줄링
    background_tasks.add_task(
        booking_service.schedule_reservation_timeout,
        result.reservation_id,
        timeout_minutes=10
    )
    
    return result

@router.get("/reservation/{reservation_id}", response_model=booking_schemas.ReservationDetail)
async def get_reservation(
    event_code: str = Path(...),
    reservation_id: str,
    db: Session = Depends(get_db)
):
    """예약 정보 조회"""
    reservation = await booking_service.get_reservation(
        db=db,
        event_code=event_code,
        reservation_id=reservation_id
    )
    if not reservation:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="예약을 찾을 수 없습니다."
        )
    return reservation

@router.post("/reservation/{reservation_id}/extend")
async def extend_reservation(
    event_code: str = Path(...),
    reservation_id: str,
    db: Session = Depends(get_db)
):
    """예약 시간 연장"""
    result = await booking_service.extend_reservation(
        db=db,
        event_code=event_code,
        reservation_id=reservation_id,
        extend_minutes=5
    )
    return result

@router.delete("/reservation/{reservation_id}")
async def cancel_reservation(
    event_code: str = Path(...),
    reservation_id: str,
    db: Session = Depends(get_db)
):
    """예약 취소 (재고 해제)"""
    await booking_service.cancel_reservation(
        db=db,
        event_code=event_code,
        reservation_id=reservation_id
    )
    return {"message": "예약이 취소되었습니다."}
```

### 결제 처리 API

```python
# app/api/public/payment.py
from fastapi import APIRouter, Depends, HTTPException, status, Path, BackgroundTasks
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.schemas import payment as payment_schemas
from app.services import payment_service

router = APIRouter(prefix="/public/{event_code}/payment", tags=["공개-결제"])

@router.post("/initiate", response_model=payment_schemas.PaymentInitiation)
async def initiate_payment(
    event_code: str = Path(...),
    payment_data: payment_schemas.PaymentRequest,
    db: Session = Depends(get_db)
):
    """결제 시작 (토스페이먼츠 연동)"""
    result = await payment_service.initiate_payment(
        db=db,
        event_code=event_code,
        payment_data=payment_data
    )
    return result

@router.post("/success", response_model=payment_schemas.PaymentSuccess)
async def payment_success(
    event_code: str = Path(...),
    success_data: payment_schemas.PaymentSuccessRequest,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db)
):
    """결제 성공 처리"""
    result = await payment_service.process_payment_success(
        db=db,
        event_code=event_code,
        success_data=success_data
    )
    
    # 백그라운드에서 QR 티켓 생성 및 알림 발송
    background_tasks.add_task(
        payment_service.post_payment_processing,
        result.order_id,
        event_code
    )
    
    return result

@router.post("/fail")
async def payment_fail(
    event_code: str = Path(...),
    fail_data: payment_schemas.PaymentFailRequest,
    db: Session = Depends(get_db)
):
    """결제 실패 처리"""
    await payment_service.process_payment_fail(
        db=db,
        event_code=event_code,
        fail_data=fail_data
    )
    return {"message": "결제가 실패했습니다."}

@router.post("/webhook")
async def payment_webhook(
    webhook_data: payment_schemas.PaymentWebhook,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db)
):
    """토스페이먼츠 웹훅 처리"""
    result = await payment_service.process_webhook(
        db=db,
        webhook_data=webhook_data
    )
    
    if result.status == "success":
        background_tasks.add_task(
            payment_service.webhook_post_processing,
            result.order_id
        )
    
    return {"message": "웹훅 처리 완료"}

@router.get("/order/{order_number}", response_model=payment_schemas.OrderDetail)
async def get_order_detail(
    event_code: str = Path(...),
    order_number: str,
    customer_phone: str,
    db: Session = Depends(get_db)
):
    """주문 상세 조회 (고객용)"""
    order = await payment_service.get_customer_order(
        db=db,
        event_code=event_code,
        order_number=order_number,
        customer_phone=customer_phone
    )
    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="주문을 찾을 수 없습니다."
        )
    return order

---

## 🔗 외부 API 연동

### 토스페이먼츠 연동 서비스

```python
# app/services/payment_service.py
import httpx
import json
from typing import Dict, Any
from app.config import settings
from app.core.logger import get_logger

logger = get_logger(__name__)

class TossPaymentService:
    """토스페이먼츠 API 연동 서비스"""
    
    def __init__(self):
        self.base_url = settings.TOSS_PAYMENT_URL
        self.secret_key = settings.TOSS_SECRET_KEY
        self.client_key = settings.TOSS_CLIENT_KEY
    
    async def create_payment(
        self,
        order_id: str,
        amount: int,
        order_name: str,
        customer_email: str,
        customer_name: str,
        success_url: str,
        fail_url: str
    ) -> Dict[str, Any]:
        """결제 요청 생성"""
        try:
            payment_data = {
                "orderId": order_id,
                "amount": amount,
                "orderName": order_name,
                "customerEmail": customer_email,
                "customerName": customer_name,
                "successUrl": success_url,
                "failUrl": fail_url
            }
            
            # 토스페이먼츠 위젯 URL 반환
            return {
                "payment_key": f"TEMP_{order_id}",
                "payment_url": f"https://js.tosspayments.com/v1/payment",
                "client_key": self.client_key,
                "payment_data": payment_data
            }
            
        except Exception as e:
            logger.error(f"토스페이먼츠 결제 생성 실패: {e}")
            raise

    async def confirm_payment(
        self,
        payment_key: str,
        order_id: str,
        amount: int
    ) -> Dict[str, Any]:
        """결제 승인"""
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    f"{self.base_url}/confirm",
                    json={
                        "paymentKey": payment_key,
                        "orderId": order_id,
                        "amount": amount
                    },
                    auth=(self.secret_key, ""),
                    headers={"Content-Type": "application/json"}
                )
                
                if response.status_code == 200:
                    return response.json()
                else:
                    error_data = response.json()
                    logger.error(f"결제 승인 실패: {error_data}")
                    raise Exception(f"결제 승인 실패: {error_data.get('message')}")
                    
        except Exception as e:
            logger.error(f"토스페이먼츠 결제 승인 실패: {e}")
            raise

    async def cancel_payment(
        self,
        payment_key: str,
        cancel_reason: str,
        cancel_amount: int = None
    ) -> Dict[str, Any]:
        """결제 취소"""
        try:
            cancel_data = {
                "cancelReason": cancel_reason
            }
            if cancel_amount:
                cancel_data["cancelAmount"] = cancel_amount
            
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    f"{self.base_url}/{payment_key}/cancel",
                    json=cancel_data,
                    auth=(self.secret_key, ""),
                    headers={"Content-Type": "application/json"}
                )
                
                if response.status_code == 200:
                    return response.json()
                else:
                    error_data = response.json()
                    logger.error(f"결제 취소 실패: {error_data}")
                    raise Exception(f"결제 취소 실패: {error_data.get('message')}")
                    
        except Exception as e:
            logger.error(f"토스페이먼츠 결제 취소 실패: {e}")
            raise

    async def get_payment_info(self, payment_key: str) -> Dict[str, Any]:
        """결제 정보 조회"""
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    f"{self.base_url}/{payment_key}",
                    auth=(self.secret_key, ""),
                    headers={"Content-Type": "application/json"}
                )
                
                if response.status_code == 200:
                    return response.json()
                else:
                    error_data = response.json()
                    logger.error(f"결제 정보 조회 실패: {error_data}")
                    raise Exception(f"결제 정보 조회 실패: {error_data.get('message')}")
                    
        except Exception as e:
            logger.error(f"토스페이먼츠 결제 정보 조회 실패: {e}")
            raise
```

### 카카오 알림톡 연동 서비스

```python
# app/services/notification_service.py
import httpx
import json
from typing import Dict, Any, List
from app.config import settings
from app.core.logger import get_logger

logger = get_logger(__name__)

class KakaoNotificationService:
    """카카오 알림톡 API 연동 서비스"""
    
    def __init__(self):
        self.rest_api_key = settings.KAKAO_REST_API_KEY
        self.sender_key = settings.KAKAO_SENDER_KEY
        self.base_url = "https://kapi.kakao.com/v2/api/talk/memo"
    
    async def send_booking_confirmation(
        self,
        customer_phone: str,
        customer_name: str,
        event_title: str,
        order_number: str,
        visit_date: str,
        ticket_count: int,
        total_amount: int,
        qr_codes: List[str]
    ) -> Dict[str, Any]:
        """예약 확인 알림톡 발송"""
        try:
            template_object = {
                "object_type": "text",
                "text": f"""🎫 [{event_title}] 예약이 완료되었습니다!

👤 예약자: {customer_name}
📋 주문번호: {order_number}
📅 방문일자: {visit_date}
🎟️ 티켓수량: {ticket_count}매
💰 결제금액: {total_amount:,}원

📱 QR코드로 현장에서 빠른 입장이 가능합니다.
스마트폰에 저장하여 입장 시 제시해 주세요.

문의: 고객센터 1588-1234""",
                "link": {
                    "web_url": f"https://ticket-system.com/{event_title.lower()}/order/{order_number}",
                    "mobile_web_url": f"https://ticket-system.com/{event_title.lower()}/order/{order_number}"
                }
            }
            
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    self.base_url + "/default/send",
                    data={
                        "template_object": json.dumps(template_object, ensure_ascii=False)
                    },
                    headers={
                        "Authorization": f"KakaoAK {self.rest_api_key}",
                        "Content-Type": "application/x-www-form-urlencoded"
                    }
                )
                
                if response.status_code == 200:
                    logger.info(f"예약 확인 알림톡 발송 성공: {customer_phone}")
                    return {"success": True, "message": "알림톡 발송 완료"}
                else:
                    error_data = response.json()
                    logger.error(f"알림톡 발송 실패: {error_data}")
                    return {"success": False, "error": error_data}
                    
        except Exception as e:
            logger.error(f"카카오 알림톡 발송 실패: {e}")
            return {"success": False, "error": str(e)}

    async def send_entrance_notification(
        self,
        customer_phone: str,
        customer_name: str,
        event_title: str,
        entrance_time: str,
        entrance_gate: str
    ) -> Dict[str, Any]:
        """입장 완료 알림톡 발송"""
        try:
            template_object = {
                "object_type": "text",
                "text": f"""✅ [{event_title}] 입장이 완료되었습니다!

👤 고객명: {customer_name}
🚪 입장게이트: {entrance_gate}
⏰ 입장시간: {entrance_time}

즐거운 관람 되세요! 🎉""",
                "link": {
                    "web_url": f"https://ticket-system.com/{event_title.lower()}",
                    "mobile_web_url": f"https://ticket-system.com/{event_title.lower()}"
                }
            }
            
            # 실제 카카오 API 호출 로직
            # ...
            
            return {"success": True, "message": "입장 알림톡 발송 완료"}
            
        except Exception as e:
            logger.error(f"입장 알림톡 발송 실패: {e}")
            return {"success": False, "error": str(e)}

    async def send_refund_notification(
        self,
        customer_phone: str,
        customer_name: str,
        order_number: str,
        refund_amount: int,
        refund_reason: str
    ) -> Dict[str, Any]:
        """환불 완료 알림톡 발송"""
        try:
            template_object = {
                "object_type": "text",
                "text": f"""💸 환불이 완료되었습니다.

👤 고객명: {customer_name}
📋 주문번호: {order_number}
💰 환불금액: {refund_amount:,}원
📝 환불사유: {refund_reason}

환불 처리는 영업일 기준 3-5일 소요됩니다.
문의: 고객센터 1588-1234"""
            }
            
            # 실제 카카오 API 호출 로직
            # ...
            
            return {"success": True, "message": "환불 알림톡 발송 완료"}
            
        except Exception as e:
            logger.error(f"환불 알림톡 발송 실패: {e}")
            return {"success": False, "error": str(e)}
```

---

## ⚙️ 설정 및 환경변수

### 메인 설정 파일

```python
# app/config.py
from typing import Optional
from pydantic import BaseSettings, validator

class Settings(BaseSettings):
    """애플리케이션 설정"""
    
    # 기본 설정
    APP_NAME: str = "Ticket System API"
    APP_VERSION: str = "2.0.0"
    DEBUG: bool = False
    ENVIRONMENT: str = "development"
    
    # 서버 설정
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    RELOAD: bool = False
    
    # 데이터베이스 설정
    DATABASE_URL: str
    DATABASE_POOL_SIZE: int = 10
    DATABASE_MAX_OVERFLOW: int = 20
    
    # Redis 설정
    REDIS_URL: str
    REDIS_MAX_CONNECTIONS: int = 20
    
    # JWT 설정
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7일
    
    # 토스페이먼츠 설정
    TOSS_CLIENT_KEY: str
    TOSS_SECRET_KEY: str
    TOSS_PAYMENT_URL: str = "https://api.tosspayments.com/v1/payments"
    
    # 카카오 설정
    KAKAO_REST_API_KEY: str
    KAKAO_SENDER_KEY: str
    
    # 파일 업로드 설정
    UPLOAD_PATH: str = "/opt/ticket-system/uploads"
    MAX_FILE_SIZE: int = 10 * 1024 * 1024  # 10MB
    ALLOWED_EXTENSIONS: list = [".jpg", ".jpeg", ".png", ".gif", ".pdf", ".doc", ".docx"]
    
    # 로깅 설정
    LOG_LEVEL: str = "INFO"
    LOG_FORMAT: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    
    # CORS 설정
    CORS_ORIGINS: list = ["http://localhost:3000", "https://ticket-system.com"]
    CORS_METHODS: list = ["GET", "POST", "PUT", "DELETE", "OPTIONS"]
    CORS_HEADERS: list = ["*"]
    
    # 보안 설정
    BCRYPT_ROUNDS: int = 12
    SESSION_TIMEOUT_MINUTES: int = 30
    MAX_LOGIN_ATTEMPTS: int = 5
    LOCKOUT_DURATION_MINUTES: int = 15
    
    # 성능 설정
    WORKER_TIMEOUT: int = 30
    KEEPALIVE_TIMEOUT: int = 2
    MAX_WORKERS: int = 4
    
    # 예약 설정
    RESERVATION_TIMEOUT_MINUTES: int = 10
    MAX_TICKETS_PER_ORDER: int = 10
    STOCK_WARNING_THRESHOLD: int = 10
    
    @validator("DATABASE_URL")
    def validate_database_url(cls, v):
        if not v.startswith(("postgresql://", "postgresql+asyncpg://")):
            raise ValueError("DATABASE_URL must be a PostgreSQL URL")
        return v
    
    @validator("REDIS_URL")
    def validate_redis_url(cls, v):
        if not v.startswith("redis://"):
            raise ValueError("REDIS_URL must be a Redis URL")
        return v
    
    class Config:
        env_file = ".env"
        case_sensitive = True

# 설정 인스턴스 생성
settings = Settings()
```

### 데이터베이스 연결 설정

```python
# app/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
from app.config import settings

# 동기 엔진 (Alembic 마이그레이션용)
engine = create_engine(
    settings.DATABASE_URL.replace("+asyncpg", ""),
    pool_pre_ping=True,
    pool_size=settings.DATABASE_POOL_SIZE,
    max_overflow=settings.DATABASE_MAX_OVERFLOW
)

# 세션 팩토리
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 베이스 클래스
Base = declarative_base()

# 비동기 엔진 (FastAPI용)
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker as async_sessionmaker

async_engine = create_async_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,
    pool_size=settings.DATABASE_POOL_SIZE,
    max_overflow=settings.DATABASE_MAX_OVERFLOW,
    echo=settings.DEBUG
)

AsyncSessionLocal = async_sessionmaker(
    async_engine,
    class_=AsyncSession,
    expire_on_commit=False
)
```

API 통신 오류: {e}")
                raise
    
    async def cancel_payment(
        self,
        payment_key: str,
        cancel_reason: str,
        cancel_amount: Optional[int] = None
    ) -> Dict[str, Any]:
        """결제 취소"""
        async with httpx.AsyncClient() as client:
            try:
                cancel_data = {"cancelReason": cancel_reason}
                if cancel_amount:
                    cancel_data["cancelAmount"] = cancel_amount
                
                response = await client.post(
                    f"{self.base_url}/{payment_key}/cancel",
                    headers=self.headers,
                    json=cancel_data
                )
                
                if response.status_code == 200:
                    return response.json()
                else:
                    error = response.json()
                    logger.error(f"결제 취소 실패: {error}")
                    raise Exception(error.get("message"))
                    
            except Exception as e:
                logger.error(f"토스페이먼츠 API 통신 오류: {e}")
                raise
```

### 카카오 알림톡 연동

```python
# app/external/kakao_notify.py
import httpx
import json
from typing import Dict, Any, List
from app.config import settings
from app.core.logger import get_logger

logger = get_logger(__name__)

class KakaoNotifyService:
    """카카오 알림톡 서비스"""
    
    def __init__(self):
        self.api_key = settings.KAKAO_API_KEY
        self.sender_key = settings.KAKAO_SENDER_KEY
        self.base_url = settings.KAKAO_API_URL
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"KakaoAK {self.api_key}"
        }
    
    async def send_booking_confirmation(
        self,
        phone: str,
        name: str,
        event_title: str,
        order_number: str,
        visit_date: str,
        ticket_count: int,
        total_amount: int
    ) -> Dict[str, Any]:
        """예약 확인 알림톡"""
        template_data = {
            "template_code": "booking_confirm_001",
            "receiver_num": phone,
            "receiver_name": name,
            "template_args": {
                "event_title": event_title,
                "order_number": order_number,
                "visit_date": visit_date,
                "ticket_count": str(ticket_count),
                "total_amount": f"{total_amount:,}",
                "customer_name": name
            }
        }
        
        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(
                    f"{self.base_url}/send",
                    headers=self.headers,
                    json=template_data
                )
                
                if response.status_code == 200:
                    logger.info(f"알림톡 발송 성공: {order_number}")
                    return response.json()
                else:
                    error = response.json()
                    logger.error(f"알림톡 발송 실패: {error}")
                    return {"success": False, "error": error}
                    
            except Exception as e:
                logger.error(f"카카오 API 통신 오류: {e}")
                return {"success": False, "error": str(e)}
    
    async def send_entrance_notification(
        self,
        phone: str,
        name: str,
        event_title: str,
        entrance_time: str
    ) -> Dict[str, Any]:
        """입장 완료 알림톡"""
        template_data = {
            "template_code": "entrance_complete_001",
            "receiver_num": phone,
            "receiver_name": name,
            "template_args": {
                "event_title": event_title,
                "customer_name": name,
                "entrance_time": entrance_time
            }
        }
        
        # API 호출 로직...
        return {"success": True}
```

---

## 🛡️ 미들웨어 및 보안

### CORS 미들웨어

```python
# app/core/middleware.py
from fastapi import Request, status
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
import time
import uuid
from app.core.logger import get_logger

logger = get_logger(__name__)

class LoggingMiddleware(BaseHTTPMiddleware):
    """요청/응답 로깅 미들웨어"""
    
    async def dispatch(self, request: Request, call_next):
        request_id = str(uuid.uuid4())
        start_time = time.time()
        
        # 요청 로깅
        logger.info(
            f"[{request_id}] {request.method} {request.url.path} "
            f"- Client: {request.client.host}"
        )
        
        # 요청 처리
        response = await call_next(request)
        
        # 응답 로깅
        process_time = time.time() - start_time
        logger.info(
            f"[{request_id}] Status: {response.status_code} "
            f"- Process time: {process_time:.3f}s"
        )
        
        # 응답 헤더 추가
        response.headers["X-Request-ID"] = request_id
        response.headers["X-Process-Time"] = str(process_time)
        
        return response

class RateLimitMiddleware(BaseHTTPMiddleware):
    """Rate Limiting 미들웨어"""
    
    def __init__(self, app, calls: int = 100, period: int = 60):
        super().__init__(app)
        self.calls = calls
        self.period = period
        self.clients = {}
    
    async def dispatch(self, request: Request, call_next):
        client_ip = request.client.host
        now = time.time()
        
        # 클라이언트별 요청 기록
        if client_ip not in self.clients:
            self.clients[client_ip] = []
        
        # 만료된 요청 제거
        self.clients[client_ip] = [
            timestamp for timestamp in self.clients[client_ip]
            if timestamp > now - self.period
        ]
        
        # Rate limit 확인
        if len(self.clients[client_ip]) >= self.calls:
            return JSONResponse(
                status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                content={"detail": "Too many requests"}
            )
        
        # 요청 기록
        self.clients[client_ip].append(now)
        
        response = await call_next(request)
        return response

class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    """보안 헤더 미들웨어"""
    
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        
        # 보안 헤더 추가
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["X-XSS-Protection"] = "1; mode=block"
        response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
        
        return response
```

### 예외 처리

```python
# app/core/exceptions.py
from fastapi import Request, status
from fastapi.responses import JSONResponse
from app.core.logger import get_logger

logger = get_logger(__name__)

class TicketSystemException(Exception):
    """기본 예외 클래스"""
    def __init__(self, message: str, status_code: int = 400):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)

class NotFoundException(TicketSystemException):
    """리소스를 찾을 수 없음"""
    def __init__(self, message: str = "리소스를 찾을 수 없습니다."):
        super().__init__(message, status.HTTP_404_NOT_FOUND)

class UnauthorizedException(TicketSystemException):
    """인증 실패"""
    def __init__(self, message: str = "인증이 필요합니다."):
        super().__init__(message, status.HTTP_401_UNAUTHORIZED)

class ForbiddenException(TicketSystemException):
    """권한 부족"""
    def __init__(self, message: str = "권한이 부족합니다."):
        super().__init__(message, status.HTTP_403_FORBIDDEN)

class ConflictException(TicketSystemException):
    """충돌 (중복 등)"""
    def __init__(self, message: str = "요청이 현재 상태와 충돌합니다."):
        super().__init__(message, status.HTTP_409_CONFLICT)

class ValidationException(TicketSystemException):
    """유효성 검증 실패"""
    def __init__(self, message: str = "입력값이 유효하지 않습니다."):
        super().__init__(message, status.HTTP_422_UNPROCESSABLE_ENTITY)

# 전역 예외 핸들러
async def ticket_system_exception_handler(
    request: Request,
    exc: TicketSystemException
) -> JSONResponse:
    """커스텀 예외 핸들러"""
    logger.error(
        f"TicketSystemException: {exc.message} - "
        f"Path: {request.url.path} - "
        f"Method: {request.method}"
    )
    
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": exc.__class__.__name__,
            "message": exc.message,
            "path": request.url.path
        }
    )

async def general_exception_handler(
    request: Request,
    exc: Exception
) -> JSONResponse:
    """일반 예외 핸들러"""
    logger.error(
        f"Unhandled exception: {str(exc)} - "
        f"Path: {request.url.path} - "
        f"Method: {request.method}",
        exc_info=True
    )
    
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "error": "InternalServerError",
            "message": "서버 내부 오류가 발생했습니다.",
            "path": request.url.path
        }
    )
```

---

## ⚙️ 설정 및 환경변수

### 환경 설정

```python
# app/config.py
from pydantic import BaseSettings, validator
from typing import Optional, List
import os

class Settings(BaseSettings):
    """애플리케이션 설정"""
    
    # 기본 설정
    APP_NAME: str = "Ticket System API"
    APP_VERSION: str = "3.0.0"
    DEBUG: bool = False
    ENVIRONMENT: str = "development"
    
    # 서버 설정
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    WORKERS: int = 4
    
    # 데이터베이스
    DATABASE_URL: str
    DATABASE_POOL_SIZE: int = 20
    DATABASE_MAX_OVERFLOW: int = 0
    
    # Redis
    REDIS_URL: str
    REDIS_MAX_CONNECTIONS: int = 50
    
    # JWT
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    
    # 토스페이먼츠
    TOSS_CLIENT_KEY: str
    TOSS_SECRET_KEY: str
    TOSS_API_URL: str = "https://api.tosspayments.com/v1/payments"
    
    # 카카오
    KAKAO_API_KEY: str
    KAKAO_SENDER_KEY: str
    KAKAO_API_URL: str = "https://kapi.kakao.com/v1/api/talk"
    
    # 파일 업로드
    UPLOAD_DIR: str = "./uploads"
    MAX_UPLOAD_SIZE: int = 10 * 1024 * 1024  # 10MB
    ALLOWED_EXTENSIONS: List[str] = [".jpg", ".jpeg", ".png", ".pdf"]
    
    # CORS
    CORS_ORIGINS: List[str] = ["http://localhost:3000"]
    
    # 로깅
    LOG_LEVEL: str = "INFO"
    LOG_FILE: Optional[str] = None
    
    @validator("DATABASE_URL")
    def validate_database_url(cls, v):
        if not v.startswith(("postgresql://", "postgresql+asyncpg://")):
            raise ValueError("DATABASE_URL must be a PostgreSQL URL")
        return v
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
```

### 데이터베이스 설정

```python
# app/database.py
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import settings

# 비동기 엔진
engine = create_async_engine(
    settings.DATABASE_URL,
    echo=settings.DEBUG,
    pool_size=settings.DATABASE_POOL_SIZE,
    max_overflow=settings.DATABASE_MAX_OVERFLOW,
    pool_pre_ping=True
)

# 세션 팩토리
AsyncSessionLocal = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Base 클래스
Base = declarative_base()

# 동기 엔진 (마이그레이션용)
sync_engine = create_async_engine(
    settings.DATABASE_URL.replace("+asyncpg", ""),
    echo=settings.DEBUG
)
```

### Redis 설정

```python
# app/core/redis_client.py
import redis.asyncio as redis
import json
from typing import Optional, Any
from app.config import settings
from app.core.logger import get_logger

logger = get_logger(__name__)

class RedisClient:
    """Redis 클라이언트"""
    
    def __init__(self):
        self.redis = None
    
    async def connect(self):
        """Redis 연결"""
        self.redis = await redis.from_url(
            settings.REDIS_URL,
            max_connections=settings.REDIS_MAX_CONNECTIONS,
            decode_responses=True
        )
        logger.info("Redis connected")
    
    async def disconnect(self):
        """Redis 연결 해제"""
        if self.redis:
            await self.redis.close()
            logger.info("Redis disconnected")
    
    async def get(self, key: str) -> Optional[Any]:
        """값 조회"""
        value = await self.redis.get(key)
        if value:
            try:
                return json.loads(value)
            except json.JSONDecodeError:
                return value
        return None
    
    async def set(
        self, 
        key: str, 
        value: Any, 
        ttl: Optional[int] = None
    ) -> bool:
        """값 저장"""
        if isinstance(value, (dict, list)):
            value = json.dumps(value)
        
        if ttl:
            return await self.redis.setex(key, ttl, value)
        else:
            return await self.redis.set(key, value)
    
    async def delete(self, key: str) -> bool:
        """값 삭제"""
        return await self.redis.delete(key) > 0
    
    async def exists(self, key: str) -> bool:
        """키 존재 여부"""
        return await self.redis.exists(key) > 0
    
    async def incr(self, key: str, amount: int = 1) -> int:
        """값 증가"""
        return await self.redis.incrby(key, amount)
    
    async def decr(self, key: str, amount: int = 1) -> int:
        """값 감소"""
        return await self.redis.decrby(key, amount)

# 싱글톤 인스턴스
redis_client = RedisClient()
```

---

## 💡 실제 구현 예시

### FastAPI 애플리케이션 초기화

```python
# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from app.config import settings
from app.database import engine
from app.core.redis_client import redis_client
from app.core.middleware import (
    LoggingMiddleware,
    RateLimitMiddleware,
    SecurityHeadersMiddleware
)
from app.core.exceptions import (
    TicketSystemException,
    ticket_system_exception_handler,
    general_exception_handler
)

# API 라우터
from app.api.v1 import api_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    """애플리케이션 수명 주기 관리"""
    # 시작
    await redis_client.connect()
    yield
    # 종료
    await redis_client.disconnect()
    await engine.dispose()

# FastAPI 앱 생성
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    debug=settings.DEBUG,
    lifespan=lifespan
)

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# 커스텀 미들웨어
app.add_middleware(SecurityHeadersMiddleware)
app.add_middleware(RateLimitMiddleware, calls=100, period=60)
app.add_middleware(LoggingMiddleware)

# 예외 핸들러
app.add_exception_handler(TicketSystemException, ticket_system_exception_handler)
app.add_exception_handler(Exception, general_exception_handler)

# API 라우터 등록
app.include_router(api_router, prefix="/api")

# 헬스 체크
@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "version": settings.APP_VERSION,
        "environment": settings.ENVIRONMENT
    }

@app.get("/")
async def root():
    return {
        "message": "Welcome to Ticket System API",
        "version": settings.APP_VERSION,
        "docs": "/docs",
        "redoc": "/redoc"
    }
```

### 실행 스크립트

```python
# run.py
import uvicorn
from app.config import settings

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host=settings.HOST,
        port=settings.PORT,
        workers=settings.WORKERS,
        reload=settings.DEBUG,
        log_level=settings.LOG_LEVEL.lower()
    )
```

### 환경변수 예시

```bash
# .env.example
# Application
APP_NAME="Ticket System API"
APP_VERSION="3.0.0"
DEBUG=False
ENVIRONMENT=production

# Server
HOST=0.0.0.0
PORT=8000
WORKERS=4

# Database
DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/ticket_system
DATABASE_POOL_SIZE=20
DATABASE_MAX_OVERFLOW=0

# Redis
REDIS_URL=redis://localhost:6379/0
REDIS_MAX_CONNECTIONS=50

# JWT
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
REFRESH_TOKEN_EXPIRE_DAYS=7

# Toss Payments
TOSS_CLIENT_KEY=test_ck_xxxxxxxxxxxxx
TOSS_SECRET_KEY=test_sk_xxxxxxxxxxxxx

# Kakao
KAKAO_API_KEY=xxxxxxxxxxxxx
KAKAO_SENDER_KEY=xxxxxxxxxxxxx

# CORS
CORS_ORIGINS=["http://localhost:3000","https://yourdomain.com"]

# Logging
LOG_LEVEL=INFO
```

---

## 📚 다음 단계

이 백엔드 시스템은 다음과 같은 특징을 가집니다:

### 🏗️ **Repository 패턴 적용**
- 데이터 접근 로직의 추상화
- 테스트 용이성 향상
- 비즈니스 로직과 데이터 로직 분리

### 🔐 **강력한 권한 시스템**
- JWT 기반 인증
- 역할별 세분화된 권한
- 이벤트별 데이터 격리

### ⚡ **고성능 아키텍처**
- 비동기 처리 최적화
- Redis 캐싱 전략
- Connection Pool 관리

### 🛡️ **보안 강화**
- Rate Limiting
- 보안 헤더
- 입력값 검증
