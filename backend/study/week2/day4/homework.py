"""
Week 2 - Day 4 과제

회원가입/로그인 API 만들기 with 완벽한 검증
"""

from fastapi import FastAPI, HTTPException, Depends, status, Header
from pydantic import BaseModel, Field, validator, EmailStr
from typing import Optional, List
from datetime import datetime, date, timedelta
from enum import Enum
import re
import hashlib
import secrets

app = FastAPI(title="회원 시스템 API")

# === 과제 1: 회원 스키마 정의 ===

class Gender(str, Enum):
    """성별"""
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"

class MembershipType(str, Enum):
    """회원 등급"""
    BASIC = "basic"
    PREMIUM = "premium"
    VIP = "vip"

class SignUpRequest(BaseModel):
    """
    회원가입 요청
    
    요구사항:
    1. username: 4-20자, 영문/숫자/언더스코어만
    2. email: 유효한 이메일
    3. password: 8자 이상, 대문자/소문자/숫자/특수문자 각 1개 이상
    4. password_confirm: password와 일치
    5. full_name: 2-50자, 한글/영문/공백만
    6. phone: 한국 휴대폰 번호
    7. birth_date: 14세 이상
    8. gender: 선택사항
    9. agree_terms: 필수 동의
    10. agree_marketing: 선택적 동의
    """
    # TODO: 구현하세요
    username: str = Field(..., min_length=4, max_length=20)
    email: EmailStr
    password: str = Field(..., min_length=8)
    password_confirm: str
    full_name: str = Field(..., min_length=2, max_length=50)
    phone: str
    birth_date: date
    gender: Optional[Gender] = None
    agree_terms: bool
    agree_marketing: bool = False
    
    @validator('username')
    def validate_username(cls, v):
        if not re.match(r'^[a-zA-Z0-9_]+$', v):
            raise ValueError('username은 영문, 숫자, 언더스코어만 가능합니다')
        return v
    
    # TODO: 나머지 validator들 구현

class LoginRequest(BaseModel):
    """
    로그인 요청
    username 또는 email로 로그인 가능
    """
    # TODO: 구현하세요
    login_id: str  # username or email
    password: str

class MemberResponse(BaseModel):
    """
    회원 정보 응답 (비밀번호 제외)
    """
    # TODO: 구현하세요
    id: int
    username: str
    email: str
    full_name: str
    membership_type: MembershipType
    created_at: datetime

class MemberUpdate(BaseModel):
    """회원 정보 수정"""
    full_name: Optional[str] = None
    phone: Optional[str] = None
    current_password: Optional[str] = None
    new_password: Optional[str] = None

class TokenResponse(BaseModel):
    """
    로그인 토큰 응답
    """
    access_token: str
    token_type: str = "bearer"
    expires_in: int = 3600
    member: MemberResponse


# === 과제 2: 패스워드 강도 체크 ===

def check_password_strength(password: str) -> dict:
    """
    패스워드 강도 체크
    
    반환값:
    {
        "score": 0-5,  # 강도 점수
        "strength": "weak|fair|good|strong|very_strong",
        "feedback": ["개선 사항 리스트"]
    }
    """
    # TODO: 구현하세요
    score = 0
    feedback = []
    
    # 길이 체크
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    
    # 문자 종류 체크
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("소문자를 포함해주세요")
    
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("대문자를 포함해주세요")
    
    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("숫자를 포함해주세요")
    
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("특수문자를 포함해주세요")
    
    # 강도 판정
    strength_map = {
        0: "weak",
        1: "weak",
        2: "fair",
        3: "good",
        4: "strong",
        5: "very_strong",
        6: "very_strong"
    }
    
    return {
        "score": min(score, 5),
        "strength": strength_map[score],
        "feedback": feedback
    }


# === 과제 3: 가짜 데이터베이스 ===

members_db = {}
tokens_db = {}  # 토큰: 회원ID 매핑
member_counter = 0


# === 헬퍼 함수 ===

def hash_password(password: str) -> str:
    """패스워드 해시"""
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """패스워드 검증"""
    return hash_password(plain_password) == hashed_password

def create_token() -> str:
    """토큰 생성"""
    return secrets.token_urlsafe(32)

def get_authorization_header(authorization: Optional[str] = Header(None)) -> str:
    """Authorization 헤더 추출"""
    if not authorization:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authorization header required"
        )
    return authorization


# === 과제 4: API 엔드포인트 ===

@app.post("/signup", response_model=MemberResponse, status_code=status.HTTP_201_CREATED)
async def sign_up(request: SignUpRequest):
    """
    회원가입
    
    - 중복 username/email 체크
    - 패스워드 해시 저장 (평문 저장 금지!)
    - 회원 ID는 자동 생성
    """
    # TODO: 구현하세요
    global member_counter
    
    # 중복 체크
    for member in members_db.values():
        if member['username'] == request.username:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="이미 사용 중인 username입니다"
            )
        if member['email'] == request.email:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="이미 가입된 이메일입니다"
            )
    
    # 회원 생성
    member_counter += 1
    new_member = {
        'id': member_counter,
        'username': request.username,
        'email': request.email,
        'password_hash': hash_password(request.password),
        'full_name': request.full_name,
        'phone': request.phone,
        'birth_date': request.birth_date,
        'gender': request.gender,
        'membership_type': MembershipType.BASIC,
        'created_at': datetime.now(),
        'agree_terms': request.agree_terms,
        'agree_marketing': request.agree_marketing
    }
    
    members_db[member_counter] = new_member
    
    return MemberResponse(
        id=new_member['id'],
        username=new_member['username'],
        email=new_member['email'],
        full_name=new_member['full_name'],
        membership_type=new_member['membership_type'],
        created_at=new_member['created_at']
    )


@app.post("/login", response_model=TokenResponse)
async def login(request: LoginRequest):
    """
    로그인
    
    - username 또는 email로 로그인
    - 패스워드 검증
    - 토큰 생성 및 반환
    """
    # TODO: 구현하세요
    pass


@app.get("/members/me", response_model=MemberResponse)
async def get_current_member(
    authorization: str = Depends(get_authorization_header)
):
    """
    현재 로그인한 회원 정보
    
    - Authorization 헤더에서 토큰 추출
    - 토큰 검증
    - 회원 정보 반환
    """
    # TODO: 구현하세요
    pass


@app.put("/members/me")
async def update_member(
    member_update: MemberUpdate,
    authorization: str = Depends(get_authorization_header)
):
    """
    회원 정보 수정
    
    - 현재 로그인한 회원만 수정 가능
    - 비밀번호 변경 시 현재 비밀번호 확인
    """
    # TODO: 구현하세요
    pass


@app.post("/logout")
async def logout(
    authorization: str = Depends(get_authorization_header)
):
    """
    로그아웃
    
    - 토큰 무효화
    """
    # TODO: 구현하세요
    pass


# === 과제 5: 추가 기능 ===

@app.post("/check-username")
async def check_username(username: str):
    """
    username 중복 체크
    
    반환: {"available": true/false}
    """
    # TODO: 구현하세요
    for member in members_db.values():
        if member['username'] == username:
            return {"available": False}
    return {"available": True}


@app.post("/check-email")
async def check_email(email: str):
    """
    email 중복 체크
    
    반환: {"available": true/false}
    """
    # TODO: 구현하세요
    pass


@app.post("/password-strength")
async def check_password(password: str):
    """패스워드 강도 체크 API"""
    return check_password_strength(password)


# === 테스트 및 실행 ===

if __name__ == "__main__":
    print("""
    회원 시스템 API 과제
    
    구현해야 할 것:
    1. SignUpRequest의 모든 validator
    2. login 엔드포인트
    3. get_current_member 엔드포인트
    4. update_member 엔드포인트
    5. logout 엔드포인트
    6. check_email 엔드포인트
    
    테스트 방법:
    1. uvicorn homework:app --reload
    2. http://localhost:8000/docs 에서 테스트
    
    평가 기준:
    - 모든 검증 규칙 구현
    - 에러 처리
    - 보안 (패스워드 해시)
    - 코드 가독성
    """)
