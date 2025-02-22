from fastapi import APIRouter
from ..base_router import BaseRouter
from ....models.location import LocationAutocompleteRequest, LocationAutocompleteResponse
from ....services.location_service import LocationService

class LocationRouter(BaseRouter):
    def __init__(self, location_service: LocationService):
        self._router = APIRouter(prefix="/locations", tags=["Location"])
        self._location_service = location_service
        self._configure_routes()

    def get_router(self) -> APIRouter:
        return self._router

    def _configure_routes(self):
        @self._router.post("/autocomplete", response_model=LocationAutocompleteResponse)
        async def autocomplete_location(
            request: LocationAutocompleteRequest
        ) -> LocationAutocompleteResponse:
            """Get location suggestions based on user input"""
            suggestions = await self._location_service.get_location_suggestions(request.query)
            return LocationAutocompleteResponse(suggestions=suggestions)
