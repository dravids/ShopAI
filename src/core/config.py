from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    google_maps_api_key: str
    environment: str = "development"
    
    class Config:
        env_file = ".env"

@lru_cache()
def get_settings() -> Settings:
    return Settings()
