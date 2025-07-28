"""
Week 2 - Day 3: FastAPI 첫 걸음

PHP 웹 개발과 FastAPI 비교
"""

# FastAPI 임포트
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

# FastAPI 앱 생성 (PHP의 index.php와 유사)
app = FastAPI(
    title="티켓 예약 API",
    description="전시회 티켓 예약 시스템 API",
    version="1.0.0"
)

# === 1. 기본 라우팅 ===
# PHP:
# Route::get('/', function() {
#     return "Hello World";
# });

@app.get("/")
def read_root():
    """루트 엔드포인트"""
    return {"message": "Hello FastAPI!"}


# === 2. 경로 매개변수 ===
# PHP: Route::get('/users/{id}', ...)
@app.get("/users/{user_id}")
def read_user(user_id: int):
    """사용자 조회"""
    return {"user_id": user_id, "name": f"User {user_id}"}


# === 3. 쿼리 매개변수 ===
# PHP: $_GET['skip'], $_GET['limit']
@app.get("/items/")
def read_items(skip: int = 0, limit: int = 10):
    """아이템 목록 조회"""
    items = [{"id": i, "name": f"Item {i}"} for i in range(skip, skip + limit)]
    return {"items": items, "total": 100}


# === 4. Pydantic 모델 (요청/응답 데이터 검증) ===
# PHP에서는 직접 검증해야 하지만, FastAPI는 자동으로!

class UserCreate(BaseModel):
    """사용자 생성 요청 모델"""
    username: str
    email: str
    age: int
    is_active: bool = True

class UserResponse(BaseModel):
    """사용자 응답 모델"""
    id: int
    username: str
    email: str
    created_at: datetime
    is_active: bool


# === 5. POST 요청 처리 ===
# PHP: $_POST 또는 json_decode(file_get_contents('php://input'))

# 가짜 데이터베이스
fake_users_db = []

@app.post("/users/", response_model=UserResponse)
def create_user(user: UserCreate):
    """사용자 생성"""
    # 새 사용자 생성
    new_user = {
        "id": len(fake_users_db) + 1,
        "username": user.username,
        "email": user.email,
        "created_at": datetime.now(),
        "is_active": user.is_active
    }
    fake_users_db.append(new_user)
    return new_user


# === 6. PUT 요청 (수정) ===
class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    is_active: Optional[bool] = None

@app.put("/users/{user_id}")
def update_user(user_id: int, user_update: UserUpdate):
    """사용자 정보 수정"""
    # 실제로는 DB에서 조회
    if user_id > len(fake_users_db):
        raise HTTPException(status_code=404, detail="User not found")
    
    # 업데이트 로직
    return {"message": f"User {user_id} updated", "data": user_update}


# === 7. DELETE 요청 ===
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    """사용자 삭제"""
    if user_id > len(fake_users_db):
        raise HTTPException(status_code=404, detail="User not found")
    
    return {"message": f"User {user_id} deleted"}


# === 8. 상태 코드와 에러 처리 ===
from fastapi import status

@app.post("/login", status_code=status.HTTP_200_OK)
def login(username: str, password: str):
    """로그인 처리"""
    # PHP: if (!$valid) { http_response_code(401); }
    if username != "admin" or password != "1234":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return {"access_token": "fake-token", "token_type": "bearer"}


# === 9. 리스트 응답 ===
@app.get("/events/", response_model=List[dict])
def get_events():
    """이벤트 목록 조회"""
    events = [
        {"id": 1, "name": "전시회 A", "date": "2024-03-01"},
        {"id": 2, "name": "전시회 B", "date": "2024-03-15"},
    ]
    return events


# === 10. 파일 업로드 ===
from fastapi import File, UploadFile

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    """파일 업로드"""
    # PHP: $_FILES['file']
    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "size": file.size
    }


# === 실행 방법 ===
# 터미널에서: uvicorn main:app --reload
# 
# PHP와 차이점:
# 1. Apache/Nginx 설정 불필요
# 2. 자동 API 문서: http://localhost:8000/docs
# 3. 타입 검증 자동
# 4. 비동기 지원 (async/await)

if __name__ == "__main__":
    import uvicorn
    print("""
    FastAPI 서버 실행 방법:
    
    1. 터미널에서:
       uvicorn main:app --reload
    
    2. 브라우저에서:
       - API 문서: http://localhost:8000/docs
       - 대체 문서: http://localhost:8000/redoc
       - 루트: http://localhost:8000/
    
    3. 테스트:
       - GET: curl http://localhost:8000/users/1
       - POST: curl -X POST http://localhost:8000/users/ \\
               -H "Content-Type: application/json" \\
               -d '{"username":"test","email":"test@test.com","age":25}'
    """)
    
    # 코드로 직접 실행할 때
    # uvicorn.run(app, host="0.0.0.0", port=8000)
