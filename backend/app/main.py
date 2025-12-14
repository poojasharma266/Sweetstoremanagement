from fastapi import FastAPI
from app.db.session import engine
from app.db.base import Base
from app.api.auth import router as auth_router
from app.api.sweets import router as sweets_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Pooja Sweet's shop", version="1.0.0")

Base.metadata.create_all(bind=engine)

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(auth_router)

app.include_router(sweets_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)