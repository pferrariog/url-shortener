import pytest

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from url_shortener.app import app
from url_shortener.extensions.database import UrlModel
from url_shortener.extensions.database import get_db_connection


@pytest.fixture
def session():
    engine = create_engine("sqlite:///:memory:")
    Session = sessionmaker(bind=engine)
    UrlModel.metadata.create_all(engine)
    yield Session()
    UrlModel.metadata.drop_all(engine)


@pytest.fixture
def client(session):
    def get_connection_override():
        return session

    with TestClient(app) as client:
        app.dependency_overrides[get_db_connection] = get_connection_override
        yield client

    app.dependency_overrides.clear()
