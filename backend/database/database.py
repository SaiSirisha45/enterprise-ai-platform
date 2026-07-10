from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# OpenTelemetry SQLAlchemy Instrumentation
from opentelemetry.instrumentation.sqlalchemy import SQLAlchemyInstrumentor

# ==========================================
# Database Configuration
# ==========================================

DATABASE_URL = "sqlite:///./enterprise_ai.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
)

# Automatically trace all SQLAlchemy queries
SQLAlchemyInstrumentor().instrument(engine=engine)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

Base = declarative_base()


# ==========================================
# Database Dependency
# ==========================================

def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close() 