"""
This module provides the LocationService class for fetching location suggestions
using the Google Places API. It supports both test mode with mock data and real
mode with actual API calls.

Classes:
    LocationService: A service class for fetching location suggestions based on
    a query string.

Exceptions:
    AppException: Custom exception class for handling application-specific errors.

"""

from typing import List
import googlemaps
from ..core.config import Settings
from ..core.exceptions import AppException
from ..models.location import LocationSuggestion


class LocationService:
    """
    LocationService is a service class responsible for fetching location suggestions
    based on a query string. It can operate in test mode, returning mock data, or in
    production mode, using the Google Places API to fetch real location suggestions.
    Attributes:
        test_mode (bool): A flag indicating whether the service is in test mode.
        client (googlemaps.Client): The Google Maps client used to fetch location suggestions.
    Methods:
        __init__(test_mode: bool = True):
            Initializes the LocationService instance. If not in test mode, it attempts
            to initialize the Google Maps client with the provided API key.
        async get_location_suggestions(query: str) -> List[LocationSuggestion]:
            Fetches location suggestions based on the provided query string. If the service
            is in test mode, returns a list of mock location suggestions. Otherwise, it uses
            the Google Places API to fetch real location suggestions.
                AppException: If there is an error while fetching location suggestions from
                the Google Places API.
    """

    def __init__(self, test_mode: bool = True):
        self.test_mode = test_mode
        self.client = None
        if not test_mode:
            try:
                self.client = googlemaps.Client(key=Settings().google_maps_api_key)
            except Exception as e:
                raise AppException(
                    code="config_error",
                    message=f"Failed to initialize Google Maps client: {str(e)}",
                ) from e

    async def get_location_suggestions(self, query: str) -> List[LocationSuggestion]:
        """
        Fetches location suggestions based on the provided query string.
        If the service is in test mode, returns a list of mock location suggestions.
        Otherwise, it uses the Google Places API to fetch real location suggestions.
        Args:
            query (str): The search query string for location suggestions.
        Returns:
            List[LocationSuggestion]: A list of location suggestions.
        Raises:
            AppException: If there is an error while fetching location suggestions from the Google Places API.
        """

        if self.test_mode:
            return [
                LocationSuggestion(
                    place_id="mock_place_1",
                    description="Mock Location 1, Test City",
                    main_text="Mock Location 1",
                    secondary_text="Test City",
                ),
                LocationSuggestion(
                    place_id="mock_place_2",
                    description="Mock Location 2, Test City",
                    main_text="Mock Location 2",
                    secondary_text="Test City",
                ),
            ]

        try:
            results = self.client.places_autocomplete(
                input_text=query, types=["geocode", "establishment"], language="en"
            )

            return [
                LocationSuggestion(
                    place_id=result["place_id"],
                    description=result["description"],
                    main_text=result["structured_formatting"]["main_text"],
                    secondary_text=result["structured_formatting"].get(
                        "secondary_text"
                    ),
                )
                for result in results
            ]
        except Exception as e:
            raise AppException(
                code="google_maps_error",
                message=f"Failed to fetch location suggestions: {str(e)}",
            ) from e
