"""Configuration management for ShopAI.

This module provides centralized configuration management using pydantic-settings.
Environment variables are loaded from .env file with proper validation.

Example:
    >>> from src.core.config import get_settings
    >>> settings = get_settings()
    >>> print(settings.environment)
    'development'
"""
from pydantic_settings import BaseSettings
from functools import lru_cache
from typing import Literal

class Settings(BaseSettings):
    """Application settings loaded from environment variables.
    
    Attributes:
        google_maps_api_key: API key for Google Maps Places API
        environment: Current environment (development/production)
    """
    google_maps_api_key: str
    environment: Literal["development", "production"] = "development"
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False

@lru_cache()
def get_settings() -> Settings:
    """Get cached application settings.
    
    Returns:
        Settings: Application configuration instance
    """
    return Settings()
