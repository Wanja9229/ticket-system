# 🧪 FastAPI Toy Project

Python + FastAPI 기반의 CRUD 학습용 토이 프로젝트입니다.

---

## 📁 프로젝트 구조

toy-project/
├── app/
│ ├── main.py # FastAPI 진입점
│ ├── api/ # API 라우터
│ ├── models/ # SQLAlchemy 모델
│ ├── schemas/ # Pydantic 스키마
│ ├── crud/ # DB 작업 함수
│ ├── services/ # 서비스 로직
│ ├── db/ # DB 세션 설정
│ └── core/ # 설정 파일
├── requirements.txt # 의존성 목록
└── README.md # 실행 가이드


---

## 🚀 실행 방법

### 1. 가상환경 만들기 (선택)

```bash
python -m venv venv
.\venv\Scripts\activate      # Windows PowerShell
# source venv/bin/activate   # macOS/Linux
```

### 2. 패키지 설치
```bash
pip install -r requirements.txt
```

### 3. 환경 설정 (app/core/config.py)

```python
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/toy_users"
```

### 4. DB 테이블 생성 (자동 생성 방식)
```python
from app.models import user
user.Base.metadata.create_all(bind=engine)
```
### 5. 서버 실행
```python
uvicorn app.main:app --reload
```
실행 후 접속: http://127.0.0.1:8000/docs


### 🧪 테스트용 API 예시
```json
POST /users/
{
  "name": "홍길동",
  "email": "hong@example.com"
}
```

### ✅ 학습 포인트
- FastAPI 기본 구조
- SQLAlchemy 모델 및 세션
- Pydantic 데이터 검증
- 서비스 계층 분리 (services/)
- RESTful API 설계

### 💡 확장 아이디어
- JWT 로그인 기능 추가
- 게시판 or 티켓 예매 모델 추가
- 에러 처리 및 유효성 검증 강화