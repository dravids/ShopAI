import googlemaps
from typing import List
from ..core.config import Settings
from ..core.exceptions import AppException
from ..models.location import LocationSuggestion

class LocationService:
    def __init__(self, test_mode: bool = True):
        self.test_mode = test_mode
        self.client = None
        if not test_mode:
            try:
                self.client = googlemaps.Client(key=Settings().google_maps_api_key)
            except Exception as e:
                raise AppException(
                    code="config_error",
                    message=f"Failed to initialize Google Maps client: {str(e)}"
                )

    async def get_location_suggestions(self, query: str) -> List[LocationSuggestion]:
        if self.test_mode:
            return [
                LocationSuggestion(
                    place_id="mock_place_1",
                    description="Mock Location 1, Test City",
                    main_text="Mock Location 1",
                    secondary_text="Test City"
                ),
                LocationSuggestion(
                    place_id="mock_place_2",
                    description="Mock Location 2, Test City",
                    main_text="Mock Location 2",
                    secondary_text="Test City"
                )
            ]
        
        try:
            results = self.client.places_autocomplete(
                input_text=query,
                types=["geocode", "establishment"],
                language="en"
            )
            
            return [
                LocationSuggestion(
                    place_id=result["place_id"],
                    description=result["description"],
                    main_text=result["structured_formatting"]["main_text"],
                    secondary_text=result["structured_formatting"].get("secondary_text")
                )
                for result in results
            ]
        except Exception as e:
            raise AppException(
                code="google_maps_error",
                message=f"Failed to fetch location suggestions: {str(e)}"
            )
