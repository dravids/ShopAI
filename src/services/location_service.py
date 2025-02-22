import os
import googlemaps
from typing import List
from dotenv import load_dotenv
from fastapi import HTTPException

from ..models.location import LocationSuggestion

load_dotenv()

class LocationService:
    def __init__(self, test_mode: bool = True):
        self.test_mode = test_mode
        self.client = None
        if not test_mode:
            api_key = os.getenv("GOOGLE_MAPS_API_KEY")
            if api_key:
                self.client = googlemaps.Client(key=api_key)

    async def get_location_suggestions(self, query: str) -> List[LocationSuggestion]:
        # Mock response for testing without API key
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
