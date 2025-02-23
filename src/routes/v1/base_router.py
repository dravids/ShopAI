"""Base router interface for ShopAI API routes.

This module provides the base interface for all route handlers,
ensuring consistent router configuration across the application.

Example:
    >>> from fastapi import APIRouter
    >>> from src.routes.v1.base_router import BaseRouter
    >>> class CustomRouter(BaseRouter):
    ...     def get_router(self) -> APIRouter:
    ...         router = APIRouter()
    ...         return router
"""
from abc import ABC, abstractmethod
from fastapi import APIRouter

class BaseRouter(ABC):
    """Abstract base class for route handlers.
    
    All route handlers must implement this interface to ensure
    consistent router configuration and dependency injection.
    """
    
    @abstractmethod
    def get_router(self) -> APIRouter:
        """Get the configured FastAPI router.
        
        Returns:
            APIRouter: Router with configured routes and dependencies
        """
        pass
