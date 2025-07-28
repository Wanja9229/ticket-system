# 🏗️ 전시회 티켓 예약 시스템 - Next.js 프론트엔드 구조 가이드

> **프로젝트명**: ticket-system  
> **목표**: 권한 기반 다중 관리자 지원 Next.js 프론트엔드  
> **작성일**: 2025.07.28  
> **버전**: v3.0 (Next.js 14 App Router 기반 구조)

## 📋 목차
1. [프로젝트 개요](#프로젝트-개요)
2. [전체 폴더 구조](#전체-폴더-구조)
3. [폴더별 상세 설명](#폴더별-상세-설명)
4. [데이터 흐름도](#데이터-흐름도)
5. [실제 사용 예시](#실제-사용-예시)
6. [개발 가이드라인](#개발-가이드라인)

---

## 🎯 프로젝트 개요

이 문서는 **전시회 예약 시스템**의 Next.js 프론트엔드 구조를 설명합니다.  
각 폴더의 역할과 파일들이 어떻게 연결되는지 이해하기 쉽게 정리했습니다.

### 핵심 원칙
- **명확한 역할 분리**: 각 폴더는 하나의 명확한 목적을 가집니다
- **재사용성**: 컴포넌트와 함수는 재사용 가능하게 설계합니다
- **확장성**: 새로운 기능 추가가 쉬운 구조입니다

---

## 📁 전체 폴더 구조
```
exhibition-frontend/
├── app/                    # 🏠 라우팅 & 페이지]

├── components/             # 🧩 재사용 컴포넌트
├── lib/                    # 🔧 유틸리티 & 설정
├── services/               # 📡 API 통신 로직
├── contexts/               # 🌐 전역 상태 관리
├── hooks/                  # 🎣 커스텀 훅
├── public/                 # 📦 정적 파일
├── styles/                 # 🎨 스타일 파일
└── data/                   # 📊 정적 데이터
```

---

## 📂 폴더별 상세 설명

### 1. `app/` - 라우팅 & 페이지 🏠
**역할**: URL 경로와 1:1로 매칭되는 페이지 파일들을 관리합니다.
```
app/
├── layout.js               # 전체 레이아웃 (HTML 구조)
├── page.js                 # 메인 페이지 (/)
├── error.js                # 에러 페이지
├── loading.js              # 로딩 컴포넌트
├── not-found.js            # 404 페이지
│
├── (public)/               # 일반 사용자 영역 (URL에 안 보임)
│   ├── layout.js          # 헤더/푸터 있는 레이아웃
│   ├── exhibitions/       # 전시회 관련
│   │   ├── page.js       # 전시회 목록 (/exhibitions)
│   │   └── [id]/         # 동적 라우트
│   │       └── page.js   # 전시회 상세 (/exhibitions/123)
│   └── about/
│       └── page.js       # 회사소개 (/about)
│
├── (admin)/                # 관리자 영역
│   ├── layout.js          # 사이드바 레이아웃
│   └── admin/
│       └── page.js       # 관리자 대시보드 (/admin)
│
└── (auth)/                 # 인증 영역
    ├── layout.js          # 심플 레이아웃
    └── login/
        └── page.js       # 로그인 (/login)
```

**주요 파일 설명**:
- `layout.js`: 자식 페이지들을 감싸는 공통 레이아웃
- `page.js`: 실제 페이지 컴포넌트
- `[id]`: 동적 경로 (예: /exhibitions/1, /exhibitions/2)
- `(폴더명)`: Route Group - URL에 영향 없이 레이아웃 그룹화

---

### 2. `components/` - 재사용 컴포넌트 🧩

**역할**: 여러 페이지에서 재사용되는 UI 조각들을 관리합니다.
```
components/
├── common/                 # 🌍 공통 컴포넌트
│   ├── Header.js          # 상단 헤더
│   ├── Footer.js          # 하단 푸터
│   ├── Navigation.js      # 네비게이션 메뉴
│   └── Logo.js            # 로고
│
├── ui/                     # 🎨 기본 UI 요소
│   ├── Button.js          # 버튼
│   ├── Input.js           # 입력 필드
│   ├── Card.js            # 카드 컴포넌트
│   ├── Modal.js           # 모달 팝업
│   └── Toast.js           # 토스트 메시지
│
└── features/               # 🚀 기능별 컴포넌트
    ├── exhibitions/
    │   ├── ExhibitionCard.js      # 전시회 카드
    │   ├── ExhibitionList.js      # 전시회 목록
    │   └── ReservationForm.js     # 예약 폼
    └── auth/
        ├── LoginForm.js            # 로그인 폼
        └── RegisterForm.js         # 회원가입 폼
```

**컴포넌트 분류 기준**:
- `common/`: 레이아웃에 사용되는 큰 단위 컴포넌트
- `ui/`: 어디서든 쓸 수 있는 작은 단위 컴포넌트
- `features/`: 특정 기능에 특화된 컴포넌트
---

### 3. `lib/` - 유틸리티 & 설정 🔧

**역할**: 프로젝트 전반에서 사용되는 헬퍼 함수, 설정, 유틸리티를 관리합니다.

```
lib/
├── api/                    # 🔌 API 통신 설정
│   ├── client.js          # Axios 인스턴스
│   ├── endpoints.js       # API 엔드포인트 목록
│   └── interceptors.js    # 요청/응답 인터셉터
│
├── metadata/               # 🔍 SEO & 메타데이터
│   ├── config.js          # 사이트 기본 정보
│   ├── generators.js      # 메타데이터 생성 함수
│   └── templates.js       # 페이지별 템플릿
│
├── constants/              # 📌 상수값
│   ├── routes.js          # 라우트 경로
│   ├── messages.js        # 메시지 (에러, 성공 등)
│   └── config.js          # 앱 설정값
│
└── utils/                  # 🛠 유틸리티 함수
    ├── format.js          # 날짜, 숫자 포맷
    ├── validation.js      # 유효성 검사
    └── storage.js         # 로컬스토리지 헬퍼
```

---

### 4. `services/` - API 통신 로직 📡

**역할**: 백엔드 API와의 통신 로직을 관리합니다.
```
services/
├── api/                    # 🌐 내부 API 서비스
│   ├── auth.service.js    # 인증 관련 API
│   ├── exhibitions.service.js  # 전시회 API
│   └── reservations.service.js # 예약 API
│
└── external/               # 🔗 외부 API 서비스
    ├── payment.service.js  # 토스페이먼츠
    └── notification.service.js # 카카오 알림톡
```

**Service 파일 구조 예시**:
```javascript
// exhibitions.service.js
class ExhibitionService {
  async getList() { }      // 목록 조회
  async getDetail(id) { }  // 상세 조회
  async create(data) { }   // 생성
  async update(id, data) { } // 수정
  async delete(id) { }     // 삭제
}
```

---

### 5. `contexts/` - 전역 상태 관리 🌐
**역할**: 여러 컴포넌트에서 공유하는 전역 상태를 관리합니다.

```
contexts/
├── AuthContext.js          # 🔐 인증/사용자 정보
├── ThemeContext.js         # 🎨 테마 (다크모드 등)
├── ToastContext.js         # 📢 토스트 메시지
└── ModalContext.js         # 🪟 모달 상태
```

**언제 Context를 사용하나요?**
- 여러 컴포넌트에서 공유하는 데이터
- Props로 전달하기에 너무 깊은 계층
- 전역적으로 필요한 UI 상태

---

### 6. `hooks/` - 커스텀 훅 🎣
**역할**: 재사용 가능한 로직을 훅으로 만들어 관리합니다.

```
hooks/
├── useAuth.js              # 인증 관련 로직
├── useDebounce.js          # 디바운스 처리
├── useLocalStorage.js      # 로컬스토리지 연동
└── useInfiniteScroll.js    # 무한 스크롤
```

---

### 7. `public/` - 정적 파일 📦
**역할**: 이미지, 폰트, 파비콘 등 정적 파일을 관리합니다.
```
public/
├── images/                 # 이미지 파일
├── fonts/                  # 웹폰트
├── icons/                  # 아이콘
└── favicon.ico            # 파비콘
```

---

### 8. `styles/` - 스타일 파일 🎨
**역할**: 전역 스타일과 CSS 파일을 관리합니다.
```
styles/
├── globals.css            # 전역 스타일
├── variables.css          # CSS 변수
└── components/            # 컴포넌트별 스타일
```

---

### 9. `data/` - 정적 데이터 📊
**역할**: 하드코딩된 데이터나 설정값을 관리합니다.
```
data/
├── menu.js                # 메뉴 구조
├── company.js             # 회사 정보
└── faqs.js                # FAQ 데이터
```

---

## 🔄 데이터 흐름도

### 전체 흐름
```
사용자 → Page → Component → Service → API → Backend
         ↓         ↓          ↓
      Context   Custom Hook  Axios Client
```

### 상세 흐름도
```
┌─────────────┐     ┌──────────────┐     ┌─────────────┐
│  사용자 액션  │ ──→ │ Page Component│ ──→ │ 데이터 필요? │
└─────────────┘     └──────────────┘     └─────────────┘
                                                 │
                    ┌────────────────────────────┼────────────────────────┐
                    ↓                            ↓                        ↓
            ┌──────────────┐            ┌──────────────┐         ┌──────────────┐
            │   Context    │            │   Service    │         │  Component   │
            │  (전역 상태)  │            │  (API 호출)   │         │   (UI만)     │
            └──────────────┘            └──────────────┘         └──────────────┘
                    │                            │                        │
                    ↓                            ↓                        │
            ┌──────────────┐            ┌──────────────┐                │
            │useContext Hook│            │  API Client  │                │
            └──────────────┘            └──────────────┘                │
                    │                            │                        │
                    │                            ↓                        │
                    │                    ┌──────────────┐                │
                    │                    │ Backend API  │                │
                    │                    └──────────────┘                │
                    │                            │                        │
                    │                            ↓                        │
                    │                    ┌──────────────┐                │
                    │                    │  응답 데이터  │                │
                    │                    └──────────────┘                │
                    │                            │                        │
                    ↓                            ↓                        ↓
                    └────────────────────────────┴────────────────────────┘
                                                 │
                                                 ↓
                                        ┌──────────────┐
                                        │ UI 렌더링    │
                                        └──────────────┘
```

---

## 💡 실제 사용 예시

### 예시: 전시회 예약 프로세스

**1. 사용자가 전시회 상세 페이지 접속**
```
└── app/exhibitions/[id]/page.js
```

**2. 페이지에서 전시회 데이터 로드**
```
└── services/api/exhibitions.service.js
    └── lib/api/client.js (Axios)
```

**3. 예약 버튼 클릭**
```
└── components/features/exhibitions/ReservationForm.js
```

**4. 로그인 체크**
```
└── contexts/AuthContext.js (전역 상태)
```

**5. 예약 API 호출**
```
└── services/api/reservations.service.js
```

**6. 성공/실패 메시지**
```
└── contexts/ToastContext.js
    └── components/ui/Toast.js
```

---

## 🛠️ 개발 가이드라인

### 1. 컴포넌트 작성 규칙

**파일 네이밍**
- 컴포넌트: `PascalCase.js` (예: `ExhibitionCard.js`)
- 훅: `camelCase.js` (예: `useAuth.js`)
- 유틸리티: `camelCase.js` (예: `format.js`)

**컴포넌트 구조**
```javascript
// 1. imports
import React from 'react';
import styles from './Component.module.scss';

// 2. 컴포넌트 정의
function Component({ prop1, prop2 }) {
  // 3. 상태 및 훅
  const [state, setState] = useState();
  
  // 4. 이펙트
  useEffect(() => {}, []);
  
  // 5. 핸들러
  const handleClick = () => {};
  
  // 6. 렌더링
  return <div>...</div>;
}

// 7. export
export default Component;
```

### 2. API 서비스 패턴

```javascript
// services/api/exhibitions.service.js
import apiClient from '@/lib/api/client';

class ExhibitionService {
  // 목록 조회
  async getList(params) {
    const { data } = await apiClient.get('/exhibitions', { params });
    return data;
  }
  
  // 상세 조회
  async getDetail(id) {
    const { data } = await apiClient.get(`/exhibitions/${id}`);
    return data;
  }
  
  // 생성 (관리자용)
  async create(exhibitionData) {
    const { data } = await apiClient.post('/exhibitions', exhibitionData);
    return data;
  }
}

export default new ExhibitionService();
```

### 3. 상태 관리 베스트 프랙티스

**Context 사용**
```javascript
// contexts/AuthContext.js
import { createContext, useContext, useState } from 'react';

const AuthContext = createContext();

export function AuthProvider({ children }) {
  const [user, setUser] = useState(null);
  
  const login = async (credentials) => {
    // 로그인 로직
  };
  
  const logout = () => {
    // 로그아웃 로직
  };
  
  return (
    <AuthContext.Provider value={{ user, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
}

export const useAuth = () => useContext(AuthContext);
```

### 4. 스타일링 규칙

**SCSS 모듈 사용**
```scss
// Component.module.scss
.container {
  padding: 20px;
  
  &__header {
    margin-bottom: 16px;
  }
  
  &__content {
    display: flex;
    gap: 12px;
    
    @media (max-width: 768px) {
      flex-direction: column;
    }
  }
}
```

**CSS 변수 활용**
```css
/* styles/variables.css */
:root {
  /* 색상 */
  --color-primary: #3B82F6;
  --color-secondary: #10B981;
  --color-danger: #EF4444;
  
  /* 간격 */
  --spacing-xs: 4px;
  --spacing-sm: 8px;
  --spacing-md: 16px;
  --spacing-lg: 24px;
  --spacing-xl: 32px;
  
  /* 글꼴 크기 */
  --font-xs: 12px;
  --font-sm: 14px;
  --font-md: 16px;
  --font-lg: 18px;
  --font-xl: 24px;
}
```

### 5. 성능 최적화 팁

**이미지 최적화**
```javascript
import Image from 'next/image';

function ExhibitionCard({ image, title }) {
  return (
    <Image
      src={image}
      alt={title}
      width={300}
      height={200}
      loading="lazy"
      placeholder="blur"
    />
  );
}
```

**동적 임포트**
```javascript
// 무거운 컴포넌트는 필요할 때만 로드
const QRScanner = dynamic(() => import('@/components/QRScanner'), {
  loading: () => <p>스캐너 로딩중...</p>,
  ssr: false
});
```

**메모이제이션**
```javascript
// 비용이 높은 계산은 메모이제이션
const expensiveValue = useMemo(() => {
  return calculateExpensiveValue(data);
}, [data]);

// 자주 리렌더링되는 컴포넌트는 React.memo
const OptimizedComponent = React.memo(({ prop1, prop2 }) => {
  return <div>...</div>;
});
```

---

## 📄 페이지별 구조 설계

### 1. 고객 예약 페이지 (/[event_code])

**이벤트 홈페이지**
- 이벤트 정보 및 이미지 갤러리
- 티켓 종류 및 가격 안내
- 최신 공지사항 (최대 5개)
- 예약하기 버튼 (메인 CTA)

**예약 플로우**
- **Step 1**: 티켓 선택 (상품, 옵션, 수량, 날짜)
- **Step 2**: 고객 정보 입력 (이름, 전화번호, 이메일)
- **Step 3**: 결제 방법 선택 (토스페이먼츠)
- **Step 4**: 예약 확인 및 결제

**결제 완료 페이지**
- QR 티켓 표시 (개별 QR 코드)
- 주문 상세 정보
- 스마트폰 저장 기능
- 공유 기능

### 2. 슈퍼 관리자 대시보드 (/super-admin)

**메인 대시보드**
- 전체 시스템 통계 (이벤트 수, 총 매출, 총 주문, 활성 관리자)
- 이벤트별 매출 차트
- 최근 활동 로그
- 빠른 액션 버튼

**이벤트 관리**
- 이벤트 목록 (테이블 형태)
- 이벤트 생성/수정/삭제
- 이벤트 활성화/비활성화
- 이벤트별 상세 통계

**관리자 관리**
- 관리자 목록 (이벤트별 필터)
- 관리자 계정 생성/수정/삭제
- 권한 레벨 관리
- 비밀번호 초기화

**전체 통계 및 분석**
- 매출 분석 (기간별, 이벤트별)
- 관리자 활동 로그
- 시스템 성능 지표
- 데이터 내보내기

### 3. 이벤트 관리자 대시보드 (/admin)

**이벤트 대시보드**
- 자신의 이벤트 통계 (매출, 주문, 입장, 재고)
- 오늘의 현황 (실시간 업데이트)
- 매출 추이 차트
- 최근 주문 목록
- 재고 부족 알림

**상품 관리 (Level 2+)**
- 상품 목록 및 재고 현황
- 상품 등록/수정/삭제
- 상품 옵션 관리 (성인/청소년/어린이)
- 재고 조정 기능

**주문 관리 (Level 1+)**
- 주문 목록 (필터링, 검색)
- 주문 상세 정보
- 환불 처리 (Level 3+)
- 주문 상태 변경
- 엑셀 내보내기

**입장 관리**
- QR 스캔 인터페이스 (웹 기반)
- 입장 로그 조회
- 입장 통계 (일별, 시간별)
- 수동 입장 처리

### 4. PWA 입장 관리 앱 (/scanner)

**QR 스캔 메인 화면**
- 카메라 뷰 및 QR 스캔 기능
- 실시간 스캔 결과 표시
- 입장 확인/거부 처리
- 오늘의 입장 통계

**오프라인 지원**
- 오프라인 스캔 데이터 저장
- 온라인 복구 시 자동 동기화
- 오프라인 상태 표시
- 대기열 관리

**설정 및 이력**
- 카메라 설정 (해상도, 포커스)
- 스캔 이력 조회
- 장치 정보 및 상태
- 로그아웃 기능

---

## 🧩 컴포넌트 아키텍처

### 컴포넌트 분류 체계

**1. Layout 컴포넌트**
- `RootLayout`: 전역 레이아웃 (SEO, 폰트, 전역 상태)
- `PublicLayout`: 고객용 레이아웃 (이벤트별 헤더/푸터)
- `SuperAdminLayout`: 슈퍼 관리자 레이아웃 (사이드바, 헤더)
- `AdminLayout`: 이벤트 관리자 레이아웃 (권한별 메뉴)
- `PWALayout`: PWA 스캐너 레이아웃 (모바일 최적화)

**2. Auth 컴포넌트**
- `PermissionGuard`: 권한 기반 렌더링 제어
- `ProtectedRoute`: 인증 필요 페이지 보호
- `RoleBasedComponent`: 역할별 UI 컴포넌트
- `LoginForm`: 관리자 타입별 로그인 폼

**3. UI 컴포넌트**
- `Button`: 다양한 변형 및 상태 지원
- `Input`: 폼 입력 필드 (검증 포함)
- `Modal`: 모달 다이얼로그
- `Toast`: 알림 메시지
- `Table`: 데이터 테이블 (정렬, 페이징)
- `Chart`: 차트 컴포넌트 (Chart.js 기반)

**4. Business 컴포넌트**
- `TicketSelector`: 티켓 선택 인터페이스
- `ProductManager`: 상품 관리 인터페이스
- `OrderTable`: 주문 목록 테이블
- `QRScanner`: PWA QR 스캔 기능
- `Dashboard`: 대시보드 위젯

### 컴포넌트 설계 원칙

**재사용성**
- 비즈니스 로직과 UI 로직 분리
- Props 기반 설정 가능한 유연한 인터페이스
- 컴포지션 패턴 활용

**접근성**
- ARIA 속성 및 키보드 네비게이션 지원
- 스크린 리더 호환성
- 포커스 관리 및 트랩

**반응형 디자인**
- 모바일 우선 설계
- 브레이크포인트별 최적화
- PWA 네이티브 앱 경험

---

## 🔄 상태 관리 전략

### 상태 관리 아키텍처

**1. 서버 상태 (React Query)**
- API 데이터 캐싱 및 동기화
- 백그라운드 업데이트
- 오류 재시도 및 복구
- 낙관적 업데이트

**2. 클라이언트 상태 (Zustand)**
- 인증 상태 (사용자 정보, 토큰)
- 예약 플로우 상태 (장바구니, 고객정보)
- UI 상태 (모달, 토스트, 로딩)
- 스캐너 상태 (오프라인 큐, 설정)

**3. 로컬 상태 (React useState)**
- 컴포넌트 내부 상태
- 폼 입력 상태
- 임시 UI 상태

### 상태 지속성 전략

**인증 상태**
- localStorage: 토큰 및 사용자 정보
- 자동 토큰 갱신 및 만료 처리
- 로그아웃 시 상태 정리

**예약 상태**
- sessionStorage: 예약 진행 중 데이터
- 페이지 새로고침 시 상태 복원
- 결제 완료 후 상태 정리

**오프라인 상태**
- IndexedDB: PWA 오프라인 데이터
- 서비스 워커 연동
- 온라인 복구 시 동기화

---

## 🎨 스타일링 시스템

### CSS 아키텍처

**1. SCSS + CSS Modules**
- 컴포넌트별 스타일 격리
- 전역 변수 및 믹스인 활용
- BEM 방법론 기반 클래스 네이밍

**2. 디자인 토큰 시스템**
- 색상, 타이포그래피, 간격 체계화
- CSS 커스텀 프로퍼티 활용
- 다크모드 및 테마 지원

**3. 반응형 디자인**
- 모바일 우선 (Mobile First) 접근
- 브레이크포인트 기반 미디어 쿼리
- 유연한 그리드 및 레이아웃 시스템

### 테마 시스템

**라이트 테마 (기본)**
- 고객 예약 페이지 및 관리자 대시보드
- 밝고 깔끔한 UI
- 높은 가독성 및 접근성

**다크 테마**
- 사용자 선택 옵션
- 야간 사용 시 눈의 피로 감소
- 모든 컴포넌트 다크모드 지원

**스캐너 테마**
- PWA 스캐너 전용 테마
- 어두운 배경으로 카메라 화면 최적화
- 높은 대비로 QR 인식률 향상

---

## 📱 PWA 기능 구현

### PWA 핵심 기능

**1. 서비스 워커**
- 오프라인 캐싱 전략
- 백그라운드 동기화
- 푸시 알림 지원

**2. 카메라 API**
- QR 코드 실시간 스캔
- 후면 카메라 우선 사용
- 카메라 권한 관리

**3. 네이티브 기능**
- 홈 화면 추가
- 전체 화면 모드
- 네이티브 앱과 유사한 UX

### 오프라인 전략

**캐시 우선 (Cache First)**
- 정적 에셋 (CSS, JS, 이미지)
- PWA 매니페스트 및 아이콘

**네트워크 우선 (Network First)**
- API 데이터
- 실시간 정보

**오프라인 폴백**
- 네트워크 오류 시 캐시된 데이터 사용
- 오프라인 안내 페이지
- 재연결 시 자동 동기화

---

## ⚡ 성능 최적화 전략

### Next.js 최적화

**1. 코드 스플리팅**
- 라우트별 자동 분할
- 동적 import 활용
- 컴포넌트별 지연 로딩

**2. 이미지 최적화**
- Next.js Image 컴포넌트
- WebP/AVIF 형식 변환
- 반응형 이미지 제공

**3. 서버 컴포넌트**
- 초기 HTML 생성 최적화
- 클라이언트 JavaScript 감소
- SEO 개선

### 런타임 최적화

**1. React 최적화**
- useMemo, useCallback 활용
- React.memo로 불필요한 리렌더링 방지
- 가상화된 리스트 (긴 목록 처리)

**2. 상태 관리 최적화**
- 필요한 컴포넌트만 구독
- 상태 정규화
- 지역 상태 우선 사용

**3. 네트워크 최적화**
- API 응답 캐싱
- 요청 디바운싱
- 병렬 요청 처리

---

## 🔧 개발 환경 설정

### 필수 의존성

**React 생태계**
```json
{
  "react": "^18.0.0",
  "react-dom": "^18.0.0",
  "next": "^14.0.0"
}
```

**상태 관리**
```json
{
  "@tanstack/react-query": "^5.0.0",
  "zustand": "^4.0.0"
}
```

**스타일링**
```json
{
  "sass": "^1.0.0",
  "classnames": "^2.0.0"
}
```

**PWA 및 유틸리티**
```json
{
  "next-pwa": "^5.0.0",
  "axios": "^1.0.0",
  "qr-scanner": "^1.0.0"
}
```

### 개발 도구 설정

**ESLint + Prettier**
- 코드 품질 및 일관성 유지
- Next.js 규칙 및 React Hooks 규칙
- 자동 포맷팅

**환경 변수 관리**
```bash
# .env.local
NEXT_PUBLIC_API_URL=http://localhost:8000
NEXT_PUBLIC_TOSS_CLIENT_KEY=test_ck_...
NEXT_PUBLIC_APP_ENV=development
```

**빌드 최적화**
```javascript
// next.config.js
module.exports = {
  experimental: {
    appDir: true,
  },
  images: {
    domains: ['localhost', 'ticket-system.com'],
  },
  compiler: {
    removeConsole: process.env.NODE_ENV === 'production',
  },
}
```

### 배포 전략

**개발 환경**
- `npm run dev`: 로컬 개발 서버
- Hot Module Replacement
- 소스맵 및 개발자 도구

**스테이징 환경**
- `npm run build`: 프로덕션 빌드
- 성능 및 번들 크기 분석
- E2E 테스트 실행

**프로덕션 환경**
- 정적 파일 CDN 배포
- 이미지 최적화 서비스
- 성능 모니터링

---

## 🎯 다음 단계

이 프론트엔드 구조 설계를 바탕으로 다음 작업들을 진행할 예정입니다:

### 📋 Step 1: 환경 설정
**[성능 최적화 및 보안](ticket_performance.md)** 문서로 고성능 시스템 구현 방법을 학습하세요.

### 🔧 Step 2: 개발 시작  
각 컴포넌트와 페이지를 단계별로 구현하며, 권한 기반 시스템을 점진적으로 구축합니다.

### ⚡ Step 3: 최적화
성능 측정 및 최적화를 통해 1만명 동시 접속 목표를 달성합니다.

### 🚀 Step 4: 배포
PWA 기능을 포함한 완전한 시스템을 프로덕션 환경에 배포합니다.

---

## 💡 핵심 특징 요약

이 프론트엔드 시스템의 핵심 특징은 다음과 같습니다:

### 🔐 **권한 기반 다중 인터페이스**
- 슈퍼 관리자, 이벤트 관리자, 고객, 현장 스태프별 최적화된 UI
- JWT 기반 권한 검증 및 자동 라우팅
- 이벤트별 완전한 데이터 격리

### 📱 **모던 웹 기술 활용**
- Next.js 14 App Router로 최신 React 기능 활용
- PWA로 네이티브 앱 수준의 사용자 경험
- 오프라인 지원으로 현장에서도 안정적 동작

### 🎨 **확장 가능한 디자인 시스템**
- SCSS + CSS Modules로 유지보수 용이한 스타일링
- 다크모드 및 테마 시스템으로 다양한 환경 지원
- 완전한 반응형 디자인으로 모든 기기 지원

### ⚡ **고성능 아키텍처**
- 코드 스플리팅 및 지연 로딩으로 빠른 초기 로딩
- React Query로 효율적인 서버 상태 관리
- 최적화된 이미지 및 에셋 처리

이제 **성능 최적화 및 보안** 문서를 작성하여 고성능 시스템 구현 방법을 다루겠습니다! 💪