from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html, get_redoc_html

description = """
# ShopAI API
This is a modern e-commerce API built with FastAPI.

## Features
* Product management
* User authentication
* Order processing
"""

app = FastAPI(
    title="ShopAI",
    description=description,
    version="1.0.0",
    docs_url=None,  # Disable default docs
    redoc_url=None,  # Disable default redoc
)


@app.get("/ping", tags=["Root"])
async def read_root():
    """
     Root endpoint that returns welcome message.
    Returns:
     dict: A simple welcome message
    """
    return {"response": "pong-test-hot-reload"}


@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    """
    Custom Swagger UI documentation.
    """
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
    )


@app.get("/redoc", include_in_schema=False)
async def redoc_html():
    """
    ReDoc documentation.
    """
    return get_redoc_html(
        openapi_url=app.openapi_url,
        title=app.title + " - ReDoc",
    )
