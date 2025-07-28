"""
Week 2 - Day 4: Pydantic 스키마와 데이터 검증

PHP의 수동 검증 vs FastAPI의 자동 검증
"""

from fastapi import FastAPI, HTTPException, Query, Path, Body
from pydantic import BaseModel, Field, validator, EmailStr
from typing import Optional, List, Union
from datetime import datetime, date
from enum import Enum
import re

app = FastAPI(title="데이터 검증 예제")

# === 1. 기본 검증 ===
class UserBase(BaseModel):
    """기본 사용자 모델"""
    # PHP: if (strlen($username) < 3 || strlen($username) > 20) { ... }
    username: str = Field(..., min_length=3, max_length=20, description="사용자명")
    
    # PHP: if (!filter_var($email, FILTER_VALIDATE_EMAIL)) { ... }
    email: EmailStr  # 자동 이메일 검증
    
    # PHP: if ($age < 18 || $age > 100) { ... }
    age: int = Field(..., ge=18, le=100, description="나이")
    
    # 선택적 필드 with 기본값
    is_active: bool = True
    bio: Optional[str] = Field(None, max_length=500)


# === 2. 커스텀 검증 (validator) ===
class UserCreate(UserBase):
    """사용자 생성 모델 with 추가 검증"""
    password: str = Field(..., min_length=8)
    phone: str
    
    @validator('username')
    def username_alphanumeric(cls, v):
        """사용자명은 영문자와 숫자만"""
        if not v.replace('_', '').isalnum():
            raise ValueError('사용자명은 영문자, 숫자, 언더스코어만 가능합니다')
        return v
    
    @validator('password')
    def password_strength(cls, v):
        """비밀번호 강도 검증"""
        if not re.search(r'[A-Z]', v):
            raise ValueError('비밀번호는 최소 1개의 대문자를 포함해야 합니다')
        if not re.search(r'[0-9]', v):
            raise ValueError('비밀번호는 최소 1개의 숫자를 포함해야 합니다')
        return v
    
    @validator('phone')
    def phone_validation(cls, v):
        """전화번호 형식 검증"""
        # 한국 전화번호 패턴
        pattern = r'^01[0-9]-?[0-9]{3,4}-?[0-9]{4}$'
        if not re.match(pattern, v.replace('-', '')):
            raise ValueError('올바른 전화번호 형식이 아닙니다 (예: 010-1234-5678)')
        return v


# === 3. 중첩된 모델 ===
class Address(BaseModel):
    """주소 모델"""
    street: str
    city: str
    country: str = "Korea"
    postal_code: str = Field(..., regex=r'^\d{5}$')  # 5자리 우편번호

class UserWithAddress(UserBase):
    """주소가 포함된 사용자"""
    address: Address  # 중첩된 모델


# === 4. Enum 사용 ===
class UserRole(str, Enum):
    ADMIN = "admin"
    USER = "user"
    GUEST = "guest"

class TicketType(str, Enum):
    ADULT = "adult"
    CHILD = "child"
    SENIOR = "senior"


# === 5. 날짜/시간 검증 ===
class Event(BaseModel):
    """이벤트 모델"""
    name: str
    event_date: date  # 날짜만
    start_time: datetime  # 날짜와 시간
    price: float = Field(..., gt=0, description="가격은 0보다 커야 함")
    
    @validator('event_date')
    def date_not_past(cls, v):
        """과거 날짜 불가"""
        if v < date.today():
            raise ValueError('이벤트 날짜는 오늘 이후여야 합니다')
        return v


# === 6. 리스트와 딕셔너리 검증 ===
class Order(BaseModel):
    """주문 모델"""
    items: List[str] = Field(..., min_items=1, description="최소 1개 이상")
    quantities: List[int] = Field(..., min_items=1)
    metadata: dict = {}  # 자유 형식 딕셔너리
    tags: List[str] = Field(default_factory=list, max_items=5)
    
    @validator('quantities', each_item=True)
    def check_positive(cls, v):
        """수량은 양수만"""
        if v <= 0:
            raise ValueError('수량은 0보다 커야 합니다')
        return v


# === 7. Union 타입 (여러 타입 허용) ===
class PaymentMethod(BaseModel):
    """결제 수단"""
    # 카드번호 또는 계좌번호
    account: Union[str, int]
    # 금액은 정수 또는 실수
    amount: Union[int, float] = Field(..., gt=0)


# === API 엔드포인트에서 사용 ===

@app.post("/users/")
def create_user(user: UserCreate):
    """사용자 생성 - 자동 검증"""
    # 여기 도달했다면 모든 검증 통과
    return {"message": "사용자 생성 성공", "user": user}


@app.post("/users/with-address/")
def create_user_with_address(user: UserWithAddress):
    """주소 포함 사용자 생성"""
    return {"message": "생성 성공", "user": user}


# === 쿼리 파라미터 검증 ===
@app.get("/items/")
def read_items(
    # PHP: $page = max(1, intval($_GET['page'] ?? 1));
    page: int = Query(1, ge=1, description="페이지 번호"),
    size: int = Query(10, ge=1, le=100, description="페이지 크기"),
    sort: Optional[str] = Query(None, regex="^(name|price|date)$"),
    role: Optional[UserRole] = Query(None, description="사용자 역할")
):
    """아이템 목록 - 쿼리 파라미터 검증"""
    return {
        "page": page,
        "size": size,
        "sort": sort,
        "role": role
    }


# === 경로 파라미터 검증 ===
@app.get("/users/{user_id}")
def get_user(
    user_id: int = Path(..., ge=1, description="사용자 ID")
):
    """사용자 조회 - 경로 파라미터 검증"""
    return {"user_id": user_id}


# === 요청 본문 추가 검증 ===
@app.post("/events/")
def create_event(
    event: Event = Body(..., example={
        "name": "Python 컨퍼런스",
        "event_date": "2024-12-25",
        "start_time": "2024-12-25T09:00:00",
        "price": 50000
    })
):
    """이벤트 생성 with 예제"""
    return {"message": "이벤트 생성 성공", "event": event}


# === 응답 모델 ===
class UserResponse(BaseModel):
    """응답용 사용자 모델 (비밀번호 제외)"""
    id: int
    username: str
    email: str
    created_at: datetime
    
    class Config:
        # 예제 데이터
        schema_extra = {
            "example": {
                "id": 1,
                "username": "johndoe",
                "email": "john@example.com",
                "created_at": "2024-01-01T00:00:00"
            }
        }


@app.post("/register/", response_model=UserResponse)
def register(user: UserCreate):
    """회원가입 - 응답에서 비밀번호 제외"""
    # 실제로는 DB에 저장
    return UserResponse(
        id=1,
        username=user.username,
        email=user.email,
        created_at=datetime.now()
    )


# === 에러 응답 모델 ===
class ErrorResponse(BaseModel):
    """에러 응답"""
    error: str
    detail: str
    timestamp: datetime = Field(default_factory=datetime.now)


@app.get("/error-example/", responses={
    200: {"model": UserResponse},
    404: {"model": ErrorResponse}
})
def error_example(user_id: int):
    """에러 응답 예제"""
    if user_id == 999:
        raise HTTPException(
            status_code=404,
            detail={"error": "Not Found", "detail": "사용자를 찾을 수 없습니다"}
        )
    return UserResponse(
        id=user_id,
        username="testuser",
        email="test@example.com",
        created_at=datetime.now()
    )


if __name__ == "__main__":
    print("""
    Pydantic 검증 예제
    
    주요 기능:
    1. 자동 타입 검증
    2. 필드 제약 조건 (min/max, regex 등)
    3. 커스텀 validator
    4. 중첩된 모델
    5. Enum 타입
    6. 날짜/시간 검증
    7. 에러 메시지 자동 생성
    
    테스트:
    - 잘못된 데이터로 요청하면 422 에러와 함께 상세한 에러 메시지
    - Swagger UI에서 모든 검증 규칙 확인 가능
    
    PHP와 차이점:
    - 수동 검증 코드 불필요
    - 타입 힌트로 자동 문서화
    - 일관된 에러 응답
    """)
