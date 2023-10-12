from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from url_shortener.routers.urls import router as url_router

from .settings import settings


def create_app(title: str, docs_url: str, description: str, routers: list) -> FastAPI:
    """App factory"""
    app = FastAPI(
        title=title,
        docs_url=docs_url,
        description=description,
    )

    for route in routers:
        app.include_router(route)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ORIGINS,
        allow_methods=["*"]
    )

    return app


app = create_app(settings.APP_NAME, settings.DOCS_PATH, settings.APP_DESCRIPTION, [url_router])
