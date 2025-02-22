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
