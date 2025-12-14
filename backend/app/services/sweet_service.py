from sqlalchemy.orm import Session
from sqlalchemy import and_
from app.db.models import Sweet
from fastapi import HTTPException


def create_sweet(db: Session, data: dict):
    sweet = Sweet(**data)
    db.add(sweet)
    db.commit()
    db.refresh(sweet)
    return sweet

def get_all_sweets(db: Session):
    return db.query(Sweet).all()

def purchase_sweet(db: Session, sweet_id: int):
    sweet = db.query(Sweet).filter(Sweet.id == sweet_id).first()

    if not sweet:
        raise HTTPException(status_code=404, detail="Sweet not found")

    if sweet.quantity <= 0:
        raise HTTPException(status_code=400, detail="Out of stock")

    sweet.quantity -= 1
    db.commit()
    db.refresh(sweet)
    return sweet

def restock_sweet(db: Session, sweet_id: int, amount: int):
    sweet = db.query(Sweet).filter(Sweet.id == sweet_id).first()

    if not sweet:
        raise HTTPException(status_code=404, detail="Sweet not found")

    sweet.quantity += amount
    db.commit()
    db.refresh(sweet)
    return sweet

def search_sweets(
    db: Session,
    name: str | None = None,
    category: str | None = None,
    min_price: float | None = None,
    max_price: float | None = None,
):
    query = db.query(Sweet)

    if name:
        query = query.filter(Sweet.name.ilike(f"%{name}%"))

    if category:
        query = query.filter(Sweet.category == category)

    if min_price is not None:
        query = query.filter(Sweet.price >= min_price)

    if max_price is not None:
        query = query.filter(Sweet.price <= max_price)

    return query.all()