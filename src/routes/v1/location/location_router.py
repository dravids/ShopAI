"""
This module defines the LocationRouter class, which is responsible for handling
location-related API routes in the ShopAI application.

Classes:
    LocationRouter: A router class that configures and handles location-related
                    API endpoints.

Dependencies:
    - fastapi.APIRouter
    - fastapi.Depends
    - typing.Annotated
    - typing.Callable
    - ..base_router.BaseRouter
    - ....models.location.LocationAutocompleteRequest
    - ....models.location.LocationAutocompleteResponse
    - ....services.location_service.LocationService
"""

from typing import Annotated, Callable
from fastapi import APIRouter, Depends
from ..base_router import BaseRouter
from ....models.location import (
    LocationAutocompleteRequest,
    LocationAutocompleteResponse,
)
from ....services.location_service import LocationService


class LocationRouter(BaseRouter):
    """
    LocationRouter is responsible for handling location-related API routes.
    Methods:
        __init__(get_location_service: Callable[[], LocationService]):
            Initializes the LocationRouter with a location service provider.
        get_router() -> APIRouter:
            Returns the configured APIRouter instance.
        _configure_routes():
            Configures the API routes for the location-related endpoints.
    Routes:
        POST /locations/autocomplete:
            Endpoint to get location suggestions based on user input.
            - Request: LocationAutocompleteRequest
            - Response: LocationAutocompleteResponse
    """

    def __init__(self, get_location_service: Callable[[], LocationService]):
        self._router = APIRouter(prefix="/locations", tags=["Location"])
        self._get_location_service = get_location_service
        self._configure_routes()

    def get_router(self) -> APIRouter:
        return self._router

    def _configure_routes(self):
        @self._router.post("/autocomplete", response_model=LocationAutocompleteResponse)
        async def autocomplete_location(
            request: LocationAutocompleteRequest,
            service: Annotated[LocationService, Depends(self._get_location_service)],
        ) -> LocationAutocompleteResponse:
            """Get location suggestions based on user input"""
            suggestions = await service.get_location_suggestions(request.query)
            return LocationAutocompleteResponse(suggestions=suggestions)
