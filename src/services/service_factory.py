from typing import Annotated
from fastapi import Depends
from .location_service import LocationService
from ..core.config import Settings, get_settings

def get_location_service(settings: Annotated[Settings, Depends(get_settings)]) -> LocationService:
    return LocationService(test_mode=settings.environment != "production")
