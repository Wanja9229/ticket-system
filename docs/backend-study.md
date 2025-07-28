# PHP 개발자를 위한 Python/FastAPI 4주 스터디

> **대상**: PHP 개발 경험 3년 이상  
> **목표**: Python + FastAPI로 실무 프로젝트 참여 가능  
> **일정**: 4주 (주 2회, 화/목)  
> **시간**: 회당 2-3시간  

## 📋 전체 커리큘럼

| 주차 | 일정 | 주제 | 목표 |
|------|------|------|------|
| 1주차 | 화/목 | Python 속성 코스 | PHP와 비교하며 Python 핵심 익히기 |
| 2주차 | 화/목 | FastAPI 기초 | REST API 개발 시작 |
| 3주차 | 화/목 | DB 연동과 ORM | SQLAlchemy로 CRUD 구현 |
| 4주차 | 화/목 | 인증과 실전 | JWT 인증, 프로젝트 구조 이해 |

---

## 🐍 1주차: Python 속성 코스

### Day 1 (화요일) - Python vs PHP
**학습 목표**: PHP 개발자 관점에서 Python 이해하기

#### 핵심 비교
```php
// PHP
$name = "홍길동";
$users = array("김", "이", "박");
$user = array("name" => "김철수", "age" => 30);

function get_user($id) {
    return "User " . $id;
}
```

```python
# Python (위와 동일한 코드)
name = "홍길동"
users = ["김", "이", "박"]
user = {"name": "김철수", "age": 30}

def get_user(id):
    return f"User {id}"
```

#### 실습 내용
1. Python 설치 및 가상환경 설정
2. 변수, 자료형, 함수 기초
3. 조건문, 반복문 (들여쓰기 주의!)
4. 리스트와 딕셔너리 다루기
5. **과제**: PHP 함수 5개를 Python으로 변환

### Day 2 (목요일) - Python 클래스와 모듈
**학습 목표**: 객체지향과 모듈 시스템 이해

#### PHP vs Python 클래스
```php
// PHP
class User {
    private $name;
    
    public function __construct($name) {
        $this->name = $name;
    }
    
    public function getName() {
        return $this->name;
    }
}
```

```python
# Python
class User:
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        return self.name
```

#### 실습 내용
1. 클래스 정의와 상속
2. 모듈 import 시스템
3. 예외 처리 (try/except)
4. 파일 읽기/쓰기, JSON 처리
5. **과제**: User 클래스 만들고 CRUD 메서드 구현

---

## ⚡ 2주차: FastAPI 시작하기

### Day 3 (화요일) - 첫 API 만들기
**학습 목표**: FastAPI로 REST API 개발 시작

#### 기본 구조
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/users/{user_id}")
def read_user(user_id: int):
    return {"user_id": user_id}

@app.post("/users")
def create_user(name: str, email: str):
    return {"name": name, "email": email}
```

#### 실습 내용
1. FastAPI 설치 및 프로젝트 생성
2. GET, POST, PUT, DELETE 구현
3. 경로 매개변수와 쿼리 매개변수
4. uvicorn으로 서버 실행
5. **과제**: 간단한 게시판 API (목록, 상세, 등록)

### Day 4 (목요일) - 데이터 검증과 문서화
**학습 목표**: Pydantic으로 데이터 검증하기

#### Pydantic 모델
```python
from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    name: str
    email: str
    age: Optional[int] = None

@app.post("/users")
def create_user(user: UserCreate):
    return user
```

#### 실습 내용
1. Pydantic 모델 정의
2. 요청/응답 검증
3. 에러 처리
4. 자동 API 문서 (Swagger UI)
5. **과제**: 회원가입/로그인 API 구현

---

## 🗄️ 3주차: 데이터베이스 실전

### Day 5 (화요일) - SQLAlchemy 기초
**학습 목표**: ORM으로 데이터베이스 다루기

#### 모델 정의
```python
from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(100), unique=True)
```

#### 실습 내용
1. PostgreSQL 연결 설정
2. 모델 정의와 마이그레이션
3. 세션 관리
4. 기본 CRUD 작업
5. **과제**: Event, Ticket 모델 생성

### Day 6 (목요일) - CRUD 완성
**학습 목표**: 실제 사용 가능한 API 만들기

#### CRUD 함수
```python
def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def create_user(db: Session, user: UserCreate):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    return db_user
```

#### 실습 내용
1. Repository 패턴 구현
2. 복잡한 쿼리 (JOIN, 필터링)
3. 페이지네이션
4. 트랜잭션 처리
5. **과제**: 전체 User CRUD API 완성

---

## 🔐 4주차: 인증과 프로젝트 구조

### Day 7 (화요일) - JWT 인증
**학습 목표**: 보안 구현하기

#### JWT 구현
```python
from jose import jwt
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"])

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict):
    return jwt.encode(data, SECRET_KEY, algorithm="HS256")
```

#### 실습 내용
1. 비밀번호 해싱
2. JWT 토큰 생성/검증
3. 인증 미들웨어
4. 권한 관리
5. **과제**: 로그인/로그아웃 구현

### Day 8 (목요일) - 프로젝트 구조 이해
**학습 목표**: 실제 프로젝트 참여 준비

#### 프로젝트 구조
```
backend/
├── app/
│   ├── api/         # 라우터
│   ├── core/        # 설정, 보안
│   ├── models/      # DB 모델
│   ├── schemas/     # Pydantic 스키마
│   ├── services/    # 비즈니스 로직
│   └── main.py      # 진입점
├── tests/           # 테스트
└── requirements.txt # 패키지 목록
```

#### 실습 내용
1. 실제 프로젝트 코드 분석
2. 환경 변수 관리
3. 로깅 시스템
4. Git 협업 방법
5. **최종 과제**: 기존 프로젝트에 기능 추가

---

## 💡 PHP 개발자를 위한 꿀팁

### 1. 자주 헷갈리는 문법
| 설명 | PHP | Python |
|------|-----|--------|
| 변수 선언 | `$var = 1;` | `var = 1` |
| 배열/리스트 | `array(1,2,3)` | `[1, 2, 3]` |
| 연관배열/딕셔너리 | `array("a"=>1)` | `{"a": 1}` |
| 문자열 결합 | `"Hi " . $name` | `f"Hi {name}"` |
| null 체크 | `is_null($var)` | `var is None` |
| 배열 길이 | `count($arr)` | `len(arr)` |

### 2. 자주 쓰는 패턴
```python
# PHP의 foreach와 비슷
for user in users:
    print(user.name)

# PHP의 array_map과 비슷  
names = [user.name for user in users]

# PHP의 array_filter와 비슷
adults = [user for user in users if user.age >= 18]
```

### 3. 주의사항
- **들여쓰기가 문법임** (스페이스 4개 권장)
- **self는 명시적으로 써야 함** (PHP의 $this)
- **True/False/None** 첫 글자 대문자
- **문장 끝에 세미콜론 없음**

---

## 🎯 4주 후 달성 가능한 것

✅ Python 기본 문법 이해  
✅ FastAPI로 REST API 개발  
✅ PostgreSQL + SQLAlchemy 사용  
✅ JWT 인증 구현  
✅ 프로젝트 코드 읽고 수정  
✅ 새로운 기능 추가 가능  

---

## 📚 추천 학습 자료

1. **FastAPI 공식 문서** - https://fastapi.tiangolo.com/ko/
2. **Python for PHP Developers** 검색
3. **Real Python** - 실전 예제 많음
4. **이 프로젝트의 실제 코드** 분석

---

## 🔥 성공 전략

1. **완벽하게 이해하려 하지 말고 일단 따라하기**
2. **PHP 코드를 Python으로 변환하는 연습**
3. **매일 30분씩이라도 코드 작성**
4. **모르는 건 바로 ChatGPT에 물어보기**
5. **실제 프로젝트 코드 많이 읽기**

---

**기억하세요**: PHP 개발 경험이 있다면 개념은 이미 아는 것! 문법만 익히면 됩니다. 화이팅! 💪
