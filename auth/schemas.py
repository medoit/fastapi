from fastapi_users import schemas
from typing import Optional
from datetime import datetime

from pydantic import EmailStr


class UserRead(schemas.BaseUser[int]):
    id: int
    username: str
    registered_at: datetime
    role_id: int
    email: EmailStr
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False
    
    class Config:
        orm_mode = True


class UserCreate(schemas.BaseUserCreate):
    username: str
    role_id: int
    email: EmailStr
    password: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False


class UserUpdate(schemas.BaseUserUpdate):
    username: str
    role_id: int
    password: Optional[str]
    email: Optional[EmailStr]
    is_active: Optional[bool]
    is_superuser: Optional[bool]
    is_verified: Optional[bool]