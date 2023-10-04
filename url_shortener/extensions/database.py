from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session


base = declarative_base()
db_url = ""  # set environment manager like dynaconf


class UrlModel(base):
    """Url database table fields"""

    __tablename__ = "url"
    id = Column(Integer, primary_key=True, autoincrement=True)
    original_url = Column(String)
    reference_code = Column(String)
    creation_date = Column(DateTime, default=datetime.now)


def get_db_connection():
    """Get the database"""
    engine = create_engine(db_url)
    with Session(engine) as session:
        yield session()
