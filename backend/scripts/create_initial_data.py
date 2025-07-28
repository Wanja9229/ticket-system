"""
초기 데이터 생성 스크립트
슈퍼 관리자와 테스트 이벤트를 생성합니다.
"""

import asyncio
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from app.models.super_admin import SuperAdmin
from app.models.event import Event
from app.models.event_manager import EventManager
from app.core.security import get_password_hash
from datetime import datetime, timedelta
import uuid


def create_initial_data():
    db = SessionLocal()
    
    try:
        # 1. 슈퍼 관리자 생성
        super_admin = db.query(SuperAdmin).filter(
            SuperAdmin.username == "admin"
        ).first()
        
        if not super_admin:
            super_admin = SuperAdmin(
                id=str(uuid.uuid4()),
                username="admin",
                password_hash=get_password_hash("admin1234"),
                name="시스템 관리자",
                email="admin@example.com",
                is_active=True
            )
            db.add(super_admin)
            print("✅ 슈퍼 관리자 생성 완료")
        else:
            print("ℹ️ 슈퍼 관리자가 이미 존재합니다")
        
        # 2. 테스트 이벤트 생성
        test_event = db.query(Event).filter(
            Event.code == "TEST2024"
        ).first()
        
        if not test_event:
            test_event = Event(
                id=str(uuid.uuid4()),
                code="TEST2024",
                name="2024 테스트 전시회",
                description="시스템 테스트를 위한 전시회입니다.",
                location="서울특별시 강남구 테스트홀",
                start_date=datetime.now(),
                end_date=datetime.now() + timedelta(days=30),
                is_active=True,
                is_deleted=False,
                max_tickets_per_order=4
            )
            db.add(test_event)
            db.commit()  # 이벤트를 먼저 커밋
            print("✅ 테스트 이벤트 생성 완료")
            
            # 3. 이벤트 관리자 생성
            event_manager = EventManager(
                id=str(uuid.uuid4()),
                event_id=test_event.id,
                username="manager",
                password_hash=get_password_hash("manager1234"),
                name="이벤트 매니저",
                email="manager@example.com",
                phone="010-1234-5678",
                permission_level=2,
                is_active=True
            )
            db.add(event_manager)
            print("✅ 이벤트 관리자 생성 완료")
        else:
            print("ℹ️ 테스트 이벤트가 이미 존재합니다")
        
        db.commit()
        print("\n✨ 초기 데이터 생성 완료!")
        print("\n📌 로그인 정보:")
        print("- 슈퍼 관리자: admin / admin1234")
        print("- 이벤트 관리자: manager / manager1234")
        
    except Exception as e:
        print(f"❌ 오류 발생: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    print("🚀 초기 데이터 생성 시작...")
    create_initial_data()
