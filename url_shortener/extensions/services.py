from random import choices
from string import ascii_letters
from string import digits

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from url_shortener.extensions.schemas import UrlExists
from url_shortener.extensions.schemas import UrlSchema

from .database import UrlModel


def set_url_reference_code(session: Session, url_info: UrlSchema) -> str:
    """Create a reference code with ascii characters"""
    reference_code = get_reference_code_alias(url_info)
    ref_code_exists = session.scalar(select(UrlModel).where(UrlModel.reference_code == reference_code))
    if ref_code_exists and url_info.reference_code:
        raise HTTPException(400, detail="Url alias already exists, try another!")
    if ref_code_exists:
        return set_url_reference_code(session)

    return reference_code


def get_reference_code_alias(url_info: UrlSchema) -> str:
    """Return reference code value based on user input data"""
    if not url_info.reference_code:
        return "".join(choices(ascii_letters + digits, k=6))
    return url_info.reference_code


def insert_url_into_db(session: Session, url_info: UrlSchema) -> UrlModel:
    """Send data to the table only if any of items don't exist in the table"""
    url_exists = session.scalar(select(UrlModel).where(UrlModel.original_url == url_info.original_url.__str__()))
    if url_exists:
        return UrlExists(
            original_url=url_exists.original_url,
            reference_code=url_exists.reference_code,
            creation_date=url_exists.creation_date,
            message="Url register already exists!",
        )
    url_reference_code = set_url_reference_code(session, url_info)
    new_register = UrlModel(original_url=url_info.original_url.__str__(), reference_code=url_reference_code)
    session.add(new_register)
    session.commit()
    session.refresh(new_register)
    return new_register


def get_url_from_db(session: Session, reference_code: str) -> UrlModel:
    """Get the original url from database"""
    url_response = session.scalar(select(UrlModel).where(UrlModel.reference_code == reference_code))
    if not url_response:
        raise HTTPException(status_code=404, detail=f"URL {reference_code} not found")
    return url_response
