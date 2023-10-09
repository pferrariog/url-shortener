from fastapi.testclient import TestClient
from pytest import fixture
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from url_shortener.app import app
from url_shortener.extensions.database import UrlModel
from url_shortener.extensions.database import get_db_connection


@fixture
def session():
    engine = create_engine("sqlite:///:memory:", connect_args={"check_same_thread": False}, poolclass=StaticPool)
    UrlModel.metadata.create_all(engine)
    Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    yield Session()
    UrlModel.metadata.drop_all(engine)


@fixture
def client(session):
    def get_connection_override():
        return session

    with TestClient(app) as client:
        app.dependency_overrides[get_db_connection] = get_connection_override
        yield client

    app.dependency_overrides.clear()


@fixture
def url(session):
    url = UrlModel(original_url="http://teste.com", reference_code="teste")
    session.add(url)
    session.commit()
    session.refresh(url)
    return url
