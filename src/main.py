from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html, get_redoc_html

from .core.config import get_settings
from .services.service_factory import get_location_service
from .routes.v1 import create_v1_router

description = """
# ShopAI API
One single app for all your shopping needs
"""

app = FastAPI(
    title="ShopAI",
    description=description,
    version="1.0.0",
    docs_url=None,  # Disable default docs
    redoc_url=None,  # Disable default redoc
)

# Add middleware
from .core.middleware import error_handler_middleware
app.middleware("http")(error_handler_middleware)

# Initialize settings with environment
settings = get_settings()

# Configure routes with production mode
v1_router = create_v1_router(get_location_service)
app.include_router(v1_router)

@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    """Custom Swagger UI documentation"""
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
    )

@app.get("/redoc", include_in_schema=False)
async def redoc_html():
    """ReDoc documentation"""
    return get_redoc_html(
        openapi_url=app.openapi_url,
        title=app.title + " - ReDoc",
    )
