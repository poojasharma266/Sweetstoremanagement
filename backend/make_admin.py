from app.db.session import SessionLocal
from app.db.models import User

db = SessionLocal()

user = db.query(User).filter(User.email == "admin@test.com").first()

if not user:
    print("User not found")
else:
    user.role = "ADMIN"
    db.commit()
    print(f"{user.email} promoted to ADMIN")

db.close()
