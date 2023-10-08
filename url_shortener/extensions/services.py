from random import choices
from string import ascii_letters
from string import digits

from sqlalchemy import select
from sqlalchemy.orm import Session
from url_shortener.extensions.schemas import UrlExists
from url_shortener.extensions.schemas import UrlSchema

from .database import UrlModel


def create_url_reference_code(session: Session) -> str:
    """Create a reference code with ascii characters"""
    reference_code = "".join(choices(ascii_letters + digits, k=6))
    ref_code_exists = session.scalar(select(UrlModel).where(UrlModel.reference_code == reference_code))
    if ref_code_exists:
        return create_url_reference_code(session)

    return reference_code


def insert_url_into_db(session: Session, url_info: UrlSchema):
    """Send data to the table only if any of items don't exist in the table"""
    url_exists = session.scalar(select(UrlModel).where(UrlModel.original_url == url_info.original_url.__str__()))
    if url_exists:
        return UrlExists(url_exists, message="Url register already exists!")

    url_reference_code = create_url_reference_code(session)
    new_register = UrlModel(original_url=url_info.original_url.__str__(), reference_code=url_reference_code)
    session.add(new_register)
    session.commit()
    session.refresh(new_register)
    return new_register
