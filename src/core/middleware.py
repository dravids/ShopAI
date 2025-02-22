"""
middleware.py

This module contains middleware for handling exceptions in a FastAPI application.
It includes a middleware function that intercepts requests and handles 
application-specific
and general exceptions, returning appropriate JSON responses.

Functions:
    error_handler_middleware(request: Request, call_next): Middleware to handle 
    exceptions and return appropriate JSON responses.
    
"""

from fastapi import Request
from fastapi.responses import JSONResponse
from .exceptions import AppException


async def error_handler_middleware(request: Request, call_next):
    """
    Middleware to handle exceptions and return appropriate JSON responses.
    Args:
        request (Request): The incoming HTTP request.
        call_next (Callable): The next middleware or request handler.
    Returns:
        JSONResponse: A JSON response with the appropriate status code and error
        details.
    Raises:
        AppException: If an application-specific exception occurs, returns a 400 s
        tatus code with error details.
        Exception: If a general exception occurs, returns a 500 status code
        with the error message.
    """

    try:
        return await call_next(request)
    except AppException as e:
        return JSONResponse(
            status_code=400,
            content={"code": e.code, "message": e.message, "details": e.details},
        )
    except Exception as e:
        return JSONResponse(
            status_code=500, content={"code": "internal_error", "message": str(e)}
        )
