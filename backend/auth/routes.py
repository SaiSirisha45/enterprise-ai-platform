from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.database import get_db
from models.user import User
from schemas.auth import RegisterRequest, LoginRequest
from security.hash import hash_password, verify_password

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register")
def register(request: RegisterRequest, db: Session = Depends(get_db)):

    print("========== REGISTER ==========")
    print("STEP 1")

    existing_user = db.query(User).filter(
        User.email == request.email
    ).first()

    print("STEP 2")

    if existing_user:
        print("Email already exists")
        return {
            "error": "Email already registered"
        }

    print("STEP 3")

    hashed_password = hash_password(request.password)

    print("STEP 4")
    print("HASH:", hashed_password)

    new_user = User(
        name=request.name,
        email=request.email,
        password=hashed_password,
        role="user"
    )

    print("STEP 5")

    db.add(new_user)

    print("STEP 6")

    db.commit()

    print("STEP 7")

    db.refresh(new_user)

    print("STEP 8")
    print("REGISTER SUCCESS")

    return {
        "message": "User registered successfully"
    }


@router.post("/login")
def login(request: LoginRequest, db: Session = Depends(get_db)):

    print("========== LOGIN ==========")

    user = db.query(User).filter(
        User.email == request.email
    ).first()

    if not user:
        return {
            "error": "Invalid email or password"
        }

    print("User Found")

    print("Stored Password:")
    print(user.password)

    print("Entered Password:")
    print(request.password)

    if not verify_password(
        request.password,
        user.password
    ):
        return {
            "error": "Invalid email or password"
        }

    print("LOGIN SUCCESS")

    return {
        "access_token": "demo-access-token",
        "refresh_token": "demo-refresh-token",
        "token_type": "bearer",
        "user": {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "role": user.role
        }
    } 