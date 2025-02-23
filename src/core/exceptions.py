"""Exception handling for ShopAI.

This module provides custom exception classes for consistent error handling
across the application.

Example:
    >>> from src.core.exceptions import AppException
    >>> raise AppException(
    ...     code="validation_error",
    ...     message="Invalid input",
    ...     details={"field": "query"}
    ... )
"""
from typing import Dict, Any, Optional
from fastapi import HTTPException

class AppException(Exception):
    """Base exception for application-specific errors.
    
    Attributes:
        code: Error code for client handling
        message: Human-readable error message
        details: Additional error context
    
    Example:
        >>> error = AppException("not_found", "Resource not found")
        >>> print(error.code)
        'not_found'
    """
    def __init__(self, code: str, message: str, details: Optional[Dict[str, Any]] = None):
        self.code = code
        self.message = message
        self.details = details or {}
