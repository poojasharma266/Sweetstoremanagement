from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.services.auth_service import create_user, authenticate_user
from app.core.security import create_access_token

router = APIRouter(prefix="/api/auth", tags=["auth"])

@router.post("/register", status_code=201)
def register(payload: dict, db: Session = Depends(get_db)):
    role = payload.get("role", "USER")  # ✅ SAFE

    user = create_user(
        db,
        payload["email"],
        payload["password"],
        role
    )

    return {
        "id": user.id,
        "email": user.email
    }

@router.post("/login")
def login(payload: dict, db: Session = Depends(get_db)):
    user = authenticate_user(db, payload["email"], payload["password"])
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}
