# 전시회 티켓 예약 시스템 - 프로젝트 개요 및 개발환경

> **프로젝트명**: 전시회 티켓 예약 시스템  
> **목표**: 고성능 다중 전시회 티켓 예약 및 관리 시스템  
> **성능 요구사항**: 동시 접속자 1만명 처리 가능  
> **작성일**: 2025.07.25  
> **버전**: v2.0 (다중 전시회 관리 플로우 보완)

## 📋 목차

1. [프로젝트 개요](#-프로젝트-개요)
2. [다중 전시회 관리 시스템 플로우](#-다중-전시회-관리-시스템-플로우)
3. [기술 스택](#-기술-스택)
4. [개발 단계별 계획](#-개발-단계별-계획)
5. [시스템 아키텍처](#-시스템-아키텍처)
6. [개발 환경 구성](#-개발-환경-구성)
7. [문서 구조](#-문서-구조)

---

## 🎯 프로젝트 개요

### 📌 시스템 개요
전시회 티켓 예약 시스템은 **고성능 다중 전시회 관리**를 위한 풀스택 웹 애플리케이션입니다. 슈퍼 관리자가 전시회를 생성하고 담당자를 배정하면, 각 담당자가 독립적으로 자신의 전시회를 관리할 수 있는 **멀티 테넌트 아키텍처**를 제공합니다.

### 🎪 핵심 기능

#### 사용자 기능
- **실시간 티켓 예약 시스템**: 동시 접속자 1만명 처리 가능
- **토스페이먼츠 결제 연동**: 안전한 카드결제 시스템  
- **카카오 알림톡**: 예약 확인 및 알림 서비스
- **QR코드 현장 입장 관리**: PWA 기반 모바일 앱
- **다중 전시회 지원**: URL 경로별 독립 운영 (/aaa, /bbb, /ccc)

#### 관리자 기능 🆕
- **슈퍼 관리자 시스템**: 전시회 생성, 담당자 관리, 전체 통계
- **전시회 담당자 시스템**: 상품 관리, 주문 관리, 입장 관리
- **권한 레벨 관리**: 1~9 단계 권한 체계
- **활동 로그 추적**: 모든 관리자 활동 기록
- **대시보드**: 실시간 통계 및 분석

### 🚀 성능 목표
- **동시 접속**: 1만명/1분 처리 가능
- **응답 시간**: 평균 200ms 이하  
- **가용성**: 99.9% 업타임
- **확장성**: 수평 확장 가능한 마이크로서비스 아키텍처

---

## 🏢 다중 전시회 관리 시스템 플로우

### 🔄 전체 관리 플로우

```mermaid
graph TB
    %% 사용자 진입점
    User[👤 사용자] --> WebSite[🌐 웹사이트 접속<br/>domain.com/aaa]
    Admin[👨‍💼 관리자] --> AdminPanel[🔧 관리자 패널<br/>domain.com/admin]
    Staff[👩‍💼 현장직원] --> PWAApp[📱 PWA 스캐너 앱<br/>domain.com/scanner]

    %% 웹사이트 흐름
    WebSite --> TicketCheck{전시회 코드<br/>유효성 검사}
    TicketCheck -->|유효| TicketHome[🎨 전시회 홈페이지]
    TicketCheck -->|무효| ErrorPage[❌ 404 에러]
    
    TicketHome --> TicketSelect[🎫 티켓 선택<br/>- 성인/청소년/어린이<br/>- 수량 선택<br/>- 입장일자 선택]
    
    TicketSelect --> CustomerInfo[📝 고객정보 입력<br/>- 이름<br/>- 연락처<br/>- 이메일]
    
    CustomerInfo --> StockCheck{재고 확인<br/>Redis}
    StockCheck -->|재고 부족| StockError[❌ 재고 부족 안내]
    StockCheck -->|재고 충분| StockReserve[🔒 재고 임시 예약<br/>Redis Lock]
    
    StockReserve --> PaymentPage[💳 결제 페이지<br/>토스페이먼츠]
    
    PaymentPage --> PaymentProcess{결제 처리}
    PaymentProcess -->|성공| PaymentSuccess[✅ 결제 완료]
    PaymentProcess -->|실패| PaymentFail[❌ 결제 실패]
    PaymentProcess -->|취소| PaymentCancel[🚫 결제 취소]
    
    PaymentFail --> StockRelease1[🔓 재고 해제]
    PaymentCancel --> StockRelease2[🔓 재고 해제]
    
    PaymentSuccess --> OrderCreate[📋 주문 생성<br/>PostgreSQL]
    OrderCreate --> QRGenerate[🔲 QR코드 생성]
    QRGenerate --> KakaoSend[📲 카카오 알림톡 발송]
    KakaoSend --> OrderComplete[✅ 예약 완료]

    %% 관리자 패널 흐름
    AdminPanel --> AdminLogin{관리자 로그인}
    AdminLogin -->|실패| AdminLoginFail[❌ 로그인 실패]
    AdminLogin -->|성공| AdminDashboard[📊 관리자 대시보드]
    
    AdminDashboard --> AdminMenus{관리 메뉴}
    AdminMenus --> ProductMgmt[🎫 상품 관리<br/>- 티켓 종류 등록<br/>- 가격 설정<br/>- 재고 관리]
    AdminMenus --> OrderMgmt[📋 주문 관리<br/>- 주문 내역 조회<br/>- 환불 처리<br/>- 고객 정보]
    AdminMenus --> StatsMgmt[📈 통계 관리<br/>- 매출 통계<br/>- 입장 통계<br/>- 실시간 현황]
    AdminMenus --> InvitationMgmt[🎟️ 초대권 관리<br/>- 업체별 초대권 발급<br/>- 사용 현황 추적]
    
    ProductMgmt --> RedisSync1[🔄 Redis 재고 동기화]
    OrderMgmt --> DBUpdate1[💾 DB 업데이트]
    
    %% PWA 스캐너 앱 흐름
    PWAApp --> PWALogin{현장직원 로그인}
    PWALogin -->|실패| PWALoginFail[❌ 로그인 실패]
    PWALogin -->|성공| PWAScanner[📷 QR 스캐너]
    
    PWAScanner --> QRScan[📸 QR코드 스캔]
    QRScan --> QRValidate{QR 유효성 검증}
    QRValidate -->|무효| QRInvalid[❌ 무효한 QR코드]
    QRValidate -->|이미 사용| QRUsed[⚠️ 이미 입장한 티켓]
    QRValidate -->|유효| QRValid[✅ 유효한 티켓]
    
    QRValid --> EntryConfirm[🚪 입장 확인<br/>- 고객 정보 표시<br/>- 입장 버튼]
    EntryConfirm --> EntryProcess{입장 처리}
    EntryProcess -->|확인| EntrySuccess[✅ 입장 완료<br/>DB 플래그 업데이트]
    EntryProcess -->|취소| EntryCanceled[🚫 입장 취소]
    
    EntrySuccess --> EntryLog[📝 입장 로그 기록]
    EntrySuccess --> PWAScanner

    %% 초대권 시스템 흐름
    InvitationMgmt --> InviteCreate[📧 초대권 생성<br/>- 업체명 입력<br/>- 수량 설정]
    InviteCreate --> InviteLink[🔗 초대 링크 생성]
    InviteLink --> InviteSend[📤 업체에 링크 전송]
    
    InviteSend --> InviteAccess[🎟️ 업체 직원이<br/>초대 링크 접속]
    InviteAccess --> InviteForm[📝 초대권 신청서<br/>- 직원 연락처 입력]
    InviteForm --> InviteQR[🔲 초대권 QR 생성]
    InviteQR --> InviteKakao[📲 초대권 카카오톡 발송]

    %% 시스템 백그라운드 프로세스
    subgraph Background[🔄 백그라운드 프로세스]
        StockSync[⏰ 재고 동기화<br/>Redis ↔ PostgreSQL]
        PaymentWebhook[🔔 결제 웹훅 처리<br/>토스페이먼츠]
        LogRotation[📁 로그 순환]
        StatsUpdate[📊 통계 업데이트]
        CacheUpdate[🗄️ 캐시 갱신]
    end

    %% 데이터베이스 연결
    subgraph Database[💾 데이터 저장소]
        PostgreSQL[(🐘 PostgreSQL<br/>- 주문 데이터<br/>- 고객 정보<br/>- 상품 정보<br/>- 관리자 계정)]
        Redis[(🔴 Redis<br/>- 실시간 재고<br/>- 세션 관리<br/>- 캐시<br/>- 대기열)]
    end

    %% 외부 API 연결
    subgraph ExternalAPI[🌐 외부 API]
        TossAPI[💳 토스페이먼츠 API]
        KakaoAPI[📱 카카오 알림톡 API]
    end

    %% 데이터 흐름 연결
    OrderCreate --> PostgreSQL
    StockReserve --> Redis
    PaymentProcess --> TossAPI
    KakaoSend --> KakaoAPI
    QRValidate --> PostgreSQL
    EntrySuccess --> PostgreSQL

    %% 스타일링
    classDef userClass fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    classDef adminClass fill:#f3e5f5,stroke:#4a148c,stroke-width:2px
    classDef processClass fill:#e8f5e8,stroke:#1b5e20,stroke-width:2px
    classDef errorClass fill:#ffebee,stroke:#b71c1c,stroke-width:2px
    classDef successClass fill:#e8f5e8,stroke:#2e7d32,stroke-width:2px
    classDef dbClass fill:#fff3e0,stroke:#e65100,stroke-width:3px
    classDef apiClass fill:#fce4ec,stroke:#880e4f,stroke-width:2px

    class User,WebSite,TicketHome,TicketSelect,CustomerInfo,PaymentPage userClass
    class Admin,AdminPanel,AdminDashboard,ProductMgmt,OrderMgmt,StatsMgmt adminClass
    class Staff,PWAApp,PWAScanner,QRScan,EntryConfirm processClass
    class ErrorPage,StockError,PaymentFail,PaymentCancel errorClass
    class PaymentSuccess,OrderComplete,EntrySuccess,QRValid successClass
    class PostgreSQL,Redis dbClass
    class TossAPI,KakaoAPI apiClass
```

### 👥 사용자 역할 정의

#### 슈퍼 관리자 (Super Admin, Level 9)
```
권한:
✅ 전시회 생성/수정/삭제
✅ 모든 전시회 담당자 관리
✅ 전체 시스템 통계 조회
✅ 시스템 설정 관리
✅ 모든 전시회 데이터 접근

접근 URL:
- /super-admin/dashboard
- /super-admin/tickets  
- /super-admin/managers
- /super-admin/statistics
```

#### 전시회 담당자 (Manager, Level 3)
```
권한:
✅ 자신이 담당하는 전시회만 관리
✅ 상품 등록/수정/삭제
✅ 주문내역 조회/관리
✅ 입장 관리 (QR 스캔)
✅ 전시회별 통계 조회
❌ 다른 전시회 데이터 접근 불가

접근 URL:
- /admin/dashboard
- /admin/products
- /admin/orders
- /admin/entrance
```

#### 일반 관리자 (Staff, Level 2)
```
권한:
✅ 상품 등록/수정만 가능
✅ 주문내역 조회만 가능
❌ 삭제 권한 없음
❌ 통계 접근 제한

접근 URL:
- /admin/products (읽기/쓰기)
- /admin/orders (읽기 전용)
```

#### 조회 전용 (Viewer, Level 1)
```
권한:
✅ 통계 및 주문내역 조회만 가능
❌ 수정/삭제 권한 없음

접근 URL:
- /admin/dashboard (읽기 전용)
- /admin/orders (읽기 전용)
```

### 🎫 전시회별 독립 운영 구조

```
도메인: ticket.example.com

전시회 A: /aaa/
전시회 B: /bbb/  
전시회 C: /ccc/

각 전시회마다:
- 독립적인 URL 경로
- 독립적인 상품 관리
- 독립적인 주문 관리
- 독립적인 통계
- 독립적인 담당자 권한
```

---

## 🛠 기술 스택

### Frontend 기술
- **Framework**: React 18 + Next.js 14
- **Language**: JavaScript (ES6+)
- **Styling**: SCSS/CSS Modules (Tailwind CSS 대신)
- **State Management**: React Query/SWR
- **PWA**: Service Worker + Web App Manifest + Workbox
- **QR Scanner**: PWA Camera API + QR Scanner 라이브러리
- **Authentication**: JWT + 권한 기반 라우팅

### Backend 기술
- **Framework**: Python 3.12 + FastAPI
- **ORM**: SQLAlchemy (비동기 지원)
- **Validation**: Pydantic
- **Server**: Uvicorn + Gunicorn (멀티워커)
- **Async**: asyncio/await 패턴
- **Authentication**: JWT + 권한 미들웨어

### Database & Cache
- **Main DB**: PostgreSQL 16+
- **Cache**: Redis 7+
- **Connection Pool**: asyncpg + aioredis
- **Migration**: Alembic

### Infrastructure
- **OS**: Ubuntu 24.04 LTS (8코어 32GB)
- **Proxy**: nginx (로드밸런싱)
- **Deployment**: Native 설치 (Docker 미사용)
- **Cloud**: AWS (향후 계획)

### External APIs
- **Payment**: 토스페이먼츠 API v1
- **Notification**: 카카오 알림톡 API
- **QR**: PWA Camera API + QR Scanner

### Development Tools
- **Code Editor**: VS Code
- **API Testing**: Postman
- **DB Management**: Dbeaver
- **Redis Management**: RedisInsight
- **Version Control**: Git

---

## 📈 개발 단계별 계획

### 1단계: 시스템 설계 & 구조 정의 ✅
- [ ] 전체 시스템 아키텍처 설계
- [ ] **다중 전시회 관리 플로우 설계** 🆕
- [ ] **권한 기반 접근 제어 시스템 설계** 🆕  
- [ ] 데이터베이스 스키마 설계 (권한 테이블 포함)
- [ ] API 엔드포인트 구조 설계
- [ ] 프론트엔드 페이지 구조 설계 (관리자 페이지 포함)
- [ ] 성능 최적화 전략 수립

### 2단계: 로컬 개발환경 구축 🔄
- [ ] 프로젝트 디렉토리 구조 생성
- [ ] **슈퍼 관리자 및 담당자 시스템 구조 생성** 🆕
- [ ] FastAPI 백엔드 기본 설정 (Native 환경)
- [ ] Next.js 프론트엔드 기본 설정 (Native 환경)
- [ ] PostgreSQL + Redis Native 설치
- [ ] **권한 기반 미들웨어 기본 구현** 🆕
- [ ] 환경변수 및 설정 파일 구성

### 3단계: DB / Redis 구성 및 권한 시스템 ⭐
- [ ] PostgreSQL 데이터베이스 구축
- [ ] **다중 관리자 테이블 스키마 적용** 🆕
- [ ] Redis 캐시 서버 구축
- [ ] **권한 기반 데이터 접근 로직 구현** 🆕
- [ ] 초기 데이터 및 테스트 데이터 생성
- [ ] **슈퍼 관리자 계정 초기 생성** 🆕
- [ ] 연결 테스트 및 검증

### 4단계: 백엔드 (FastAPI) 기능 구현 ⭐
- [ ] **권한 기반 인증 시스템 구현** 🆕
- [ ] **슈퍼 관리자 API 구현** 🆕
- [ ] **전시회 담당자 API 구현** 🆕
- [ ] 기본 CRUD API 구현
- [ ] 예약 및 재고 관리 로직
- [ ] 결제 API 연동
- [ ] 알림 시스템 구현
- [ ] **활동 로그 시스템 구현** 🆕

### 5단계: 프론트엔드 (Next.js) 화면 구성 ⭐
- [ ] **권한 기반 라우팅 시스템 구현** 🆕
- [ ] **슈퍼 관리자 대시보드 구현** 🆕
- [ ] **전시회 담당자 대시보드 구현** 🆕
- [ ] 기본 레이아웃 및 컴포넌트
- [ ] 예약 페이지 구현
- [ ] 결제 페이지 구현
- [ ] PWA 입장 관리 앱

### 6단계: 다중 전시회 관리 기능 완성 🆕
- [ ] **전시회 생성/수정/삭제 기능**
- [ ] **담당자 계정 생성 및 권한 관리**
- [ ] **전시회별 독립 상품 관리**
- [ ] **전시회별 독립 주문 관리**
- [ ] **전시회별 통계 및 분석**
- [ ] **활동 로그 대시보드**

### 7단계: 공통 기능 추가
- [ ] 입력 검증 시스템
- [ ] 에러 핸들링 로직
- [ ] 로딩/에러/토스트 컴포넌트
- [ ] 로깅 및 모니터링
- [ ] **권한별 메뉴 제어** 🆕
- [ ] 테스트 코드 작성

### 8단계: 예약 / 예매 / 대기열 로직 구현
- [ ] Redis 기반 대기열 시스템
- [ ] 실시간 재고 관리
- [ ] 오버셀링 방지 로직
- [ ] 임시 예약 및 타임아웃 처리
- [ ] 동시성 제어 구현

### 9단계: 테스트 & 로드 체크
- [ ] 단위 테스트 작성
- [ ] 통합 테스트 구현
- [ ] **권한 시스템 테스트** 🆕
- [ ] 성능 테스트 (부하 테스트)
- [ ] 보안 테스트
- [ ] 사용자 시나리오 테스트

### 10단계: 배포 및 보안 설정
- [ ] 프로덕션 환경 구성
- [ ] CI/CD 파이프라인 구축
- [ ] SSL/TLS 인증서 적용
- [ ] 방화벽 및 보안 설정
- [ ] **권한 기반 보안 정책 적용** 🆕
- [ ] 백업 및 모니터링 시스템

### 11단계: 운영모드 전환
- [ ] 실운영 환경 배포
- [ ] 모니터링 대시보드 구축
- [ ] **관리자별 운영 매뉴얼 작성** 🆕
- [ ] 장애 대응 절차 수립
- [ ] 성능 튜닝 및 최적화

---

## 🏗 시스템 아키텍처

### 전체 시스템 구조 (다중 관리자 지원)

```
┌─────────────────────────────────────────────────────────────┐
│                    사용자 인터페이스                        │
├─────────────┬─────────────┬─────────────┬─────────────────────┤
│ 예약 페이지 │ 결제 페이지 │ 확인 페이지 │ PWA 입장관리 앱     │
│ (/aaa, /bbb)│ (토스결제)  │ (QR 생성)   │ (QR 스캔)           │
└─────────────┴─────────────┴─────────────┴─────────────────────┘
                              │
┌─────────────────────────────────────────────────────────────┐
│                  슈퍼 관리자 인터페이스 🆕                   │
├─────────────┬─────────────┬─────────────┬─────────────────────┤
│ 전시회 관리 │ 담당자 관리 │ 전체 통계   │ 시스템 설정         │
│ (/super-admin/tickets) │ (/super-admin/stats) │             │
└─────────────┴─────────────┴─────────────┴─────────────────────┘
                              │
┌─────────────────────────────────────────────────────────────┐
│                 전시회 담당자 인터페이스 🆕                  │
├─────────────┬─────────────┬─────────────┬─────────────────────┤
│ 상품 관리   │ 주문 관리   │ 입장 관리   │ 전시회 통계         │
│ (/admin/products) │ (/admin/orders) │ (/admin/entrance) │   │
└─────────────┴─────────────┴─────────────┴─────────────────────┘
                              │
┌─────────────────────────────────────────────────────────────┐
│                    API Gateway (nginx)                     │
│                  - 권한 기반 라우팅 🆕                      │
└─────────────────────────────────────────────────────────────┘
                              │
┌─────────────────────────────────────────────────────────────┐
│                  FastAPI 백엔드 서버                       │
├─────────────┬─────────────┬─────────────┬─────────────────────┤
│ 예약 API    │ 결제 API    │슈퍼관리자API│ 담당자 API 🆕       │
│ 재고 관리   │ 웹훅 처리   │전시회 관리  │ 상품/주문 관리      │
└─────────────┴─────────────┴─────────────┴─────────────────────┘
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│ PostgreSQL  │    │    Redis    │    │ 외부 API    │
│ (메인 DB)   │    │ (캐시/대기열)│   │ 토스/카카오 │
│권한/활동로그│    │전시회별 재고│    │    🆕       │
└─────────────┘    └─────────────┘    └─────────────┘
```

### 컴포넌트별 역할

#### Frontend (Next.js + React)
- **일반 사용자 인터페이스**: 반응형 웹 디자인
- **슈퍼 관리자 인터페이스** 🆕: 전시회 생성, 담당자 관리
- **전시회 담당자 인터페이스** 🆕: 상품 관리, 주문 관리  
- **권한 기반 라우팅** 🆕: PermissionGuard 컴포넌트
- **PWA 기능**: 오프라인 지원, 푸시 알림
- **QR 스캔**: 카메라 API 활용 현장 입장 관리

#### Backend (FastAPI)
- **API 서버**: RESTful API 제공
- **권한 미들웨어** 🆕: JWT + 권한 레벨 검증
- **다중 전시회 로직** 🆕: 전시회별 데이터 격리
- **비즈니스 로직**: 예약, 결제, 재고 관리
- **외부 연동**: 결제, 알림 API 통합
- **활동 로그** 🆕: 모든 관리자 활동 추적

#### Database (PostgreSQL)
- **사용자 데이터**: 슈퍼 관리자, 전시회 담당자 🆕
- **전시회 데이터**: 다중 전시회 관리 🆕
- **권한 데이터**: 권한 레벨, 접근 제어 🆕
- **활동 로그**: 관리자 활동 추적 🆕
- **주문 데이터**: 주문, 상품, 결제 정보
- **관계형 데이터**: 정규화된 스키마

#### Cache (Redis)
- **전시회별 세션**: 사용자 대기열 상태 🆕
- **전시회별 재고**: 빠른 재고 조회/차감 🆕
- **권한 캐시**: JWT 토큰 검증 캐시 🆕
- **임시 데이터**: 결제 진행 중 데이터

---

## 🖥 개발 환경 구성

### 서버 사양 요구사항

#### 개발 환경
```
OS: Ubuntu 22.02 LTS
CPU: 8코어 (최소 2코어)
RAM: 32GB (최소 8GB)
Storage: SSD 500GB (최소 100GB)
Network: 100Mbps
```

#### 프로덕션 환경
```
OS: Ubuntu 24.04 LTS
CPU: 8코어 (최소 4코어)
RAM: 32GB (최소 16GB)
Storage: SSD 500GB (최소 200GB)
Network: 1Gbps
```

### Native 설치 환경 (Docker 미사용)

#### 1. 시스템 패키지 설치
```bash
# 시스템 업데이트
sudo apt update && sudo apt upgrade -y

# 기본 개발 도구
sudo apt install -y build-essential curl wget git vim

# Python 개발 환경
sudo apt install -y python3.12 python3.12-venv python3.12-dev python3-pip

# Node.js 20.x 설치
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt install -y nodejs

# PostgreSQL 16 설치
sudo apt install -y postgresql-16 postgresql-contrib-16 postgresql-client-16

# Redis 7 설치
sudo apt install -y redis-server

# nginx 설치
sudo apt install -y nginx

# 추가 유틸리티
sudo apt install -y htop tree jq unzip
```

#### 2. PostgreSQL 설정
```bash
# PostgreSQL 서비스 시작
sudo systemctl start postgresql
sudo systemctl enable postgresql

# 데이터베이스 및 사용자 생성
sudo -u postgres createuser ticket_user
sudo -u postgres createdb ticket_system
sudo -u postgres psql -c "ALTER USER ticket_user WITH ENCRYPTED PASSWORD 'ticket_pass';"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE ticket_system TO ticket_user;"

# 외부 접속 허용 (필요 시)
sudo nano /etc/postgresql/16/main/postgresql.conf
# listen_addresses = 'localhost'

sudo nano /etc/postgresql/16/main/pg_hba.conf
# local   all             ticket_user                         md5

sudo systemctl restart postgresql
```

#### 3. Redis 설정
```bash
# Redis 설정 파일 수정
sudo nano /etc/redis/redis.conf

# 다음 설정 변경:
# maxmemory 2gb
# maxmemory-policy allkeys-lru
# save 900 1
# save 300 10
# save 60 10000

# Redis 서비스 재시작
sudo systemctl restart redis-server
sudo systemctl enable redis-server
```

#### 4. 프로젝트 디렉토리 구조 생성
```bash
# 프로젝트 루트 디렉토리
sudo mkdir -p /opt/ticket-system
sudo chown $USER:$USER /opt/ticket-system
cd /opt/ticket-system

# 기본 구조 생성
mkdir -p {backend,frontend,docs,scripts,logs}

# 백엔드 가상환경 생성
cd backend
python3.12 -m venv venv
source venv/bin/activate
pip install --upgrade pip

# 프론트엔드 초기화
cd ../frontend
npm init -y
```

### 환경변수 설정

#### 백엔드 환경변수 (.env)
```bash
# backend/.env
# 데이터베이스 설정
DATABASE_URL=postgresql://ticket_user:ticket_pass@localhost:5432/ticket_system
REDIS_URL=redis://localhost:6379

# JWT 설정
SECRET_KEY=your-super-secret-key-here-change-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# 토스페이먼츠 설정
TOSS_CLIENT_KEY=test_ck_your_client_key
TOSS_SECRET_KEY=test_sk_your_secret_key
TOSS_PAYMENT_URL=https://api.tosspayments.com/v1/payments

# 카카오 알림톡 설정
KAKAO_REST_API_KEY=your_kakao_rest_api_key
KAKAO_SENDER_KEY=your_sender_key

# 환경 설정
ENVIRONMENT=development
DEBUG=true
LOG_LEVEL=INFO

# 파일 업로드 설정
UPLOAD_PATH=/opt/ticket-system/uploads
MAX_FILE_SIZE=10485760  # 10MB
```

#### 프론트엔드 환경변수 (.env.local)
```bash
# frontend/.env.local
# API 설정
NEXT_PUBLIC_API_URL=http://localhost:8000
NEXT_PUBLIC_WS_URL=ws://localhost:8000/ws

# 토스페이먼츠 클라이언트 키
NEXT_PUBLIC_TOSS_CLIENT_KEY=test_ck_your_client_key

# 환경 설정
NEXT_PUBLIC_APP_ENV=development
NEXT_PUBLIC_APP_NAME=Ticket System

# PWA 설정
NEXT_PUBLIC_PWA_ENABLED=true
```

### 개발 도구 설정

#### VS Code 확장 프로그램
```json
{
  "recommendations": [
    "ms-python.python",
    "ms-python.flake8",
    "ms-python.black-formatter",
    "bradlc.vscode-tailwindcss",
    "esbenp.prettier-vscode",
    "ms-vscode.vscode-json",
    "redhat.vscode-yaml",
    "ms-vscode.vscode-typescript-next"
  ]
}
```

#### Git 설정
```bash
# Git 초기 설정
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# 프로젝트 Git 초기화
cd /opt/ticket-system
git init
git remote add origin https://github.com/your-username/ticket-system.git

# .gitignore 생성
cat << EOF > .gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
env/
.env

# Node.js
node_modules/
npm-debug.log*
.npm
.next/
out/
.env.local
.env.development.local
.env.test.local
.env.production.local

# Database
*.db
*.sqlite

# Logs
logs/
*.log

# OS
.DS_Store
Thumbs.db

# IDE
.vscode/
.idea/
*.swp
*.swo

# Build
dist/
build/
EOF
```

---

## 📚 문서 구조

이 프로젝트는 다음과 같은 문서들로 구성되어 있습니다:

### 📄 핵심 문서들

1. **[프로젝트 개요 및 개발환경](ticket_overview.md)** ⭐ (현재 문서)
   - 프로젝트 전체 개요
   - 다중 전시회 관리 플로우
   - 기술 스택 및 개발 단계
   - 시스템 아키텍처
   - 개발 환경 구성

2. **[데이터베이스 스키마 설계](ticket_database.md)**
   - 다중 관리자 테이블 구조
   - 권한 기반 데이터 모델
   - 인덱스 최적화 전략
   - 초기 데이터 스크립트

3. **[프론트엔드 구조 및 컴포넌트](ticket_frontend.md)**
   - Next.js 페이지 구조
   - 권한 기반 라우팅
   - 슈퍼 관리자 / 담당자 UI
   - PWA 및 QR 스캐너

4. **[백엔드 API 및 서비스](ticket_backend.md)**
   - FastAPI 구조
   - 권한 기반 API 설계
   - 슈퍼 관리자 / 담당자 API
   - 인증 및 보안 시스템

5. **[성능 최적화 및 보안](ticket_performance.md)**
   - 동시 접속 1만명 대응 전략
   - Redis 캐시 최적화
   - 오버셀링 방지 로직
   - 보안 설정 및 방화벽

6. **[배포 및 운영 가이드](ticket_deployment.md)**
   - 프로덕션 환경 구성
   - 모니터링 및 로깅
   - 백업 및 재해 복구
   - 운영 매뉴얼

### 📋 추가 참고 문서들

7. **[테스트 전략 및 가이드](ticket_testing.md)**
   - 단위 테스트
   - 통합 테스트
   - 성능 테스트
   - 권한 시스템 테스트

8. **[문제 해결 가이드](ticket_troubleshooting.md)**
   - 자주 발생하는 문제들
   - 디버깅 방법
   - 로그 분석
   - 성능 이슈 해결

### 📖 문서 읽기 순서 (권장)

#### 🔰 초기 개발자용
1. **프로젝트 개요 및 개발환경** (현재 문서) - 전체 이해
2. **데이터베이스 스키마 설계** - DB 구조 파악
3. **백엔드 API 및 서비스** - API 구조 이해
4. **프론트엔드 구조 및 컴포넌트** - UI 구조 파악

#### 🚀 실제 개발 시작할 때
1. **프로젝트 개요 및 개발환경** - 환경 설정
2. **데이터베이스 스키마 설계** - DB 구축
3. **백엔드 API 및 서비스** - API 개발
4. **프론트엔드 구조 및 컴포넌트** - UI 개발
5. **성능 최적화 및 보안** - 최적화 작업

#### 🔧 배포 및 운영 시
1. **성능 최적화 및 보안** - 성능 튜닝
2. **배포 및 운영 가이드** - 배포 설정
3. **테스트 전략 및 가이드** - 테스트 실행
4. **문제 해결 가이드** - 운영 중 문제 해결

---

## 🚀 빠른 시작 가이드

### 1. 환경 설정 체크리스트

```bash
# 1. 시스템 패키지 설치 확인
python3.12 --version     # Python 3.12+
node --version           # Node.js 20+
psql --version          # PostgreSQL 16+
redis-cli --version     # Redis 7+

# 2. 서비스 상태 확인
sudo systemctl status postgresql
sudo systemctl status redis-server

# 3. 데이터베이스 연결 테스트
psql -U ticket_user -d ticket_system -h localhost -c "SELECT version();"

# 4. Redis 연결 테스트
redis-cli ping
```

### 2. 프로젝트 초기 설정

```bash
# 프로젝트 클론 및 이동
git clone https://github.com/your-username/ticket-system.git
cd ticket-system

# 백엔드 설정
cd backend
python3.12 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 환경변수 복사 및 수정
cp .env.example .env
nano .env  # 설정 값들 수정

# 데이터베이스 마이그레이션
alembic upgrade head

# 프론트엔드 설정
cd ../frontend
npm install

# 환경변수 복사 및 수정
cp .env.local.example .env.local
nano .env.local  # 설정 값들 수정
```

### 3. 개발 서버 실행

```bash
# 터미널 1: 백엔드 서버
cd backend
source venv/bin/activate
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# 터미널 2: 프론트엔드 서버
cd frontend
npm run dev

# 터미널 3: Redis 모니터링 (선택사항)
redis-cli monitor
```

### 4. 접속 확인

- **프론트엔드**: http://localhost:3000
- **백엔드 API 문서**: http://localhost:8000/docs
- **슈퍼 관리자**: http://localhost:3000/super-admin/login
- **일반 관리자**: http://localhost:3000/admin/login

### 5. 초기 계정 정보

```
슈퍼 관리자:
- ID: superadmin
- PW: admin123

테스트 전시회 담당자:
- ID: manager1
- PW: manager123
```

---

## 💡 다음 단계

이 문서를 읽은 후에는 다음 순서로 진행하시기 바랍니다:

### 📋 Step 1: 데이터베이스 이해
**[데이터베이스 스키마 설계](ticket_database.md)** 문서를 읽고 다중 관리자 시스템의 데이터 구조를 파악하세요.

### 🔧 Step 2: 백엔드 구조 파악  
**[백엔드 API 및 서비스](ticket_backend.md)** 문서를 통해 권한 기반 API 설계를 이해하세요.

### 🎨 Step 3: 프론트엔드 구조 학습
**[프론트엔드 구조 및 컴포넌트](ticket_frontend.md)** 문서로 UI 구조와 권한별 화면을 파악하세요.

### ⚡ Step 4: 성능 최적화 전략
**[성능 최적화 및 보안](ticket_performance.md)** 문서로 고성능 시스템 구현 방법을 학습하세요.

---

## 📞 지원 및 문의

### 개발팀 연락처
- **프로젝트 리더**: leader@ticket.com
- **백엔드 개발**: backend@ticket.com  
- **프론트엔드 개발**: frontend@ticket.com
- **시스템 관리**: devops@ticket.com

### 커뮤니케이션 채널
- **Slack**: #ticket-dev
- **이슈 트래킹**: GitHub Issues
- **문서 업데이트**: GitHub Wiki

---
