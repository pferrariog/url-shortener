from datetime import datetime
from typing import Generator

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

from ..settings import settings


base = declarative_base()


class UrlModel(base):
    """Url database table fields"""

    __tablename__ = "url"
    id = Column(Integer, primary_key=True, autoincrement=True)
    original_url = Column(String)
    reference_code = Column(String)
    creation_date = Column(DateTime, default=datetime.now())


def get_db_connection() -> Generator:
    """Get the database"""
    engine = create_engine(settings.DATABASE_URL)
    session = sessionmaker(bind=engine)
    yield session()
