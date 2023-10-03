from typing import Annotated

from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import Path
from fastapi.responses import RedirectResponse
from url_shortener.extensions.schemas import UrlInfo
from url_shortener.extensions.schemas import UrlSchema
from validators import url as url_valid


router = APIRouter(prefix="/api")


@router.get("/{encoded_url}", status_code=200)
async def get_real_url(
    encoded_url: Annotated[str, Path(title="URL code to exchange for the real one")]
) -> RedirectResponse:
    """Retrieve the original url of a given code"""
    real_url = ...

    if not url_valid(encoded_url):
        raise ...

    if encoded_url not in ...:
        raise HTTPException(status_code=404, detail=f"URL {encoded_url} not found")

    return RedirectResponse(real_url)


@router.post("/", status_code=200, response_model=UrlInfo)
async def make_url_shorter(url_info: UrlSchema) -> UrlInfo:
    """Send the URL and retrieve the reference code"""
    ...
    return ...
