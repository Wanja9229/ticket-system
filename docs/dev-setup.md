# 🎨 전시티켓예약 시스템 - 프론트엔드 개발환경 구축 (Windows 11 기준, JavaScript 버전)

이 문서는 Windows 11 환경에서 `ticket-system/frontend` 폴더 기준으로 전시티켓예약 시스템의 **프론트엔드 개발환경을 JavaScript 기반으로 구축**하는 실전 가이드입니다.  
Next.js 14 (App Router), JavaScript, SCSS 기반으로 구성됩니다.

---

## ✅ 1. 필수 도구 설치

| 도구 | 설명 | 링크 |
|------|------|------|
| Node.js | v22.17.1 (LTS 권장) | https://nodejs.org |
| Git | 버전 관리 툴 | https://git-scm.com |
| VS Code | 코드 편집기 | https://code.visualstudio.com |

설치 완료 후 버전 확인:

```bash
node -v
npm -v
git --version
```

---

## 📁 2. 프로젝트 디렉토리 생성 및 진입

먼저 루트 로컬에 프로젝트 폴더(`ticket-system`)를 만들고, 프론트엔드 디렉토리로 진입합니다:

```bash
mkdir -p ticket-system/frontend
cd ticket-system/frontend
```

---

## ⚙️ 3. Next.js 프로젝트 초기화

App Router + JavaScript 기반으로 프로젝트를 초기화합니다:

```bash
npx create-next-app@latest . --app
```

### 프롬프트 응답 예시:

| 질문 | 답변 |
|------|------|
| TypeScript 사용 | ❌ No |
| ESLint 사용 | ✅ Yes |
| Tailwind CSS 사용 | ❌ No |
| src/ 디렉토리 구조 | ✅ Yes |
| Turbopack for `next dev`| ❌ No |
| customize the import alias (`@/*` by default)?| ✅ Yes |

---
## 🧵 4 npm 패키지 라이브러리 설치
```bash
npm install axios @tanstack/react-query clsx dayjs react-hook-form qrcode.react react-toastify jwt-decode sass
```

### 사용 예시:

```js
// app/page.js
import styles from './page.module.scss';

export default function Home() {
  return <h1 className={styles.title}>Exhibition System</h1>;
}
```

```scss
/* page.module.scss */
.title {
  color: #1e88e5;
  font-weight: bold;
  font-size: 2rem;
}
```

---

## 🚀 5. 개발 서버 실행

```bash
npm run dev
```

브라우저에서 확인: http://localhost:3000

---

## 🗂️ 6. 디렉토리 구조 예시

```text
ticket-system/
└── frontend/
    ├── app/
    │   ├── [exhibition]/         # 유저 예약 흐름
    │   ├── admin/                # 전시회 담당자
    │   ├── super-admin/          # 슈퍼 관리자
    │   └── entrance/             # QR 입장 PWA
    ├── components/               # 재사용 컴포넌트
    ├── hooks/                    # 커스텀 훅
    ├── services/                 # API 모듈
    ├── styles/                   # SCSS 전용
    ├── public/
    │   └── images/               # 이미지 파일
    └── .env.local                # 환경변수 설정
```

---

## 📄 7. .env.local 환경변수 설정

```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

---

## 🔌 8. 추천 VS Code 확장

- ESLint  
- Prettier  
- React (by VS Code 팀)  
- Thunder Client (API 테스트용)

---

## ✅ 9. 다음 실습 추천

- [ ] 공통 Layout 컴포넌트 만들기 (`components/common/Layout.js`)
- [ ] 관리자 로그인 페이지 (`/admin/login`)
- [ ] 사용자 예약 → 결제 → 완료 흐름 (`/[exhibition]/order`)
- [ ] `react-query`로 API 연동 실습

---

_작성일: 2025.07.25  
작성자: ilogini_
