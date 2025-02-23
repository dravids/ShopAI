"""Service factory for ShopAI dependency injection.

This module provides factory functions for service instantiation,
ensuring proper dependency injection and environment-based configuration.

Example:
    >>> from fastapi import FastAPI, Depends
    >>> app = FastAPI()
    >>> @app.get("/locations")
    ... async def get_locations(
    ...     service: LocationService = Depends(get_location_service)
    ... ):
    ...     return await service.get_location_suggestions("query")
"""
from typing import Annotated
from fastapi import Depends
from .location_service import LocationService
from ..core.config import Settings, get_settings

def get_location_service(settings: Annotated[Settings, Depends(get_settings)]) -> LocationService:
    """Get configured LocationService instance.
    
    Args:
        settings: Application settings from dependency injection
        
    Returns:
        LocationService: Service instance configured based on environment
    """
    return LocationService(test_mode=settings.environment != "production")
