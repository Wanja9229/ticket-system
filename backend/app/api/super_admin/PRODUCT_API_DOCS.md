# Product CRUD API Documentation

## Overview
이 문서는 Product와 ProductOption에 대한 CRUD API를 설명합니다.

## Base URL
- Super Admin: `/api/super-admin/products`

## Authentication
모든 API는 Super Admin 권한이 필요합니다.
- Header: `Authorization: Bearer <jwt_token>`

## API Endpoints

### 1. 상품 목록 조회
```
GET /api/super-admin/products/
```

**Query Parameters:**
- `page`: 페이지 번호 (default: 1)
- `size`: 페이지 크기 (default: 10, max: 100)
- `event_id`: 이벤트ID 필터
- `search`: 상품명 검색어
- `is_active`: 활성화 상태 필터 (true/false)
- `has_stock`: 재고 있는 상품만 (true/false)

### 2. 상품 생성
```
POST /api/super-admin/products/
```

**Request Body:**
```json
{
  "event_id": 1,
  "name": "VIP 티켓",
  "description": "프리미엄 VIP 티켓입니다",
  "base_price": 50000.00,
  "base_stock": 100,
  "is_active": true,
  "options": [
    {
      "option_name": "조조 할인",
      "price_adjustment": -5000.00,
      "stock_quantity": 50,
      "is_active": true
    }
  ]
}
```

### 3. 상품 상세 조회
```
GET /api/super-admin/products/{product_id}
```

### 4. 상품 수정
```
PUT /api/super-admin/products/{product_id}
```

### 5. 상품 삭제
```
DELETE /api/super-admin/products/{product_id}
```

### 6. 재고 조정
```
PATCH /api/super-admin/products/{product_id}/stock
```

**Request Body:**
```json
{
  "quantity": -5,
  "reason": "판매로 인한 재고 차감"
}
```

### 7. 가격 계산
```
GET /api/super-admin/products/{product_id}/price?option_id=1
```

## Product Option APIs

### 1. 옵션 생성
```
POST /api/super-admin/products/{product_id}/options
```

### 2. 옵션 수정
```
PUT /api/super-admin/products/options/{option_id}
```

### 3. 옵션 삭제
```
DELETE /api/super-admin/products/options/{option_id}
```

### 4. 옵션 재고 조정
```
PATCH /api/super-admin/products/options/stock
```

## 통계 APIs

### 1. 상품 통계 요약
```
GET /api/super-admin/products/stats/summary?event_id=1
```

### 2. 재고 부족 상품
```
GET /api/super-admin/products/low-stock?threshold=5&event_id=1
```

## 실무적 특징

1. **소프트 삭제**: 주문이 있는 상품은 비활성화만, 없는 상품은 소프트 삭제
2. **재고 관리**: 기본재고(base_stock)와 현재재고(current_stock) 분리 관리
3. **옵션 가격**: base_price + price_adjustment로 최종 가격 계산
4. **중복 체크**: 같은 이벤트 내 상품명 중복 방지
5. **권한 체크**: Super Admin만 모든 상품 관리 가능
6. **페이지네이션**: 대용량 데이터 처리를 위한 페이징
7. **필터링**: 다양한 조건으로 상품 검색 가능
8. **통계 기능**: 대시보드용 통계 데이터 제공

## Error Handling

- `400 Bad Request`: 잘못된 요청 데이터
- `404 Not Found`: 리소스를 찾을 수 없음
- `500 Internal Server Error`: 서버 내부 오류

모든 에러는 다음 형식으로 응답:
```json
{
  "detail": "에러 메시지"
}
```
