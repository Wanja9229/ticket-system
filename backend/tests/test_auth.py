import pytest
from fastapi.testclient import TestClient


def test_root_endpoint(client: TestClient):
    """Test root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "version" in data


def test_health_endpoint(client: TestClient):
    """Test health check endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "timestamp" in data


def test_super_admin_login_invalid(client: TestClient):
    """Test super admin login with invalid credentials"""
    response = client.post(
        "/api/auth/super-admin/login",
        json={"username": "invalid", "password": "invalid"}
    )
    assert response.status_code == 401
