from random import sample
from string import ascii_lowercase
from string import ascii_uppercase
from string import digits

from database import UrlModel
from sqlalchemy import or_
from sqlalchemy.orm import Session


def create_url_reference_code() -> str:
    """Create a reference code with ascii characters"""
    ascii_string = ascii_lowercase + ascii_uppercase + digits
    return "".join(sample(ascii_string, k=6))


def insert_if_not_exists(session: Session, url: str):
    """Send data to the table only if any of items don't exist in the table"""
    url_reference_code = create_url_reference_code()

    exists = (
        session.query(UrlModel)
        .filter(or_(UrlModel.reference_code == url_reference_code, UrlModel.original_url == url))
        .first()
    )

    if exists:
        ...
        return ...

    # new_register = UrlModel(...)
