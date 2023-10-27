from typing import Annotated
from typing import Union

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Path
from fastapi.responses import FileResponse
from fastapi.responses import RedirectResponse
from sqlalchemy import select
from sqlalchemy.orm import Session
from url_shortener.extensions.database import UrlModel
from url_shortener.extensions.database import get_db_connection


router = APIRouter(include_in_schema=False)


@router.get("/", response_model=None)
def render_homepage():
    """Render the app's homepage"""
    return FileResponse("static/index.html")


@router.get("/{reference_code}", status_code=307, response_model=None)
def get_real_url(
    reference_code: Annotated[str, Path(title="URL code to exchange for the real one")],
    session: Session = Depends(get_db_connection),
) -> Union[RedirectResponse, None]:
    """Redirect the user to original url of a given code"""
    url_response = session.scalar(select(UrlModel).where(UrlModel.reference_code == reference_code))
    if not url_response:
        raise HTTPException(status_code=404, detail=f"URL {reference_code} not found")
    return RedirectResponse(url_response.original_url)
