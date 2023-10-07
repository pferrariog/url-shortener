from typing import Annotated

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Path
from fastapi.responses import RedirectResponse
from sqlalchemy import select
from sqlalchemy.orm import Session
from url_shortener.extensions.database import UrlModel
from url_shortener.extensions.database import get_db_connection
from url_shortener.extensions.schemas import UrlInfo
from url_shortener.extensions.schemas import UrlSchema
from url_shortener.extensions.services import insert_url_into_db


router = APIRouter(prefix="/api")


@router.get("/{reference_code}", status_code=200)
def get_real_url(
    reference_code: Annotated[str, Path(title="URL code to exchange for the real one")],
    session: Session = Depends(get_db_connection),
) -> RedirectResponse:
    """Retrieve the original url of a given code"""
    url_response = session.scalar(select(UrlModel).where(UrlModel.reference_code == reference_code))
    if not url_response:
        raise HTTPException(status_code=404, detail=f"URL {reference_code} not found")

    return RedirectResponse(url_response.original_url)


@router.post("/", status_code=200, response_model=UrlInfo)
def make_url_shorter(url_info: UrlSchema, session: Session = Depends(get_db_connection)) -> UrlInfo:
    """Send the URL and retrieve the reference code"""
    url_response = insert_url_into_db(session, url_info)
    return url_response
