# 전시회 티켓 예약 시스템 - 백엔드 설치 가이드

## 📋 사전 요구사항

- Python 3.12+
- PostgreSQL 14+
- Redis 6+ (또는 Windows의 경우 Memurai)
- Git

## 🚀 설치 및 실행 가이드

### 1. 프로젝트 클론 및 디렉토리 이동

```bash
git clone [repository-url]
cd ticket-system/backend
```

### 2. Python 가상환경 생성 및 활성화

```bash
# Linux/Mac
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. 패키지 설치

```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

### 4. 환경변수 설정

```bash
# .env 파일 생성 (이미 있다면 수정)
cp .env.example .env

# .env 파일 편집하여 데이터베이스 정보 수정
# DATABASE_URL=postgresql+psycopg2://ticket_user:1234@localhost/ticket_system
```

### 5. PostgreSQL 데이터베이스 생성

```bash
# PostgreSQL 접속
psql -U postgres

# 사용자 생성 (이미 있다면 생략)
CREATE USER ticket_user WITH PASSWORD '1234';

# 데이터베이스 생성
DROP DATABASE IF EXISTS ticket_system;
CREATE DATABASE ticket_system OWNER ticket_user;

# 권한 부여
GRANT ALL PRIVILEGES ON DATABASE ticket_system TO ticket_user;
\q
```

### 6. 데이터베이스 마이그레이션

```bash
# 기존 마이그레이션 파일 삭제 (있다면)
rm -rf alembic/versions/*

# 초기 마이그레이션 생성
alembic revision --autogenerate -m "Initial migration"

# 마이그레이션 적용
alembic upgrade head
```

### 7. 초기 데이터 생성

```bash
# 테스트용 초기 데이터 생성
python scripts/create_initial_data.py
```

생성되는 테스트 계정:
- 슈퍼 관리자: `admin` / `admin1234`
- 이벤트 관리자: `manager` / `manager1234`

### 8. 개발 서버 실행

```bash
# 개발 서버 시작
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# 또는 특정 호스트/포트 지정
uvicorn app.main:app --reload --host localhost --port 8001
```

### 9. API 문서 확인

브라우저에서 다음 주소로 접속:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 🧪 동작 테스트

### 1. 헬스체크
```bash
curl http://localhost:8000/health
```

### 2. 슈퍼 관리자 로그인
```bash
curl -X POST http://localhost:8000/api/auth/super-admin/login \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "admin1234"}'
```

### 3. 이벤트 관리자 로그인
```bash
curl -X POST http://localhost:8000/api/auth/event-manager/login \
  -H "Content-Type: application/json" \
  -d '{"username": "manager", "password": "manager1234"}'
```

## 🔧 문제 해결

### Redis 연결 오류
- Redis 서비스가 실행 중인지 확인: `redis-cli ping`
- Windows의 경우 Memurai 서비스 확인

### PostgreSQL 연결 오류
- PostgreSQL 서비스 실행 확인
- 데이터베이스 이름, 사용자명, 비밀번호 확인
- `.env` 파일의 DATABASE_URL 확인

### 마이그레이션 오류
```bash
# Alembic 히스토리 초기화
alembic stamp head

# 또는 데이터베이스 완전 초기화 후 재시도
```

## 📝 개발 팁

### 새로운 모델 추가 시
1. `app/models/` 디렉토리에 모델 파일 생성
2. `app/models/__init__.py`에 import 추가
3. 마이그레이션 생성: `alembic revision --autogenerate -m "Add new model"`
4. 마이그레이션 적용: `alembic upgrade head`

### API 엔드포인트 추가 시
1. 해당 라우터 파일에 엔드포인트 추가
2. 필요한 경우 스키마 파일 생성/수정
3. 서비스 로직은 `app/services/`에 구현

## 🚨 주의사항

- 프로덕션 환경에서는 `.env` 파일의 SECRET_KEY를 반드시 변경하세요
- 개발 환경에서만 DEBUG=True를 사용하세요
- 실제 결제 API 키는 별도로 관리하세요
