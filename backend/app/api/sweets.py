from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.db.models import User
from app.api.deps import( 
    get_db, 
    get_current_user, 
    get_current_admin
)
from app.services.sweet_service import (
    create_sweet,
    get_all_sweets,
    purchase_sweet,
    restock_sweet,
    search_sweets
)
from typing import Optional
from app.schemas.sweet import RestockRequest

router = APIRouter(
    prefix="/api/sweets",
    tags=["sweets"]
)

@router.post("", status_code=201)
def add_sweet(
    payload: dict,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return create_sweet(db, payload)

@router.get("", dependencies=[Depends(get_current_user)])
def list_sweets(
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return get_all_sweets(db)

@router.post("/{sweet_id}/purchase")
def purchase(
    sweet_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return purchase_sweet(db, sweet_id)

@router.post("/{sweet_id}/restock")
def restock(
    sweet_id: int,
    payload: RestockRequest,
    db: Session = Depends(get_db),
    admin: User =Depends(get_current_admin)  # 🔒 ONLY ADMIN
):
    return restock_sweet(db, sweet_id, payload.amount)
@router.get("/search")
def search(
    name: Optional[str] = None,
    category: Optional[str] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
    db: Session = Depends(get_db),
):
    return search_sweets(db, name, category, min_price, max_price)