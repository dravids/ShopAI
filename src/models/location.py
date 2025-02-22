from pydantic import BaseModel, Field
from typing import List

class LocationSuggestion(BaseModel):
    place_id: str
    description: str
    main_text: str = Field(..., description="Primary text for the location")
    secondary_text: str | None = Field(None, description="Additional location details")

class LocationAutocompleteRequest(BaseModel):
    query: str = Field(..., min_length=2, max_length=100, description="Location search query")

class LocationAutocompleteResponse(BaseModel):
    suggestions: List[LocationSuggestion]
