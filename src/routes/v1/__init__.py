from fastapi import APIRouter
from .health.health_router import HealthRouter
from .location.location_router import LocationRouter
from ...services.location_service import LocationService

def create_v1_router(location_service: LocationService) -> APIRouter:
    """Create and configure v1 API router"""
    router = APIRouter(prefix="/api/v1")
    
    # Add route handlers
    health_router = HealthRouter()
    location_router = LocationRouter(location_service)
    
    router.include_router(health_router.get_router())
    router.include_router(location_router.get_router())
    
    return router
