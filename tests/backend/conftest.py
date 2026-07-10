import pytest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from backend.database.database import Base, get_db
from backend.models.user import User
from backend.main import app


TEST_DATABASE_URL = "sqlite:///./test_database.db"


engine = create_engine(
    TEST_DATABASE_URL,
    connect_args={
        "check_same_thread": False
    }
)


TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


@pytest.fixture(autouse=True)
def setup_test_database():

    # Create tables
    Base.metadata.create_all(bind=engine)

    def override_get_db():

        db = TestingSessionLocal()

        try:
            yield db

        finally:
            db.close()


    app.dependency_overrides[get_db] = override_get_db


    yield


    # Remove tables after test
    Base.metadata.drop_all(bind=engine)

    app.dependency_overrides.clear() 