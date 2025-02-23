from fastapi.testclient import TestClient

def test_mock_location_autocomplete(client: TestClient):
    """Test location autocomplete with mock data"""
    response = client.post(
        "/api/v1/locations/autocomplete",
        json={"query": "Times Square"}
    )
    assert response.status_code == 200
    data = response.json()
    assert "suggestions" in data
    assert len(data["suggestions"]) > 0
    
    suggestion = data["suggestions"][0]
    assert "place_id" in suggestion
    assert "description" in suggestion
    assert "main_text" in suggestion
    assert "secondary_text" in suggestion
    
    # Verify place details
    details = suggestion["details"]
    assert details["latitude"] == 40.7128
    assert details["longitude"] == -74.0060
    assert details["formatted_address"] == "Mock Location 1, Test City, Test Country"
    assert details["types"] == ["establishment", "point_of_interest"]
    assert details["name"] == "Mock Location 1"
    assert details["vicinity"] == "Test City"
    assert details["url"] == "https://maps.google.com/?q=mock1"
    assert details["website"] == "https://mock1.example.com"
    assert details["formatted_phone_number"] == "+1 555-0123"
    assert details["international_phone_number"] == "+1-555-0123"
    assert details["rating"] == 4.5
    assert details["user_ratings_total"] == 100
    assert details["price_level"] == 2
    assert details["opening_hours"] == {
        "open_now": True,
        "weekday_text": ["Monday: 9:00 AM – 5:00 PM"]
    }
    assert details["wheelchair_accessible_entrance"] is True
    assert details["delivery"] is True
    assert details["dine_in"] is True
    assert details["editorial_summary"] == "A mock location for testing"

def test_real_location_autocomplete(client: TestClient):
    """Test location autocomplete with real Google Maps API"""
    # Override test mode to use real API
    from src.services.service_factory import get_location_service
    from src.services.location_service import LocationService
    
    def get_real_location_service() -> LocationService:
        return LocationService(test_mode=False)
    
    client.app.dependency_overrides[get_location_service] = get_real_location_service
    
    try:
        response = client.post(
            "/api/v1/locations/autocomplete",
            json={"query": "Times Square"}
        )
        assert response.status_code == 200
        data = response.json()
        assert "suggestions" in data
        assert len(data["suggestions"]) > 0
        
        suggestion = data["suggestions"][0]
        assert "place_id" in suggestion
        assert "description" in suggestion
        assert "main_text" in suggestion
        assert "secondary_text" in suggestion
        
        # Verify place details structure (values will vary)
        details = suggestion["details"]
        assert isinstance(details["latitude"], float)
        assert isinstance(details["longitude"], float)
        assert isinstance(details["formatted_address"], str)
        assert isinstance(details["types"], list)
        assert isinstance(details["name"], str)
        assert isinstance(details["vicinity"], (str, type(None)))
        assert isinstance(details["url"], (str, type(None)))
        assert isinstance(details["website"], (str, type(None)))
        assert isinstance(details["formatted_phone_number"], (str, type(None)))
        assert isinstance(details["international_phone_number"], (str, type(None)))
        assert isinstance(details["rating"], (float, type(None)))
        assert isinstance(details["user_ratings_total"], (int, type(None)))
        assert isinstance(details["price_level"], (int, type(None)))
        assert isinstance(details["opening_hours"], (dict, type(None)))
        assert isinstance(details["wheelchair_accessible_entrance"], (bool, type(None)))
        assert isinstance(details["delivery"], (bool, type(None)))
        assert isinstance(details["dine_in"], (bool, type(None)))
        assert isinstance(details["editorial_summary"], (str, type(None)))
    finally:
        # Clean up dependency override
        client.app.dependency_overrides.clear()
