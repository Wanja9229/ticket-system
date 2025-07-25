# 🎨 전시티켓예약 시스템 - 프론트엔드 개발환경 구축 (Windows 11 기준)

이 문서는 전시티켓예약 시스템의 프론트엔드 개발환경을 Windows 11에서 구축하는 과정을 설명합니다.  
Next.js App Router + javascript + SCSS 기반입니다.

---

## 📁 2. 프로젝트 디렉토리 생성 및 진입

먼저 작업할 폴더를 만들고 이동합니다:

```bash
mkdir exhibition-frontend
cd exhibition-frontend
```

---

## ⚙️ 3. Next.js 프로젝트 초기화

App Router + javascript 기반으로 생성:

```bash
npx create-next-app@latest . --app --javascript
```

### 프롬프트 응답 예시:

| 질문 | 답변 |
|------|------|
| javascript 사용 | ✅ Yes |
| Tailwind CSS 사용 | ❌ No |
| App Router 사용 | ✅ Yes |
| ESLint 사용 | ✅ Yes |
| src/ 디렉토리 구조 | ❌ No |
| 테스트 추가할까요? | ❌ No |

---

## 🧵 4. SCSS 설정

SCSS 설치:

```bash
npm install sass
```

---

## 🚀 5. 개발 서버 실행

```bash
npm run dev
```

브라우저에서 접속 확인 → http://localhost:3000

---

## 📦 6. 주요 라이브러리 설치

```bash
npm install axios react-query clsx
npm install react-hook-form dayjs
```

---

## 🗂️ 7. 디렉토리 구조 예시

```text
exhibition-frontend/
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

## 📄 8. .env.local 환경변수 설정

```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

---

## 🔌 9. 추천 VS Code 확장

- ESLint  
- Prettier  
- React (by VS Code)  
- Thunder Client (API 테스트용)
