from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class User(BaseModel):
    """User model for storing customer information.
    
    This model represents a user in the ShopAI system with their
    personal and authentication details.
    
    Attributes:
        id (int): Unique identifier
        email (EmailStr): User's email address
        full_name (str): User's full name
        is_active (bool): Whether user account is active
        created_at (datetime): Account creation timestamp
        
    Example:
        >>> user = User(
        ...     id=1,
        ...     email="user@example.com",
        ...     full_name="John Doe"
        ... )
    """
    
    id: Optional[int] = None
    email: EmailStr
    full_name: str
    is_active: bool = True
    created_at: datetime = datetime.now()