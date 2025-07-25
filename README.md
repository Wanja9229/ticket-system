# 전시회 티켓 예약 시스템 개발 가이드

> **프로젝트명**: 전시회 티켓 예약 시스템  
> **목표**: 고성능 다중 전시회 티켓 예약 및 관리 시스템  
> **성능 요구사항**: 동시 접속자 1만명 처리 가능  
> **작성일**: 2025.07.25  
> **버전**: v1.0

## 📋 목차

1. [프로젝트 개요](#-프로젝트-개요)
2. [기술 스택](#-기술-스택)
3. [개발 단계별 계획](#-개발-단계별-계획)
4. [시스템 아키텍처](#-시스템-아키텍처)
5. [데이터베이스 설계](#-데이터베이스-설계)
6. [API 설계](#-api-설계)
7. [프론트엔드 구조](#-프론트엔드-구조)
8. [성능 최적화 전략](#-성능-최적화-전략)
9. [개발 환경 구성](#-개발-환경-구성)
10. [배포 및 운영](#-배포-및-운영)

---

## 🎯 프로젝트 개요

### 핵심 기능
- **실시간 티켓 예약 시스템**: 고성능 동시 접속 처리
- **토스페이먼츠 결제 연동**: 안전한 카드결제 시스템
- **카카오 알림톡**: 예약 확인 및 알림 서비스
- **QR코드 현장 입장 관리**: PWA 기반 모바일 앱
- **다중 전시회 관리**: 전시회별 독립적 운영 (/aaa, /bbb)
- **관리자 대시보드**: 상품/주문/통계 관리

### 성능 목표
- **동시 접속**: 1만명/1분 처리 가능
- **응답 시간**: 평균 200ms 이하
- **가용성**: 99.9% 업타임
- **확장성**: 수평 확장 가능한 마이크로서비스 아키텍처

---

## 🛠 기술 스택

### Frontend
- **Framework**: React 18 + Next.js 14
- **Language**: JavaScript (ES6+) → TypeScript 마이그레이션 예정
- **Styling**: SCSS/CSS Modules
- **State Management**: React Query/SWR
- **PWA**: Service Worker + Web App Manifest

### Backend
- **Framework**: Python 3.12 + FastAPI
- **ORM**: SQLAlchemy
- **Validation**: Pydantic
- **Server**: Uvicorn + Gunicorn
- **Async**: asyncio/await

### Database & Cache
- **Main DB**: PostgreSQL 16+
- **Cache**: Redis 7+
- **Connection Pool**: asyncpg + aioredis

### Infrastructure
- **OS**: Ubuntu 24.04 LTS (8코어 32GB)
- **Proxy**: nginx
- **Container**: Docker + Docker Compose
- **Cloud**: AWS (예정)

### External APIs
- **Payment**: 토스페이먼츠 API
- **Notification**: 카카오 알림톡 API
- **QR**: PWA Camera API + QR Scanner

---

## 📈 개발 단계별 계획

### 1단계: 시스템 설계 & 구조 정의 ✅
- [x] 전체 시스템 아키텍처 설계
- [x] 데이터베이스 스키마 설계
- [x] API 엔드포인트 구조 설계
- [x] 프론트엔드 페이지 구조 설계
- [x] 성능 최적화 전략 수립

### 2단계: 로컬 개발환경 구축 🔄
- [ ] 프로젝트 디렉토리 구조 생성
- [ ] FastAPI 백엔드 기본 설정
- [ ] Next.js 프론트엔드 기본 설정
- [ ] Docker Compose 개발환경 구성
- [ ] 환경변수 및 설정 파일 구성

### 3단계: DB / Redis 구성
- [ ] PostgreSQL 데이터베이스 구축
- [ ] Redis 캐시 서버 구축
- [ ] 데이터베이스 스키마 적용
- [ ] 초기 데이터 및 테스트 데이터 생성
- [ ] 연결 테스트 및 검증

### 4단계: 백엔드 (FastAPI) 기능 구현
- [ ] 기본 CRUD API 구현
- [ ] 인증 및 권한 시스템
- [ ] 예약 및 재고 관리 로직
- [ ] 결제 API 연동
- [ ] 알림 시스템 구현

### 5단계: 프론트엔드 (Next.js) 화면 구성
- [ ] 기본 레이아웃 및 컴포넌트
- [ ] 예약 페이지 구현
- [ ] 결제 페이지 구현
- [ ] 관리자 대시보드
- [ ] PWA 입장 관리 앱

### 6단계: 공통 기능 추가
- [ ] 입력 검증 시스템
- [ ] 에러 핸들링 로직
- [ ] 로딩/에러/토스트 컴포넌트
- [ ] 로깅 및 모니터링
- [ ] 테스트 코드 작성

### 7단계: 예약 / 예매 / 대기열 로직 구현
- [ ] Redis 기반 대기열 시스템
- [ ] 실시간 재고 관리
- [ ] 오버셀링 방지 로직
- [ ] 임시 예약 및 타임아웃 처리
- [ ] 동시성 제어 구현

### 8단계: 테스트 & 로드 체크
- [ ] 단위 테스트 작성
- [ ] 통합 테스트 구현
- [ ] 성능 테스트 (부하 테스트)
- [ ] 보안 테스트
- [ ] 사용자 시나리오 테스트

### 9단계: 배포 및 보안 설정
- [ ] 프로덕션 환경 구성
- [ ] CI/CD 파이프라인 구축
- [ ] SSL/TLS 인증서 적용
- [ ] 방화벽 및 보안 설정
- [ ] 백업 및 모니터링 시스템

### 10단계: 운영모드 전환
- [ ] 실운영 환경 배포
- [ ] 모니터링 대시보드 구축
- [ ] 운영 매뉴얼 작성
- [ ] 장애 대응 절차 수립
- [ ] 성능 튜닝 및 최적화

---

## 🏗 시스템 아키텍처

### 전체 시스템 구조

```
┌─────────────────────────────────────────────────────────────┐
│                    사용자 인터페이스                        │
├─────────────┬─────────────┬─────────────┬─────────────────────┤
│ 예약 페이지 │ 결제 페이지 │ 확인 페이지 │ PWA 입장관리 앱     │
│ (Next.js)   │ (Next.js)   │ (Next.js)   │ (QR 스캔)           │
└─────────────┴─────────────┴─────────────┴─────────────────────┘
                              │
┌─────────────────────────────────────────────────────────────┐
│                    API Gateway (nginx)                     │
└─────────────────────────────────────────────────────────────┘
                              │
┌─────────────────────────────────────────────────────────────┐
│                  FastAPI 백엔드 서버                       │
├─────────────┬─────────────┬─────────────┬─────────────────────┤
│ 예약 API    │ 결제 API    │ 관리자 API  │ 통계 API            │
│ 재고 관리   │ 웹훅 처리   │ 상품 관리   │ 대시보드            │
└─────────────┴─────────────┴─────────────┴─────────────────────┘
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│ PostgreSQL  │    │    Redis    │    │ 외부 API    │
│ (메인 DB)   │    │ (캐시/대기열)│   │ 토스/카카오 │
└─────────────┘    └─────────────┘    └─────────────┘
```

### 컴포넌트별 역할

#### Frontend (Next.js + React)
- **사용자 인터페이스**: 반응형 웹 디자인
- **PWA 기능**: 오프라인 지원, 푸시 알림
- **QR 스캔**: 카메라 API 활용 현장 입장 관리
- **상태 관리**: React Query를 통한 서버 상태 동기화

#### Backend (FastAPI)
- **API 서버**: RESTful API 제공
- **비즈니스 로직**: 예약, 결제, 재고 관리
- **외부 연동**: 결제, 알림 API 통합
- **성능 최적화**: 비동기 처리, 커넥션 풀링

#### Database (PostgreSQL)
- **데이터 영속성**: 주문, 상품, 사용자 정보
- **트랜잭션**: ACID 특성 보장
- **관계형 데이터**: 정규화된 스키마

#### Cache (Redis)
- **세션 관리**: 사용자 대기열 상태
- **실시간 재고**: 빠른 재고 조회/차감
- **임시 데이터**: 결제 진행 중 데이터

---

## 🗄 데이터베이스 설계

### 핵심 테이블 구조

#### 1. 전시회 관리 (exhibitions)
```sql
CREATE TABLE exhibitions (
    id SERIAL PRIMARY KEY,
    code VARCHAR(50) UNIQUE NOT NULL,           -- 전시회 코드 (aaa, bbb)
    name VARCHAR(200) NOT NULL,                 -- 전시회 명
    description TEXT,                           -- 설명
    start_date DATE NOT NULL,                   -- 시작일
    end_date DATE NOT NULL,                     -- 종료일
    venue VARCHAR(200),                         -- 장소
    is_active BOOLEAN DEFAULT true,             -- 활성 상태
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);
```

#### 2. 상품 관리 (products)
```sql
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    exhibition_id INTEGER REFERENCES exhibitions(id),
    name VARCHAR(200) NOT NULL,                 -- 상품명
    type VARCHAR(50) NOT NULL,                  -- 대인/소인
    price INTEGER NOT NULL,                     -- 가격
    total_quantity INTEGER NOT NULL,            -- 총 수량
    available_quantity INTEGER NOT NULL,        -- 잔여 수량
    sale_start TIMESTAMP,                       -- 판매 시작
    sale_end TIMESTAMP,                         -- 판매 종료
    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);
```

#### 3. 주문 관리 (orders)
```sql
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    order_number VARCHAR(50) UNIQUE NOT NULL,   -- 주문번호
    exhibition_id INTEGER REFERENCES exhibitions(id),
    customer_name VARCHAR(100) NOT NULL,        -- 구매자명
    customer_phone VARCHAR(20) NOT NULL,        -- 구매자 전화번호
    customer_email VARCHAR(200),                -- 구매자 이메일
    total_amount INTEGER NOT NULL,              -- 총 금액
    payment_status VARCHAR(50) DEFAULT 'pending', -- 결제 상태
    payment_method VARCHAR(50),                 -- 결제 방법
    payment_key VARCHAR(200),                   -- 토스페이먼츠 키
    visit_date DATE,                           -- 방문 예정일
    status VARCHAR(50) DEFAULT 'reserved',      -- 주문 상태
    qr_code VARCHAR(500),                      -- QR 코드
    entrance_checked BOOLEAN DEFAULT false,     -- 입장 확인
    entrance_time TIMESTAMP,                   -- 입장 시간
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);
```

#### 4. 주문 상품 (order_items)
```sql
CREATE TABLE order_items (
    id SERIAL PRIMARY KEY,
    order_id INTEGER REFERENCES orders(id),
    product_id INTEGER REFERENCES products(id),
    quantity INTEGER NOT NULL,                  -- 수량
    unit_price INTEGER NOT NULL,               -- 단가
    total_price INTEGER NOT NULL,              -- 소계
    created_at TIMESTAMP DEFAULT NOW()
);
```

#### 5. 관리자 계정 (admin_users)
```sql
CREATE TABLE admin_users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    exhibition_id INTEGER REFERENCES exhibitions(id), -- 관리 권한 전시회
    role VARCHAR(50) DEFAULT 'admin',           -- 권한 레벨
    is_active BOOLEAN DEFAULT true,
    last_login TIMESTAMP,
    created_at TIMESTAMP DEFAULT NOW()
);
```

### 인덱스 전략
```sql
-- 성능 최적화를 위한 인덱스
CREATE INDEX idx_exhibitions_code ON exhibitions(code);
CREATE INDEX idx_products_exhibition_id ON products(exhibition_id);
CREATE INDEX idx_orders_exhibition_id ON orders(exhibition_id);
CREATE INDEX idx_orders_payment_status ON orders(payment_status);
CREATE INDEX idx_orders_created_at ON orders(created_at);
CREATE INDEX idx_order_items_order_id ON order_items(order_id);
```

---

## 🔌 API 설계

### 공통 예약 API

#### 상품 조회
```http
GET /api/exhibitions/{code}/products
Response: {
  "products": [
    {
      "id": 1,
      "name": "일반 관람권 (대인)",
      "type": "adult",
      "price": 15000,
      "available_quantity": 500
    }
  ]
}
```

#### 주문 생성
```http
POST /api/orders
Request: {
  "exhibition_code": "aaa",
  "customer_name": "홍길동",
  "customer_phone": "010-1234-5678",
  "items": [
    {
      "product_id": 1,
      "quantity": 2
    }
  ],
  "visit_date": "2025-08-01"
}
Response: {
  "order_number": "ORD20250725001",
  "total_amount": 30000,
  "payment_url": "https://..."
}
```

### 결제 API

#### 결제 초기화
```http
POST /api/payments/initialize
Request: {
  "order_number": "ORD20250725001",
  "amount": 30000,
  "customer_name": "홍길동"
}
Response: {
  "payment_key": "toss_payment_key",
  "checkout_url": "https://..."
}
```

#### 결제 확인
```http
POST /api/payments/confirm
Request: {
  "payment_key": "toss_payment_key",
  "order_id": "merchant_order_id",
  "amount": 30000
}
```

### 현장 관리 API

#### QR 코드 스캔
```http
POST /api/entrance/scan
Request: {
  "qr_code": "encoded_qr_data",
  "admin_id": 1
}
Response: {
  "order_number": "ORD20250725001",
  "customer_name": "홍길동",
  "entrance_status": "allowed",
  "message": "입장 처리되었습니다."
}
```

### 관리자 API

#### 상품 관리
```http
GET /api/admin/products              # 상품 목록
POST /api/admin/products             # 상품 등록
PUT /api/admin/products/{id}         # 상품 수정
DELETE /api/admin/products/{id}      # 상품 삭제
```

#### 주문 관리
```http
GET /api/admin/orders                # 주문 목록
GET /api/admin/orders/{id}           # 주문 상세
PATCH /api/admin/orders/{id}         # 주문 상태 변경
```

#### 대시보드
```http
GET /api/admin/dashboard
Response: {
  "total_orders": 1250,
  "total_revenue": 18750000,
  "today_orders": 45,
  "entrance_count": 1100,
  "products_sold": {
    "adult": 800,
    "child": 450
  }
}
```

---

## 🎨 프론트엔드 구조

### 디렉토리 구조
```
exhibition-frontend/
├── src/
│   ├── app/                    # Next.js App Router
│   │   ├── [exhibition]/       # 동적 라우팅
│   │   │   ├── page.js         # 예약 메인 페이지
│   │   │   ├── order/          
│   │   │   │   └── page.js     # 주문서 작성
│   │   │   ├── payment/        
│   │   │   │   └── page.js     # 결제 페이지
│   │   │   └── complete/       
│   │   │       └── page.js     # 결제 완료
│   │   ├── admin/              # 관리자 페이지
│   │   │   ├── login/page.js
│   │   │   ├── dashboard/page.js
│   │   │   ├── products/page.js
│   │   │   └── orders/page.js
│   │   └── entrance/           # PWA 입장 관리
│   │       └── page.js
│   ├── components/             # 재사용 컴포넌트
│   │   ├── common/             # 공통 컴포넌트
│   │   │   ├── Loading.js
│   │   │   ├── ErrorBoundary.js
│   │   │   ├── Toast.js
│   │   │   └── Layout.js
│   │   ├── booking/            # 예약 관련
│   │   │   ├── ProductCard.js
│   │   │   ├── QuantitySelector.js
│   │   │   ├── DatePicker.js
│   │   │   └── CartSummary.js
│   │   ├── payment/            # 결제 관련
│   │   │   ├── TossPayment.js
│   │   │   ├── PaymentForm.js
│   │   │   └── PaymentResult.js
│   │   ├── admin/              # 관리자 컴포넌트
│   │   │   ├── Dashboard.js
│   │   │   ├── ProductManager.js
│   │   │   └── OrderList.js
│   │   └── entrance/           # 입장 관리
│   │       ├── QRScanner.js
│   │       ├── EntranceCheck.js
│   │       └── ScanResult.js
│   ├── hooks/                  # 커스텀 훅
│   │   ├── useQueue.js         # 대기열 관리
│   │   ├── usePayment.js       # 결제 처리
│   │   ├── useQRScanner.js     # QR 스캔
│   │   ├── useLocalStorage.js  # 로컬 스토리지
│   │   └── useAuth.js          # 인증 관리
│   ├── services/               # API 서비스
│   │   ├── api.js              # API 클라이언트
│   │   ├── booking.js          # 예약 API
│   │   ├── payment.js          # 결제 API
│   │   ├── admin.js            # 관리자 API
│   │   └── entrance.js         # 입장 API
│   ├── utils/                  # 유틸리티
│   │   ├── constants.js        # 상수
│   │   ├── helpers.js          # 헬퍼 함수
│   │   ├── validation.js       # 검증 로직
│   │   └── formatting.js       # 포맷팅
│   └── styles/                 # SCSS 스타일
│       ├── globals.scss
│       ├── variables.scss
│       ├── mixins.scss
│       └── components/
│           ├── layout.scss
│           ├── booking.scss
│           ├── payment.scss
│           └── admin.scss
├── public/
│   ├── manifest.json           # PWA 매니페스트
│   ├── sw.js                   # 서비스 워커
│   ├── icons/                  # PWA 아이콘
│   └── images/
├── package.json
├── next.config.js
└── README.md
```

### 주요 컴포넌트 설계

#### 예약 페이지 (ProductCard.js)
```javascript
// components/booking/ProductCard.js
export default function ProductCard({ product, onAddToCart }) {
  return (
    <div className="product-card">
      <h3>{product.name}</h3>
      <div className="price">{product.price.toLocaleString()}원</div>
      <div className="quantity">
        <QuantitySelector 
          max={product.available_quantity}
          onChange={(qty) => onAddToCart(product.id, qty)}
        />
      </div>
      <div className="stock">
        잔여: {product.available_quantity}매
      </div>
    </div>
  );
}
```

#### QR 스캐너 (QRScanner.js)
```javascript
// components/entrance/QRScanner.js
import { useQRScanner } from '@/hooks/useQRScanner';

export default function QRScanner({ onScan }) {
  const { 
    isScanning, 
    startScan, 
    stopScan, 
    videoRef 
  } = useQRScanner({ onScan });

  return (
    <div className="qr-scanner">
      <video ref={videoRef} className="scanner-video" />
      <div className="scanner-overlay">
        <div className="scan-frame"></div>
      </div>
      <div className="scanner-controls">
        <button onClick={isScanning ? stopScan : startScan}>
          {isScanning ? '스캔 중지' : '스캔 시작'}
        </button>
      </div>
    </div>
  );
}
```

---

## ⚡ 성능 최적화 전략

### 동시 접속 1만명 대응

#### 1. 서버 최적화
```python
# FastAPI + Gunicorn 설정 (gunicorn.conf.py)
workers = 4                     # CPU 코어 수의 절반
worker_class = "uvicorn.workers.UvicornWorker"
worker_connections = 1000       # 워커당 연결 수
max_requests = 1000            # 워커 재시작 주기
keepalive = 5                  # 연결 유지 시간
timeout = 30                   # 요청 타임아웃
```

#### 2. nginx 로드밸런싱
```nginx
# /etc/nginx/sites-available/exhibition
upstream fastapi_backend {
    server 127.0.0.1:8001 weight=1;
    server 127.0.0.1:8002 weight=1;
    server 127.0.0.1:8003 weight=1;
    server 127.0.0.1:8004 weight=1;
}

server {
    listen 80;
    server_name exhibition.example.com;

    # 정적 파일 직접 서빙
    location /_next/static/ {
        alias /var/www/exhibition/static/;
        expires 1y;
        add_header Cache-Control "public, immutable";
    }

    # API 요청 프록시
    location /api/ {
        proxy_pass http://fastapi_backend;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_connect_timeout 30s;
        proxy_send_timeout 30s;
        proxy_read_timeout 30s;
    }

    # Next.js 애플리케이션
    location / {
        proxy_pass http://127.0.0.1:3000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

#### 3. Redis 캐시 전략
```python
# 실시간 재고 관리 (Redis Lua 스크립트)
STOCK_DECREMENT_SCRIPT = """
local key = KEYS[1]
local decrement = tonumber(ARGV[1])
local current = redis.call('GET', key)

if current and tonumber(current) >= decrement then
    local new_value = redis.call('DECRBY', key, decrement)
    return new_value
else
    return -1
end
"""

# 대기열 관리
QUEUE_POSITION_SCRIPT = """
local queue_key = KEYS[1]
local user_token = ARGV[1]

-- 사용자가 이미 대기열에 있는지 확인
local position = redis.call('LPOS', queue_key, user_token)
if position then
    return position + 1
else
    -- 대기열에 추가
    redis.call('RPUSH', queue_key, user_token)
    return redis.call('LLEN', queue_key)
end
"""
```

#### 4. 데이터베이스 최적화
```sql
-- 커넥션 풀 설정
-- postgresql.conf
max_connections = 200
shared_buffers = 8GB
effective_cache_size = 24GB
work_mem = 64MB
maintenance_work_mem = 2GB

-- 성능 모니터링 쿼리
SELECT 
    query,
    calls,
    total_time,
    mean_time,
    stddev_time,
    rows
FROM pg_stat_statements 
ORDER BY total_time DESC 
LIMIT 10;
```

### 오버셀링 방지 로직

#### 2단계 검증 시스템
```python
async def reserve_tickets(order_data: OrderCreate):
    # 1단계: Redis 빠른 재고 차감
    redis_result = await redis_decrement_stock(
        order_data.product_id, 
        order_data.quantity
    )
    
    if redis_result < 0:
        raise HTTPException(
            status_code=400, 
            detail="재고 부족"
        )
    
    try:
        # 2단계: PostgreSQL 최종 검증
        db_result = await db_reserve_tickets(order_data)
        
        if not db_result:
            # 실패 시 Redis 재고 복구
            await redis_increment_stock(
                order_data.product_id, 
                order_data.quantity
            )
            raise HTTPException(
                status_code=400, 
                detail="예약 실패"
            )
            
        return db_result
        
    except Exception as e:
        # 예외 발생 시 Redis 재고 복구
        await redis_increment_stock(
            order_data.product_id, 
            order_data.quantity
        )
        raise e
```

---

## 🖥 개발 환경 구성

### Docker Compose 구성
```yaml
# docker-compose.dev.yml
version: '3.8'

services:
  # PostgreSQL 데이터베이스
  postgres:
    image: postgres:16
    environment:
      POSTGRES_DB: exhibition_tickets
      POSTGRES_USER: exhibition_user
      POSTGRES_PASSWORD: exhibition_pass
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./backend/sql:/docker-entrypoint-initdb.d

  # Redis 캐시
  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    command: redis-server --appendonly yes
    volumes:
      - redis_data:/data

  # FastAPI 백엔드
  backend:
    build: ./backend
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://exhibition_user:exhibition_pass@postgres:5432/exhibition_tickets
      - REDIS_URL=redis://redis:6379
    depends_on:
      - postgres
      - redis
    volumes:
      - ./backend:/app
    command: uvicorn main:app --host 0.0.0.0 --port 8000 --reload

  # Next.js 프론트엔드
  frontend:
    build: ./frontend
    ports:
      - "3000:3000"
    environment:
      - NEXT_PUBLIC_API_URL=http://localhost:8000
    volumes:
      - ./frontend:/app
      - /app/node_modules
    command: npm run dev

volumes:
  postgres_data:
  redis_data:
```

### 환경변수 설정
```bash
# backend/.env
DATABASE_URL=postgresql://exhibition_user:exhibition_pass@localhost:5432/exhibition_tickets
REDIS_URL=redis://localhost:6379
SECRET_KEY=your-super-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# 토스페이먼츠 설정
TOSS_CLIENT_KEY=test_ck_your_client_key
TOSS_SECRET_KEY=test_sk_your_secret_key
TOSS_PAYMENT_URL=https://api.tosspayments.com/v1/payments

# 카카오 알림톡 설정
KAKAO_REST_API_KEY=your_kakao_rest_api_key
KAKAO_SENDER_KEY=your_sender_key

# 프론트엔드 환경변수
# frontend/.env.local
NEXT_PUBLIC_API_URL=http://localhost:8000
NEXT_PUBLIC_TOSS_CLIENT_KEY=test_ck_your_client_key
NEXT_PUBLIC_APP_ENV=development
```

### 백엔드 디렉토리 구조
```
exhibition-backend/
├── app/
│   ├── __init__.py
│   ├── main.py                 # FastAPI 앱 진입점
│   ├── config.py               # 설정 관리
│   ├── database.py             # 데이터베이스 연결
│   ├── dependencies.py         # 의존성 주입
│   ├── models/                 # SQLAlchemy 모델
│   │   ├── __init__.py
│   │   ├── exhibition.py
│   │   ├── product.py
│   │   ├── order.py
│   │   └── user.py
│   ├── schemas/                # Pydantic 스키마
│   │   ├── __init__.py
│   │   ├── exhibition.py
│   │   ├── product.py
│   │   ├── order.py
│   │   └── user.py
│   ├── crud/                   # CRUD 연산
│   │   ├── __init__.py
│   │   ├── exhibition.py
│   │   ├── product.py
│   │   ├── order.py
│   │   └── user.py
│   ├── api/                    # API 라우터
│   │   ├── __init__.py
│   │   ├── api_v1/
│   │   │   ├── __init__.py
│   │   │   ├── api.py          # 라우터 통합
│   │   │   └── endpoints/
│   │   │       ├── __init__.py
│   │   │       ├── booking.py  # 예약 API
│   │   │       ├── payment.py  # 결제 API
│   │   │       ├── entrance.py # 입장 API
│   │   │       └── admin.py    # 관리자 API
│   ├── services/               # 비즈니스 로직
│   │   ├── __init__.py
│   │   ├── booking_service.py
│   │   ├── payment_service.py
│   │   ├── queue_service.py
│   │   └── notification_service.py
│   ├── utils/                  # 유틸리티
│   │   ├── __init__.py
│   │   ├── security.py         # 보안 관련
│   │   ├── redis_client.py     # Redis 클라이언트
│   │   └── helpers.py
│   └── tests/                  # 테스트 코드
│       ├── __init__.py
│       ├── conftest.py
│       ├── test_booking.py
│       └── test_payment.py
├── sql/                        # SQL 스크립트
│   ├── 01_create_tables.sql
│   ├── 02_create_indexes.sql
│   └── 03_sample_data.sql
├── requirements.txt
├── Dockerfile
└── README.md
```

---

## 🚀 배포 및 운영

### 프로덕션 환경 구성

#### 1. 서버 사양 요구사항
```
OS: Ubuntu 24.04 LTS
CPU: 8코어 (최소 4코어)
RAM: 32GB (최소 16GB)
Storage: SSD 500GB (최소 200GB)
Network: 1Gbps
```

#### 2. 시스템 서비스 구성
```bash
# systemd 서비스 설정
# /etc/systemd/system/exhibition-backend.service
[Unit]
Description=Exhibition Ticket Backend
After=network.target postgresql.service redis.service

[Service]
Type=exec
User=exhibition
Group=exhibition
WorkingDirectory=/opt/exhibition/backend
Environment=PATH=/opt/exhibition/venv/bin
ExecStart=/opt/exhibition/venv/bin/gunicorn -c gunicorn.conf.py main:app
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

#### 3. nginx 프로덕션 설정
```nginx
# /etc/nginx/sites-available/exhibition-prod
server {
    listen 80;
    server_name exhibition.example.com;
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name exhibition.example.com;

    # SSL 인증서
    ssl_certificate /etc/letsencrypt/live/exhibition.example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/exhibition.example.com/privkey.pem;
    
    # SSL 보안 설정
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers ECDHE+AESGCM:ECDHE+CHACHA20:DHE+AESGCM:DHE+CHACHA20:!aNULL:!MD5:!DSS;
    ssl_prefer_server_ciphers off;
    
    # 보안 헤더
    add_header X-Frame-Options DENY;
    add_header X-Content-Type-Options nosniff;
    add_header X-XSS-Protection "1; mode=block";
    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;

    # 로그 설정
    access_log /var/log/nginx/exhibition-access.log;
    error_log /var/log/nginx/exhibition-error.log;

    # 업로드 크기 제한
    client_max_body_size 10M;

    # 정적 파일 서빙
    location /_next/static/ {
        alias /opt/exhibition/frontend/out/_next/static/;
        expires 1y;
        add_header Cache-Control "public, immutable";
    }

    # API 요청
    location /api/ {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        
        # 타임아웃 설정
        proxy_connect_timeout 30s;
        proxy_send_timeout 30s;
        proxy_read_timeout 30s;
        
        # 버퍼링 설정
        proxy_buffering on;
        proxy_buffer_size 4k;
        proxy_buffers 8 4k;
    }

    # Next.js 애플리케이션
    location / {
        proxy_pass http://127.0.0.1:3000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

### 모니터링 및 로깅

#### 1. Prometheus + Grafana 모니터링
```yaml
# docker-compose.monitoring.yml
version: '3.8'

services:
  prometheus:
    image: prom/prometheus:latest
    ports:
      - "9090:9090"
    volumes:
      - ./monitoring/prometheus.yml:/etc/prometheus/prometheus.yml
      - prometheus_data:/prometheus

  grafana:
    image: grafana/grafana:latest
    ports:
      - "3001:3000"
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=admin123
    volumes:
      - grafana_data:/var/lib/grafana
      - ./monitoring/grafana/dashboards:/etc/grafana/provisioning/dashboards

  redis_exporter:
    image: oliver006/redis_exporter:latest
    environment:
      - REDIS_ADDR=redis://redis:6379
    ports:
      - "9121:9121"

  postgres_exporter:
    image: wrouesnel/postgres_exporter:latest
    environment:
      - DATA_SOURCE_NAME=postgresql://exhibition_user:exhibition_pass@postgres:5432/exhibition_tickets?sslmode=disable
    ports:
      - "9187:9187"

volumes:
  prometheus_data:
  grafana_data:
```

#### 2. 로깅 설정
```python
# app/utils/logging_config.py
import logging
import json
from datetime import datetime
from typing import Any, Dict

class JSONFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        log_entry: Dict[str, Any] = {
            "timestamp": datetime.utcnow().isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
        }
        
        if hasattr(record, "user_id"):
            log_entry["user_id"] = record.user_id
        if hasattr(record, "order_number"):
            log_entry["order_number"] = record.order_number
        if hasattr(record, "exhibition_code"):
            log_entry["exhibition_code"] = record.exhibition_code
            
        return json.dumps(log_entry, ensure_ascii=False)

# 로거 설정
def setup_logging():
    formatter = JSONFormatter()
    
    # 파일 핸들러
    file_handler = logging.FileHandler("/var/log/exhibition/app.log")
    file_handler.setFormatter(formatter)
    
    # 콘솔 핸들러
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    
    # 루트 로거 설정
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger
```

### 백업 및 재해 복구

#### 1. 데이터베이스 백업
```bash
#!/bin/bash
# scripts/backup_database.sh

BACKUP_DIR="/opt/exhibition/backups"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
DB_NAME="exhibition_tickets"
DB_USER="exhibition_user"

# PostgreSQL 백업
pg_dump -U $DB_USER -h localhost $DB_NAME | gzip > $BACKUP_DIR/postgres_backup_$TIMESTAMP.sql.gz

# Redis 백업
redis-cli BGSAVE
cp /var/lib/redis/dump.rdb $BACKUP_DIR/redis_backup_$TIMESTAMP.rdb

# 7일 이상 된 백업 파일 삭제
find $BACKUP_DIR -name "*.gz" -mtime +7 -delete
find $BACKUP_DIR -name "*.rdb" -mtime +7 -delete

echo "Backup completed: $TIMESTAMP"
```

#### 2. 자동 백업 설정
```bash
# crontab 설정
# 매일 새벽 2시에 백업 실행
0 2 * * * /opt/exhibition/scripts/backup_database.sh >> /var/log/exhibition/backup.log 2>&1

# 매주 일요일 새벽 3시에 풀 백업 및 AWS S3 업로드
0 3 * * 0 /opt/exhibition/scripts/full_backup_s3.sh >> /var/log/exhibition/backup.log 2>&1
```

### 보안 설정

#### 1. 방화벽 구성
```bash
# UFW 방화벽 설정
sudo ufw default deny incoming
sudo ufw default allow outgoing

# SSH (포트 변경 권장)
sudo ufw allow 22022/tcp

# HTTP/HTTPS
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp

# 내부 서비스 (로컬호스트만)
sudo ufw allow from 127.0.0.1 to any port 5432  # PostgreSQL
sudo ufw allow from 127.0.0.1 to any port 6379  # Redis
sudo ufw allow from 127.0.0.1 to any port 8000  # FastAPI

sudo ufw enable
```

#### 2. SSL 인증서 자동 갱신
```bash
# Let's Encrypt 인증서 자동 갱신
# /etc/cron.d/certbot
0 12 * * * root test -x /usr/bin/certbot -a \! -d /run/systemd/system && perl -e 'sleep int(rand(43200))' && certbot -q renew --nginx
```

---

## 📊 성능 모니터링 지표

### 1. 시스템 지표
- **CPU 사용률**: < 70% (평상시), < 90% (피크시)
- **메모리 사용률**: < 80%
- **디스크 I/O**: < 80%
- **네트워크 대역폭**: 모니터링 필요

### 2. 애플리케이션 지표
- **응답 시간**: 95th percentile < 500ms
- **처리량**: > 1000 TPS
- **에러율**: < 0.1%
- **가용성**: > 99.9%

### 3. 비즈니스 지표
- **예약 성공률**: > 95%
- **결제 성공률**: > 98%
- **QR 스캔 성공률**: > 99%
- **사용자 만족도**: 모니터링 필요

### 4. 알림 설정
```yaml
# 알림 규칙 (alerting.yml)
groups:
  - name: exhibition.rules
    rules:
      - alert: HighErrorRate
        expr: rate(http_requests_total{status=~"5.."}[5m]) > 0.1
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: "High error rate detected"

      - alert: DatabaseConnectionFailed
        expr: up{job="postgres"} == 0
        for: 1m
        labels:
          severity: critical
        annotations:
          summary: "Database connection failed"

      - alert: RedisConnectionFailed
        expr: up{job="redis"} == 0
        for: 1m
        labels:
          severity: warning
        annotations:
          summary: "Redis connection failed"
```

---

## 🧪 테스트 전략

### 1. 단위 테스트
```python
# tests/test_booking_service.py
import pytest
from app.services.booking_service import BookingService
from app.schemas.order import OrderCreate

@pytest.mark.asyncio
async def test_reserve_tickets_success():
    # Given
    order_data = OrderCreate(
        exhibition_code="aaa",
        customer_name="홍길동",
        customer_phone="010-1234-5678",
        items=[{"product_id": 1, "quantity": 2}]
    )
    
    # When
    result = await BookingService.reserve_tickets(order_data)
    
    # Then
    assert result.status == "reserved"
    assert result.total_amount > 0
```

### 2. 통합 테스트
```python
# tests/test_api_integration.py
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_booking_flow():
    # 1. 상품 조회
    response = client.get("/api/exhibitions/aaa/products")
    assert response.status_code == 200
    products = response.json()["products"]
    
    # 2. 주문 생성
    order_data = {
        "exhibition_code": "aaa",
        "customer_name": "홍길동",
        "customer_phone": "010-1234-5678",
        "items": [{"product_id": products[0]["id"], "quantity": 2}]
    }
    response = client.post("/api/orders", json=order_data)
    assert response.status_code == 201
    order = response.json()
    
    # 3. 주문 조회
    response = client.get(f"/api/orders/{order['order_number']}")
    assert response.status_code == 200
```

### 3. 부하 테스트
```python
# load_test.py (locust 사용)
from locust import HttpUser, task, between

class ExhibitionUser(HttpUser):
    wait_time = between(1, 3)
    
    def on_start(self):
        # 사용자 초기화
        pass
    
    @task(3)
    def view_products(self):
        self.client.get("/api/exhibitions/aaa/products")
    
    @task(1)
    def make_reservation(self):
        order_data = {
            "exhibition_code": "aaa",
            "customer_name": "홍길동",
            "customer_phone": "010-1234-5678",
            "items": [{"product_id": 1, "quantity": 1}]
        }
        self.client.post("/api/orders", json=order_data)

# 실행: locust -f load_test.py --host=http://localhost:8000
```

---

## 📝 운영 매뉴얼

### 1. 일상 운영 체크리스트

#### 매일 확인사항
- [ ] 시스템 상태 확인 (CPU, 메모리, 디스크)
- [ ] 애플리케이션 로그 확인
- [ ] 결제 처리 상태 확인
- [ ] 백업 완료 여부 확인
- [ ] 모니터링 알림 확인

#### 주간 확인사항
- [ ] 성능 지표 리뷰
- [ ] 보안 로그 분석
- [ ] 데이터베이스 성능 최적화
- [ ] 장애 대응 리뷰

### 2. 장애 대응 절차

#### 서비스 다운 시
1. **즉시 대응**: 서비스 재시작 시도
2. **원인 파악**: 로그 분석 및 시스템 상태 확인
3. **임시 조치**: 우회 경로 또는 백업 서버 활성화
4. **복구 작업**: 근본 원인 해결
5. **사후 분석**: 장애 보고서 작성 및 개선 방안 도출

#### 성능 저하 시
1. **현상 확인**: 응답 시간 및 처리량 측정
2. **병목 지점 파악**: DB, Redis, API 서버 상태 확인
3. **즉시 조치**: 캐시 최적화, 쿼리 튜닝
4. **장기 조치**: 인프라 확장 또는 코드 최적화

### 3. 비상 연락처
```
개발팀 리더: 010-XXXX-XXXX
시스템 관리자: 010-YYYY-YYYY
인프라 담당자: 010-ZZZZ-ZZZZ
```

---

## 📚 참고 자료

### 기술 문서
- [FastAPI 공식 문서](https://fastapi.tiangolo.com/)
- [Next.js 공식 문서](https://nextjs.org/docs)
- [PostgreSQL 성능 튜닝 가이드](https://wiki.postgresql.org/wiki/Performance_Optimization)
- [Redis 최적화 가이드](https://redis.io/docs/manual/optimization/)

### API 문서
- [토스페이먼츠 API 문서](https://docs.tosspayments.com/)
- [카카오 알림톡 API 문서](https://developers.kakao.com/docs/latest/ko/alimtalk/common)

### 모니터링 도구
- [Grafana 대시보드 설정](https://grafana.com/docs/)
- [Prometheus 메트릭 수집](https://prometheus.io/docs/)

---

## 📄 라이선스 및 저작권

본 문서는 전시회 티켓 예약 시스템 개발을 위한 내부 가이드 문서입니다.

**작성일**: 2025.07.25  
**최종 수정**: 2025.07.25  
**문서 버전**: 1.0  
**작성자**: 개발팀
