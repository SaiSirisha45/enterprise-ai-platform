from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.database.database import get_db
from backend.models.user import User
from backend.schemas.auth import RegisterRequest, LoginRequest
from backend.security.hash import hash_password, verify_password

from backend.performance.api_profiler import profiler
from backend.cache.cache_manager import cache

from monitoring.tracing import tracer
from monitoring.logging import logger

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


# ==========================================================
# Register
# ==========================================================

@router.post("/register")
@profiler.profile
def register(
    request: RegisterRequest,
    db: Session = Depends(get_db)
):

    with tracer.start_as_current_span("User Registration"):

        logger.info(
            "Registration Request",
            extra={"email": request.email}
        )

        existing_user = (
            db.query(User)
            .filter(User.email == request.email)
            .first()
        )

        if existing_user:

            logger.warning(
                "Registration Failed",
                extra={"email": request.email}
            )

            return {
                "error": "Email already registered"
            }

        hashed_password = hash_password(request.password)

        new_user = User(
            name=request.name,
            email=request.email,
            password=hashed_password,
            role="user"
        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        logger.info(
            "User Registered Successfully",
            extra={"user_id": new_user.id}
        )

        return {
            "message": "User registered successfully"
        }


# ==========================================================
# Login
# ==========================================================

@router.post("/login")
@profiler.profile
def login(
    request: LoginRequest,
    db: Session = Depends(get_db)
):

    with tracer.start_as_current_span("User Login"):

        logger.info(
            "Login Attempt",
            extra={"email": request.email}
        )

        user = (
            db.query(User)
            .filter(User.email == request.email)
            .first()
        )

        if not user:

            logger.warning(
                "Login Failed - User Not Found",
                extra={"email": request.email}
            )

            return {
                "error": "Invalid email or password"
            }

        if not verify_password(
            request.password,
            user.password
        ):

            logger.warning(
                "Login Failed - Invalid Password",
                extra={"email": request.email}
            )

            return {
                "error": "Invalid email or password"
            }

        response = {
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

        # Cache user session for 1 hour
        cache.cache_session(
            user.id,
            response,
            ttl=3600
        )

        logger.info(
            "Login Success",
            extra={
                "user_id": user.id,
                "role": user.role
            }
        )

        return response


# ==========================================================
# User Profile
# ==========================================================

@router.get("/profile/{user_id}")
@profiler.profile
def get_profile(
    user_id: int,
    db: Session = Depends(get_db)
):

    with tracer.start_as_current_span("Get User Profile"):

        # Check Redis cache first
        cached_profile = cache.get_user_profile(user_id)

        if cached_profile:

            logger.info(
                "User Profile Loaded From Redis",
                extra={"user_id": user_id}
            )

            return {
                "source": "redis",
                "data": cached_profile
            }

        # Load from database
        user = (
            db.query(User)
            .filter(User.id == user_id)
            .first()
        )

        if not user:

            logger.warning(
                "User Not Found",
                extra={"user_id": user_id}
            )

            return {
                "error": "User not found"
            }

        profile = {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "role": user.role
        }

        # Cache profile for 30 minutes
        cache.cache_user_profile(
            user.id,
            profile,
            ttl=1800
        )

        logger.info(
            "User Profile Cached",
            extra={"user_id": user.id}
        )

        return {
            "source": "database",
            "data": profile
        } 