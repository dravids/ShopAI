from pydantic import BaseModel, Field
from typing import List, Dict

class LocationDetails(BaseModel):
    latitude: float = Field(..., description="Location latitude")
    longitude: float = Field(..., description="Location longitude")
    formatted_address: str = Field(..., description="Full formatted address")
    types: List[str] = Field(default_factory=list, description="Place types")
    name: str = Field(..., description="Place name")
    vicinity: str | None = Field(None, description="Vicinity description")
    url: str | None = Field(None, description="Google Maps URL")
    website: str | None = Field(None, description="Place website")
    formatted_phone_number: str | None = Field(None, description="Phone number")
    international_phone_number: str | None = Field(None, description="International format")
    rating: float | None = Field(None, description="Place rating")
    user_ratings_total: int | None = Field(None, description="Total ratings")
    price_level: int | None = Field(None, ge=0, le=4, description="Price level")
    opening_hours: Dict | None = Field(None, description="Operating hours")
    wheelchair_accessible_entrance: bool | None = Field(None)
    delivery: bool | None = Field(None)
    dine_in: bool | None = Field(None)
    editorial_summary: str | None = Field(None)

class LocationSuggestion(BaseModel):
    place_id: str = Field(..., description="Unique Google Maps place identifier")
    description: str = Field(..., description="Full place description")
    main_text: str = Field(..., description="Primary text for the location")
    secondary_text: str | None = Field(None, description="Additional location details")
    details: LocationDetails | None = Field(None, description="Detailed place information")

class LocationAutocompleteRequest(BaseModel):
    query: str = Field(..., min_length=2, max_length=100, description="Location search query")

class LocationAutocompleteResponse(BaseModel):
    suggestions: List[LocationSuggestion]
