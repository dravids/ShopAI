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
from ..models.location import LocationSuggestion, LocationDetails


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
                    details=LocationDetails(
                        latitude=40.7128,
                        longitude=-74.0060,
                        formatted_address="Mock Location 1, Test City, Test Country",
                        types=["establishment", "point_of_interest"],
                        name="Mock Location 1",
                        vicinity="Test City",
                        url="https://maps.google.com/?q=mock1",
                        website="https://mock1.example.com",
                        formatted_phone_number="+1 555-0123",
                        international_phone_number="+1-555-0123",
                        rating=4.5,
                        user_ratings_total=100,
                        price_level=2,
                        opening_hours={
                            "open_now": True,
                            "weekday_text": ["Monday: 9:00 AM – 5:00 PM"]
                        },
                        wheelchair_accessible_entrance=True,
                        delivery=True,
                        dine_in=True,
                        editorial_summary="A mock location for testing"
                    )
                ),
                LocationSuggestion(
                    place_id="mock_place_2",
                    description="Mock Location 2, Test City",
                    main_text="Mock Location 2",
                    secondary_text="Test City",
                    details=LocationDetails(
                        latitude=51.5074,
                        longitude=-0.1278,
                        formatted_address="Mock Location 2, Test City, Test Country",
                        types=["establishment", "point_of_interest"],
                        name="Mock Location 2",
                        vicinity="Test City",
                        url="https://maps.google.com/?q=mock2",
                        website="https://mock2.example.com",
                        formatted_phone_number="+1 555-0124",
                        international_phone_number="+1-555-0124",
                        rating=4.8,
                        user_ratings_total=200,
                        price_level=3,
                        opening_hours={
                            "open_now": False,
                            "weekday_text": ["Monday: 10:00 AM – 6:00 PM"]
                        },
                        wheelchair_accessible_entrance=True,
                        delivery=False,
                        dine_in=True,
                        editorial_summary="Another mock location for testing"
                    )
                )
            ]

        try:
            results = self.client.places_autocomplete(
                input_text=query, types=["geocode", "establishment"], language="en"
            )

            suggestions = []
            for result in results:
                suggestion = LocationSuggestion(
                    place_id=result["place_id"],
                    description=result["description"],
                    main_text=result["structured_formatting"]["main_text"],
                    secondary_text=result["structured_formatting"].get("secondary_text"),
                )
                
                try:
                    place_details = self.client.place(
                        result["place_id"],
                        fields=[
                            "formatted_address", "geometry", "name", "type",
                            "vicinity", "url", "website", "formatted_phone_number",
                            "international_phone_number", "rating", "user_ratings_total",
                            "price_level", "opening_hours", "wheelchair_accessible_entrance",
                            "delivery", "dine_in", "editorial_summary"
                        ]
                    )["result"]
                    
                    suggestion.details = LocationDetails(
                        latitude=place_details["geometry"]["location"]["lat"],
                        longitude=place_details["geometry"]["location"]["lng"],
                        formatted_address=place_details["formatted_address"],
                        types=place_details.get("types", []),
                        name=place_details["name"],
                        vicinity=place_details.get("vicinity"),
                        url=place_details.get("url"),
                        website=place_details.get("website"),
                        formatted_phone_number=place_details.get("formatted_phone_number"),
                        international_phone_number=place_details.get("international_phone_number"),
                        rating=place_details.get("rating"),
                        user_ratings_total=place_details.get("user_ratings_total"),
                        price_level=place_details.get("price_level"),
                        opening_hours=place_details.get("opening_hours"),
                        wheelchair_accessible_entrance=place_details.get("wheelchair_accessible_entrance"),
                        delivery=place_details.get("delivery"),
                        dine_in=place_details.get("dine_in"),
                        editorial_summary=place_details.get("editorial_summary", {}).get("overview")
                    )
                except Exception as e:
                    print(f"Failed to fetch details for place {result['place_id']}: {str(e)}")
                
                suggestions.append(suggestion)
            
            return suggestions
        except Exception as e:
            raise AppException(
                code="google_maps_error",
                message=f"Failed to fetch location suggestions: {str(e)}",
            ) from e
