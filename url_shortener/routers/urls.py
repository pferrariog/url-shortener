from typing import Annotated
from typing import Union

from fastapi import APIRouter
from fastapi import Depends
from fastapi import Path
from sqlalchemy.orm import Session
from url_shortener.extensions.database import get_db_connection
from url_shortener.extensions.schemas import UrlExists
from url_shortener.extensions.schemas import UrlInfo
from url_shortener.extensions.schemas import UrlSchema
from url_shortener.extensions.services import get_url_from_db
from url_shortener.extensions.services import insert_url_into_db


router = APIRouter(prefix="/api", tags=["Url"])


@router.get("/{reference_code}", status_code=200, response_model=UrlInfo)
def get_real_url(
    reference_code: Annotated[str, Path(title="URL code to exchange for the real one")],
    session: Session = Depends(get_db_connection),
) -> Union[UrlInfo, None]:
    """Retrieve the original url of a given code"""
    url_response = get_url_from_db(session, reference_code)
    return url_response


@router.post("/", status_code=201, response_model=Union[UrlInfo, UrlExists])
def make_url_shorter(url_info: UrlSchema, session: Session = Depends(get_db_connection)) -> Union[UrlInfo, UrlExists]:
    """Send the URL and retrieve the reference code"""
    url_response = insert_url_into_db(session, url_info)
    return url_response
