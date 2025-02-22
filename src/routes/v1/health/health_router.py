from fastapi import APIRouter
from ..base_router import BaseRouter

class HealthRouter(BaseRouter):
    def __init__(self):
        self._router = APIRouter(tags=["Health"])
        self._configure_routes()

    def get_router(self) -> APIRouter:
        return self._router

    def _configure_routes(self):
        @self._router.get("/ping")
        async def ping():
            """Health check endpoint"""
            return {"response": "pong"}
