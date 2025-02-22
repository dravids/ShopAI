import os
import googlemaps
from typing import List
from dotenv import load_dotenv
from fastapi import HTTPException

from ..models.location import LocationSuggestion

load_dotenv()

class LocationService:
    def __init__(self):
        api_key = os.getenv("GOOGLE_MAPS_API_KEY")
        if not api_key:
            raise ValueError("Google Maps API key not found in environment variables")
        self.client = googlemaps.Client(key=api_key)

    async def get_location_suggestions(self, query: str) -> List[LocationSuggestion]:
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
            raise HTTPException(status_code=500, detail=str(e))
