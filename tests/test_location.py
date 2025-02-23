from fastapi.testclient import TestClient

def test_location_autocomplete(client: TestClient):
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
    assert "formatted_address" in details
    assert "types" in details and isinstance(details["types"], list)
    assert "name" in details
    assert "vicinity" in details
    assert "url" in details
    assert "website" in details
    assert "formatted_phone_number" in details
    assert "international_phone_number" in details
    assert "rating" in details and isinstance(details["rating"], float)
    assert "user_ratings_total" in details and isinstance(details["user_ratings_total"], int)
    assert "price_level" in details and isinstance(details["price_level"], int)
    assert "opening_hours" in details and isinstance(details["opening_hours"], dict)
    assert "wheelchair_accessible_entrance" in details and isinstance(details["wheelchair_accessible_entrance"], bool)
    assert "delivery" in details and isinstance(details["delivery"], bool)
    assert "dine_in" in details and isinstance(details["dine_in"], bool)
    assert "editorial_summary" in details
