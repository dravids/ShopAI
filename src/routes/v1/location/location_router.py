from fastapi import APIRouter, Depends
from typing import Annotated, Callable
from ..base_router import BaseRouter
from ....models.location import LocationAutocompleteRequest, LocationAutocompleteResponse
from ....services.location_service import LocationService

class LocationRouter(BaseRouter):
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
            service: Annotated[LocationService, Depends(self._get_location_service)]
        ) -> LocationAutocompleteResponse:
            """Get location suggestions based on user input"""
            suggestions = await service.get_location_suggestions(request.query)
            return LocationAutocompleteResponse(suggestions=suggestions)
