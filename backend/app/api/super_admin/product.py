from fastapi import APIRouter, Depends, HTTPException, status, Query, Path
from sqlalchemy.orm import Session
from typing import List, Optional
import math

from app.database import get_db
from app.dependencies import get_current_super_admin
from app.models.super_admin import SuperAdmin
from app.models.product import Product, ProductOption
from app.models.event import Event
from app.schemas.product import (
    ProductCreate, ProductUpdate, ProductResponse, ProductListResponse,
    ProductOptionCreate, ProductOptionUpdate, ProductOptionResponse
)

router = APIRouter()


@router.get("/", response_model=ProductListResponse)
async def get_products(
    page: int = Query(1, ge=1, description="페이지 번호"),
    size: int = Query(10, ge=1, le=100, description="페이지 크기"),
    db: Session = Depends(get_db),
    current_admin: SuperAdmin = Depends(get_current_super_admin)
):
    """상품 목록 조회"""
    try:
        # 기본 쿼리
        query = db.query(Product).filter(Product.is_deleted == 'N')
        
        # 전체 개수
        total = query.count()
        
        # 페이지네이션
        skip = (page - 1) * size
        products = query.offset(skip).limit(size).all()
        
        pages = math.ceil(total / size)
        
        return ProductListResponse(
            items=products,
            total=total,
            page=page,
            size=size,
            pages=pages
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="상품 목록 조회 중 오류가 발생했습니다"
        )


@router.post("/", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
async def create_product(
    product_data: ProductCreate,
    db: Session = Depends(get_db),
    current_admin: SuperAdmin = Depends(get_current_super_admin)
):
    """새 상품 생성"""
    try:
        # 이벤트 존재 확인
        event = db.query(Event).filter(Event.id == product_data.event_id).first()
        if not event:
            raise HTTPException(status_code=404, detail="이벤트를 찾을 수 없습니다")
        
        # 상품 생성
        db_product = Product(
            event_id=product_data.event_id,
            name=product_data.name,
            description=product_data.description,
            base_price=product_data.base_price,
            base_stock=product_data.base_stock,
            current_stock=product_data.current_stock,
            is_active=product_data.is_active,
            created_by=current_admin.id
        )
        
        db.add(db_product)
        db.commit()
        db.refresh(db_product)
        
        return db_product
        
    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="상품 생성 중 오류가 발생했습니다"
        )


@router.get("/{product_id}", response_model=ProductResponse)
async def get_product(
    product_id: int = Path(..., description="상품 ID"),
    db: Session = Depends(get_db),
    current_admin: SuperAdmin = Depends(get_current_super_admin)
):
    """특정 상품 조회"""
    product = db.query(Product).filter(
        Product.id == product_id,
        Product.is_deleted == 'N'
    ).first()
    
    if not product:
        raise HTTPException(status_code=404, detail="상품을 찾을 수 없습니다")
    
    return product


@router.put("/{product_id}", response_model=ProductResponse)
async def update_product(
    product_id: int = Path(..., description="상품 ID"),
    product_data: ProductUpdate,
    db: Session = Depends(get_db),
    current_admin: SuperAdmin = Depends(get_current_super_admin)
):
    """상품 정보 수정"""
    try:
        # 상품 존재 확인
        db_product = db.query(Product).filter(
            Product.id == product_id,
            Product.is_deleted == 'N'
        ).first()
        
        if not db_product:
            raise HTTPException(status_code=404, detail="상품을 찾을 수 없습니다")
        
        # 필드 업데이트 (None이 아닌 값만)
        update_data = product_data.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_product, field, value)
        
        db.commit()
        db.refresh(db_product)
        
        return db_product
        
    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="상품 수정 중 오류가 발생했습니다"
        )


@router.delete("/{product_id}")
async def delete_product(
    product_id: int = Path(..., description="상품 ID"),
    db: Session = Depends(get_db),
    current_admin: SuperAdmin = Depends(get_current_super_admin)
):
    """상품 삭제 (소프트 삭제)"""
    try:
        db_product = db.query(Product).filter(
            Product.id == product_id,
            Product.is_deleted == 'N'
        ).first()
        
        if not db_product:
            raise HTTPException(status_code=404, detail="상품을 찾을 수 없습니다")
        
        # 소프트 삭제
        db_product.is_deleted = 'Y'
        db_product.is_active = False
        
        db.commit()
        
        return {"message": f"상품 '{db_product.name}'이(가) 삭제되었습니다"}
        
    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="상품 삭제 중 오류가 발생했습니다"
        )


# ============ Product Option APIs ============

@router.post("/{product_id}/options", response_model=ProductOptionResponse, status_code=status.HTTP_201_CREATED)
async def create_product_option(
    product_id: int = Path(..., description="상품 ID"),
    option_data: ProductOptionCreate,
    db: Session = Depends(get_db),
    current_admin: SuperAdmin = Depends(get_current_super_admin)
):
    """상품 옵션 생성"""
    try:
        # 상품 존재 확인
        product = db.query(Product).filter(
            Product.id == product_id,
            Product.is_deleted == 'N'
        ).first()
        
        if not product:
            raise HTTPException(status_code=404, detail="상품을 찾을 수 없습니다")
        
        # 옵션 생성
        db_option = ProductOption(
            product_id=product_id,
            option_name=option_data.option_name,
            price_adjustment=option_data.price_adjustment,
            stock_quantity=option_data.stock_quantity,
            current_stock=option_data.current_stock,
            is_active=option_data.is_active
        )
        
        db.add(db_option)
        db.commit()
        db.refresh(db_option)
        
        return db_option
        
    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="상품 옵션 생성 중 오류가 발생했습니다"
        )


@router.put("/options/{option_id}", response_model=ProductOptionResponse)
async def update_product_option(
    option_id: int = Path(..., description="옵션 ID"),
    option_data: ProductOptionUpdate,
    db: Session = Depends(get_db),
    current_admin: SuperAdmin = Depends(get_current_super_admin)
):
    """상품 옵션 수정"""
    try:
        db_option = db.query(ProductOption).filter(
            ProductOption.id == option_id,
            ProductOption.is_deleted == 'N'
        ).first()
        
        if not db_option:
            raise HTTPException(status_code=404, detail="상품 옵션을 찾을 수 없습니다")
        
        # 필드 업데이트
        update_data = option_data.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_option, field, value)
        
        db.commit()
        db.refresh(db_option)
        
        return db_option
        
    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="상품 옵션 수정 중 오류가 발생했습니다"
        )


@router.delete("/options/{option_id}")
async def delete_product_option(
    option_id: int = Path(..., description="옵션 ID"),
    db: Session = Depends(get_db),
    current_admin: SuperAdmin = Depends(get_current_super_admin)
):
    """상품 옵션 삭제"""
    try:
        db_option = db.query(ProductOption).filter(
            ProductOption.id == option_id,
            ProductOption.is_deleted == 'N'
        ).first()
        
        if not db_option:
            raise HTTPException(status_code=404, detail="상품 옵션을 찾을 수 없습니다")
        
        # 소프트 삭제
        db_option.is_deleted = 'Y'
        db_option.is_active = False
        
        db.commit()
        
        return {"message": f"상품 옵션 '{db_option.option_name}'이(가) 삭제되었습니다"}
        
    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="상품 옵션 삭제 중 오류가 발생했습니다"
        )
