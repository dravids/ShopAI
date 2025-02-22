from typing import Dict, Any, Optional
from fastapi import HTTPException

class AppException(Exception):
    def __init__(self, code: str, message: str, details: Optional[Dict[str, Any]] = None):
        self.code = code
        self.message = message
        self.details = details or {}
