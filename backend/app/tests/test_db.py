from app.db.session import SessionLocal


def test_db_session_creation():
    db = SessionLocal()
    try:
        assert db is not None
    finally:
        db.close()
