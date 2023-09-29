from fastapi import FastAPI

from url_shortener.routers.urls import router as url_router


def create_app(
        title: str, 
        docs_url: str, 
        description: str, 
        version: str,
        routers: list
    ) -> FastAPI:
    """App factory"""
    app = FastAPI(
        title=title, 
        docs_url=docs_url,
        description=description,
        version=version
        )

    for route in routers:
        app.include_router(route)

    return app


app = create_app("URL Shortener", "/api/docs", "URL Shortener App", "0.1.0", [url_router])
