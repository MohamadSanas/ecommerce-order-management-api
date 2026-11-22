"""Pydantic schemas for User validation and serialization."""

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict, EmailStr, Field

from app.models.user import UserRole


# Shared properties across user schemas
class UserBase(BaseModel):
    email: EmailStr
    full_name: str = Field(...,max_length=255 )

# Properties required when creating a new user (Registration)
class UserCreate(UserBase):
    password: str = Field(..., min_length=8, description="Password must be at least 8 characters")


# Properties allowed when updating a user profile
class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    full_name: Optional[str] = Field(None, max_length=255)
    password: Optional[str] = Field(None, min_length=8)


# Properties returned to the client (Safe - NO PASSWORDS!)
class UserOut(UserBase):
    id: int
    role: UserRole
    is_active: bool
    created_at: datetime
    updated_at: datetime

    # Pydantic v2: allows Pydantic to read directly from SQLAlchemy models
    model_config = ConfigDict(from_attributes=True)