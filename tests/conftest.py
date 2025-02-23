import pytest
from fastapi.testclient import TestClient
from src.main import app

@pytest.fixture
def client():
    # Ensure test mode is enabled for location service
    from src.services.service_factory import get_location_service
    from src.services.location_service import LocationService
    
    # Override location service to use test mode
    def get_test_location_service() -> LocationService:
        return LocationService(test_mode=True)
    
    app.dependency_overrides[get_location_service] = get_test_location_service
    yield TestClient(app)
    app.dependency_overrides.clear()
