from typing import Annotated

from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import Path
from fastapi.responses import JSONResponse, RedirectResponse
from validators import url as url_valid

from url_shortener.extensions.schemas import UrlInfo


router = APIRouter(prefix="/api")

@router.get("/{url}", status_code=200)
async def get_real_url(url: Annotated[str, Path(min_length=15)]) -> RedirectResponse:
    """"""
    real_url = ...

    if not url_valid(url):
        raise ...
    
    if url not in ...:
        raise HTTPException(status_code=404, detail=f"URL {url} not found")
    
    return  RedirectResponse(real_url)

@router.post("/", status_code=200, response_model=UrlInfo)
async def make_url_shorter() -> JSONResponse:
    """"""
    ...
    return JSONResponse(content={
        "url": ...
    })
