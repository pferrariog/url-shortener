from random import sample
from string import ascii_lowercase
from string import ascii_uppercase
from string import digits

from fastapi import HTTPException
from sqlalchemy import or_
from sqlalchemy.orm import Session
from url_shortener.extensions.schemas import UrlSchema

from .database import UrlModel


def create_url_reference_code() -> str:
    """Create a reference code with ascii characters"""
    ascii_string = ascii_lowercase + ascii_uppercase + digits
    return "".join(sample(ascii_string, k=6))


def insert_url_into_db(session: Session, url_info: UrlSchema):
    """Send data to the table only if any of items don't exist in the table"""
    url_reference_code = create_url_reference_code()
    # TODO split this check in 2 others
    # one - check and return detail and the UrlInfo content instead of an exception if url already exists
    # two - check and apply a recursive function to create a new ref code if already exists
    exists = (
        session.query(UrlModel)
        .filter(or_(UrlModel.reference_code == url_reference_code, UrlModel.original_url == url_info.url))
        .first()
    )
    if exists:
        raise HTTPException(status_code=400, detail="Url already exists")
    new_register = UrlModel(original_url=url_info.original_url.__str__(), reference_code=url_reference_code)
    session.add(new_register)
    session.commit()
    session.refresh(new_register)
    return new_register
