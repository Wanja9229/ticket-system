from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.dependencies import get_current_event_manager
from app.models.event_manager import EventManager

router = APIRouter()


@router.get("/")
async def get_products(
    db: Session = Depends(get_db),
    current_manager: EventManager = Depends(get_current_event_manager)
):
    """이벤트의 상품 목록 조회"""
    # TODO: Implement product list logic
    return {"message": "Product list", "event_id": current_manager.event_id}


@router.post("/")
async def create_product(
    db: Session = Depends(get_db),
    current_manager: EventManager = Depends(get_current_event_manager)
):
    """새 상품 생성"""
    # TODO: Implement product creation logic
    return {"message": "Product created"}
