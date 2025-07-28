import pytest
from httpx import AsyncClient
from sqlalchemy.orm import Session
from app.main import app
from app.database import get_db, SessionLocal
from app.models.super_admin import SuperAdmin
from app.core.security import get_password_hash


@pytest.fixture
def db():
    """테스트용 데이터베이스 세션"""
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


@pytest.mark.asyncio
async def test_health_check():
    """헬스체크 엔드포인트 테스트"""
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/health")
    
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"
    assert "timestamp" in response.json()


@pytest.mark.asyncio
async def test_root():
    """루트 엔드포인트 테스트"""
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/")
    
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "version" in data
    assert data["message"] == "Exhibition Ticket System API"


@pytest.mark.asyncio
async def test_super_admin_login_failure():
    """잘못된 로그인 정보로 실패 테스트"""
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post(
            "/api/auth/super-admin/login",
            json={"username": "wrong", "password": "wrong"}
        )
    
    assert response.status_code == 401
    assert "Incorrect username or password" in response.json()["detail"]


@pytest.mark.asyncio
async def test_super_admin_login_success(db: Session):
    """슈퍼 관리자 로그인 성공 테스트"""
    # 테스트용 슈퍼 관리자 생성
    test_admin = SuperAdmin(
        username="testadmin",
        password_hash=get_password_hash("testpass123"),
        name="Test Admin",
        email="test@example.com",
        is_active=True
    )
    db.add(test_admin)
    db.commit()
    
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post(
            "/api/auth/super-admin/login",
            json={"username": "testadmin", "password": "testpass123"}
        )
    
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"
    
    # 테스트 데이터 정리
    db.delete(test_admin)
    db.commit()


@pytest.mark.asyncio
async def test_event_manager_login_failure():
    """이벤트 관리자 잘못된 로그인 테스트"""
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post(
            "/api/auth/event-manager/login",
            json={"username": "wrong", "password": "wrong"}
        )
    
    assert response.status_code == 401
    assert "Incorrect username or password" in response.json()["detail"]


@pytest.mark.asyncio
async def test_protected_endpoint_without_auth():
    """인증 없이 보호된 엔드포인트 접근 테스트"""
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/api/super-admin/events/")
    
    assert response.status_code in [403, 422]  # 인증 없이 접근 시 403 또는 422
