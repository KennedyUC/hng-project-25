from api.router import api_router
from fastapi import FastAPI
from fastapi.responses import UJSONResponse
from db.db import engine
from sqlmodel import SQLModel
def get_app() -> FastAPI:
    """
    Get FastAPI application.

    This is the main constructor of an application.

    :return: application.
    """
    app = FastAPI(
        title="VIP Service API",
        description="Backend to VIP Service Project by Team Axe",
        version="1.0",
        docs_url="/api/docs/",
        redoc_url="/api/redoc/",
        openapi_url="/api/openapi.json",
        default_response_class=UJSONResponse,
    )

    app.include_router(router=api_router, prefix="/api")
    @app.on_event("startup")
    def on_startup():
        SQLModel.metadata.create_all(engine)
    return app
