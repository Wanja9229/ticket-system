from fastapi import APIRouter, Depends, HTTPException, status, Response, Cookie
from sqlalchemy.orm import Session
from typing import Optional
from datetime import datetime, timedelta  # ✅ 상단으로 이동

from app.database import get_db
from app.schemas.customer import (
    CustomerCreate, CustomerLogin, CustomerResponse, CustomerUpdate
)
from app.models.customer import Customer
from app.core.security import (
    verify_password, get_password_hash, create_access_token
)
from app.config import settings
from app.dependencies import get_current_customer

router = APIRouter()

@router.post("/login")
async def login(
    login_data: CustomerLogin,
    response: Response,
    db: Session = Depends(get_db)
):
    """로그인"""
    customer = db.query(Customer).filter(
        Customer.phone == login_data.phone
    ).first()
    
    # 타이밍 공격 방어
    if not customer:
        verify_password("dummy", get_password_hash("dummy"))
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect phone or password"
        )
    
    # 계정 잠금 확인 (비밀번호 검증 전)
    # if customer.locked_until and customer.locked_until > datetime.now():
    #     remaining = (customer.locked_until - datetime.now()).seconds // 60
    #     raise HTTPException(
    #         status_code=status.HTTP_403_FORBIDDEN,
    #         detail=f"Account locked. Try again in {remaining} minutes."
    #     )
    
    # 비활성 계정 확인
    if not customer.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Account is disabled. Contact support."
        )
    
    # 비밀번호 검증
    if not verify_password(login_data.password, customer.password_hash):
        customer.failed_login_attempts += 1
        
        # 5회 실패 시 30분 잠금
        if customer.failed_login_attempts >= 5:
            customer.is_active = False
            # customer.locked_until = datetime.now() + timedelta(minutes=30)
        
        db.commit()
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect phone or password"
        )
    
    # 로그인 성공
    customer.last_login = datetime.now()
    customer.failed_login_attempts = 0
    # customer.locked_until = None
    db.commit()
    
    # JWT 생성 및 쿠키 설정
    access_token = create_access_token(
        data={"sub": str(customer.id), "type": "customer"},
        expires_delta=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    
    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,
        secure=settings.ENVIRONMENT == "production",  # ✅ 환경별 분기
        samesite="strict",  # ✅ CSRF 방어 강화
        max_age=settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60,
        path="/"
    )
    
    return {"message": "Login successful", "customer_id": customer.id}

@router.patch("/me", response_model=CustomerResponse)
async def update_my_profile(
    update_data: CustomerUpdate,
    current_customer: Customer = Depends(get_current_customer),
    db: Session = Depends(get_db)
):
    """내 정보 수정"""
    if update_data.email and update_data.email != current_customer.email:
        existing_email = db.query(Customer).filter(
            Customer.email == update_data.email,
            Customer.id != current_customer.id
        ).first()
        
        if existing_email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already in use"
            )
    
    if update_data.name:
        current_customer.name = update_data.name
    if update_data.email is not None:
        current_customer.email = update_data.email
    
    # ✅ updated_at은 onupdate로 자동 처리됨 (모델에서 설정)
    db.commit()
    db.refresh(current_customer)
    
    return current_customer

@router.get('/me', response_model=CustomerResponse)
async def get_my_profile(
    current_customer: Customer = Depends(get_current_customer)
):
    """
    내 정보 조회, get_current_customer로 인증된 사용자 정보 반환
    """
    return current_customer

@router.post('/logout')
async def logout(response:Response):
    """
    로그아웃
    -쿠키에 저장된 access_token삭제
    """
    response.delete_cookie(
        key="access_token",
        path="/",
        secure=settings.ENVIRONMENT == "production",
        samesite="strict"
    )
    return {"message": "Logout successful"}


@router.post('/register', response_model=CustomerResponse, status_code=status.HTTP_201_CREATED)
async def register(
    customer_data:CustomerCreate,
    db: Session = Depends(get_db)
):
    """
    회원가입
    
    1.전화번호 중복 체크
    2. 이메일 중복 체크
    3. 비밀번호 해시 처리
    4. DB 저장
    """
    existing_phone = db.query(Customer).filter(
        Customer.phone == customer_data.phone
    ).first()

    # 핸드폰 중복 체크
    if existing_phone:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Phone number already registered"
        )
    
    if customer_data.email:
        existing_email = db.query(Customer).filter(
            Customer.email == customer_data.email
        ).first()
        
        if existing_email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )
    
    password_hash = get_password_hash(customer_data.password)

    new_customer = Customer(
        name=customer_data.name,
        phone=customer_data.phone,
        password_hash=password_hash,
        email=customer_data.email,
        is_active=True,
        is_verified=False,
    )

    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)

    return new_customer


@router.delete('/me')
async def delete_my_account(
    current_customer : Customer = Depends(get_current_customer),
    db: Session = Depends(get_db)
):
    """
    회원탈퇴

    실제 삭제가 아니라 is_active = False 처리
    """

    if not current_customer.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Account already deactivated"
        )
    
    current_customer.is_active = False

    db.commit()

    return {"message":"Account deactivated successfully"}