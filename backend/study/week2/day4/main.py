"""
Week 2 - Day 4: 실제 프로젝트 스타일의 API

스키마를 활용한 체계적인 API 구성
"""

from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel, Field, validator
from typing import Optional, List
from datetime import datetime, date
from enum import Enum

app = FastAPI(
    title="티켓 예약 시스템",
    description="전시회 티켓 예약 API",
    version="1.0.0"
)

# === 스키마 정의 ===

class TicketType(str, Enum):
    """티켓 종류"""
    ADULT = "adult"
    CHILD = "child"
    SENIOR = "senior"
    GROUP = "group"

class OrderStatus(str, Enum):
    """주문 상태"""
    PENDING = "pending"
    PAID = "paid"
    CANCELLED = "cancelled"
    REFUNDED = "refunded"

# 기본 스키마
class TicketBase(BaseModel):
    """티켓 기본 정보"""
    ticket_type: TicketType
    price: float = Field(..., gt=0, description="티켓 가격")
    
    @validator('price')
    def validate_price_by_type(cls, v, values):
        """티켓 종류별 가격 검증"""
        if 'ticket_type' in values:
            if values['ticket_type'] == TicketType.CHILD and v > 30000:
                raise ValueError('어린이 티켓은 30,000원을 초과할 수 없습니다')
        return v

# 요청 스키마
class OrderCreate(BaseModel):
    """주문 생성 요청"""
    event_id: int = Field(..., description="이벤트 ID")
    customer_name: str = Field(..., min_length=2, max_length=50)
    customer_email: str = Field(..., regex=r'^[\w\.-]+@[\w\.-]+\.\w+$')
    customer_phone: str = Field(..., regex=r'^01[0-9]-?[0-9]{3,4}-?[0-9]{4}$')
    visit_date: date
    tickets: List[TicketBase] = Field(..., min_items=1, max_items=10)
    
    @validator('visit_date')
    def validate_visit_date(cls, v):
        """방문일 검증"""
        if v < date.today():
            raise ValueError('방문일은 오늘 이후여야 합니다')
        return v
    
    @validator('tickets')
    def validate_ticket_count(cls, v):
        """티켓 수량 검증"""
        adult_count = sum(1 for t in v if t.ticket_type == TicketType.ADULT)
        child_count = sum(1 for t in v if t.ticket_type == TicketType.CHILD)
        
        if child_count > 0 and adult_count == 0:
            raise ValueError('어린이 티켓은 성인 동반 시에만 구매 가능합니다')
        
        if child_count > adult_count * 2:
            raise ValueError('성인 1명당 어린이는 최대 2명까지 가능합니다')
        
        return v

class PaymentInfo(BaseModel):
    """결제 정보"""
    method: str = Field(..., regex='^(card|bank|kakao|naver)$')
    amount: float = Field(..., gt=0)
    
    class Config:
        schema_extra = {
            "example": {
                "method": "card",
                "amount": 50000
            }
        }

# 응답 스키마
class TicketResponse(BaseModel):
    """티켓 응답"""
    id: int
    ticket_number: str
    ticket_type: TicketType
    price: float
    qr_code: str

class OrderResponse(BaseModel):
    """주문 응답"""
    id: int
    order_number: str
    event_id: int
    customer_name: str
    customer_email: str
    visit_date: date
    total_amount: float
    status: OrderStatus
    tickets: List[TicketResponse]
    created_at: datetime
    
    class Config:
        from_attributes = True

class OrderSummary(BaseModel):
    """주문 요약"""
    order_number: str
    total_amount: float
    ticket_count: int
    status: OrderStatus

# === 의존성 주입 ===

def get_event_or_404(event_id: int):
    """이벤트 존재 확인"""
    # 실제로는 DB에서 조회
    if event_id not in [1, 2, 3]:  # 가짜 데이터
        raise HTTPException(
            status_code=404,
            detail=f"이벤트 {event_id}를 찾을 수 없습니다"
        )
    return {"id": event_id, "name": f"이벤트 {event_id}"}

# === API 엔드포인트 ===

@app.post(
    "/orders/",
    response_model=OrderResponse,
    status_code=status.HTTP_201_CREATED,
    summary="주문 생성",
    description="새로운 티켓 주문을 생성합니다"
)
async def create_order(
    order: OrderCreate,
    event: dict = Depends(get_event_or_404)
):
    """
    티켓 주문 생성
    
    - 이벤트가 존재해야 함
    - 방문일은 미래여야 함
    - 어린이는 성인 동반 필수
    """
    # 총액 계산
    total_amount = sum(ticket.price for ticket in order.tickets)
    
    # 주문 생성 (실제로는 DB 저장)
    order_response = OrderResponse(
        id=1,
        order_number=f"ORD{datetime.now().strftime('%Y%m%d%H%M%S')}",
        event_id=order.event_id,
        customer_name=order.customer_name,
        customer_email=order.customer_email,
        visit_date=order.visit_date,
        total_amount=total_amount,
        status=OrderStatus.PENDING,
        tickets=[
            TicketResponse(
                id=i,
                ticket_number=f"TKT{i:06d}",
                ticket_type=ticket.ticket_type,
                price=ticket.price,
                qr_code=f"QR-{i:06d}"
            )
            for i, ticket in enumerate(order.tickets, 1)
        ],
        created_at=datetime.now()
    )
    
    return order_response

@app.get(
    "/orders/{order_number}",
    response_model=OrderResponse,
    responses={
        404: {"description": "주문을 찾을 수 없음"},
        403: {"description": "접근 권한 없음"}
    }
)
async def get_order(order_number: str):
    """주문 조회"""
    # 실제로는 DB에서 조회
    if not order_number.startswith("ORD"):
        raise HTTPException(
            status_code=400,
            detail="잘못된 주문번호 형식입니다"
        )
    
    # 가짜 응답
    return OrderResponse(
        id=1,
        order_number=order_number,
        event_id=1,
        customer_name="홍길동",
        customer_email="hong@example.com",
        visit_date=date.today(),
        total_amount=50000,
        status=OrderStatus.PAID,
        tickets=[
            TicketResponse(
                id=1,
                ticket_number="TKT000001",
                ticket_type=TicketType.ADULT,
                price=50000,
                qr_code="QR-000001"
            )
        ],
        created_at=datetime.now()
    )

@app.post("/orders/{order_number}/payment")
async def process_payment(
    order_number: str,
    payment: PaymentInfo
):
    """결제 처리"""
    # 결제 검증
    if payment.amount < 1000:
        raise HTTPException(
            status_code=400,
            detail="최소 결제 금액은 1,000원입니다"
        )
    
    # 결제 처리 (실제로는 PG사 연동)
    return {
        "success": True,
        "order_number": order_number,
        "payment_id": f"PAY{datetime.now().strftime('%Y%m%d%H%M%S')}",
        "amount": payment.amount,
        "method": payment.method,
        "paid_at": datetime.now()
    }

@app.get(
    "/orders/",
    response_model=List[OrderSummary],
    summary="주문 목록"
)
async def list_orders(
    status: Optional[OrderStatus] = None,
    date_from: Optional[date] = None,
    date_to: Optional[date] = None,
    skip: int = Field(0, ge=0),
    limit: int = Field(10, ge=1, le=100)
):
    """
    주문 목록 조회
    
    필터 옵션:
    - status: 주문 상태
    - date_from/date_to: 날짜 범위
    """
    # 가짜 데이터
    orders = [
        OrderSummary(
            order_number=f"ORD2024010100{i}",
            total_amount=50000 * i,
            ticket_count=i,
            status=OrderStatus.PAID
        )
        for i in range(1, 6)
    ]
    
    return orders[skip:skip + limit]

# === 통계 API ===

class DailySales(BaseModel):
    """일별 매출"""
    date: date
    order_count: int
    ticket_count: int
    total_amount: float

@app.get("/statistics/daily-sales")
async def get_daily_sales(
    start_date: date,
    end_date: date
) -> List[DailySales]:
    """일별 매출 통계"""
    if start_date > end_date:
        raise HTTPException(
            status_code=400,
            detail="시작일은 종료일보다 이전이어야 합니다"
        )
    
    # 가짜 데이터
    return [
        DailySales(
            date=start_date,
            order_count=10,
            ticket_count=25,
            total_amount=1250000
        )
    ]

if __name__ == "__main__":
    print("""
    실전 스타일 API 예제
    
    구현된 기능:
    1. 체계적인 스키마 구조
    2. 비즈니스 로직 검증
    3. 의존성 주입
    4. 에러 응답 정의
    5. API 문서화
    
    테스트 시나리오:
    1. 주문 생성 (어린이만 구매 시도 -> 에러)
    2. 주문 조회
    3. 결제 처리
    4. 주문 목록
    5. 통계 조회
    
    Swagger UI: http://localhost:8000/docs
    """)
