from fastapi import APIRouter
from fastapi.responses import FileResponse


router = APIRouter()


@router.get("/", response_model=None)
def render_homepage():
    """Render the app's homepage"""
    return FileResponse("static/index.html")
