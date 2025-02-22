from abc import ABC, abstractmethod
from fastapi import APIRouter

class BaseRouter(ABC):
    @abstractmethod
    def get_router(self) -> APIRouter:
        """Return the FastAPI router with configured routes"""
        pass
