"""Health check endpoints for ShopAI API.

This module provides health check endpoints to verify API availability
and system status.

Example:
    >>> from fastapi import FastAPI
    >>> from src.routes.v1.health.health_router import HealthRouter
    >>> app = FastAPI()
    >>> health_router = HealthRouter()
    >>> app.include_router(health_router.get_router())
"""
from fastapi import APIRouter
from ..base_router import BaseRouter

class HealthRouter(BaseRouter):
    """Router for health check endpoints.
    
    Provides simple endpoints to verify API availability and system status.
    """
    
    def __init__(self):
        """Initialize health router with ping endpoint."""
        self._router = APIRouter(tags=["Health"])
        self._configure_routes()

    def get_router(self) -> APIRouter:
        """Get the configured health check router.
        
        Returns:
            APIRouter: Router with health check endpoints
        """
        return self._router

    def _configure_routes(self):
        """Configure health check endpoints."""
        @self._router.get("/ping")
        async def ping():
            """Simple health check endpoint.
            
            Returns:
                dict: Response with "pong" message
            """
            return {"response": "pong"}
