from typing import Optional

from datetime import datetime

from pydantic import BaseModel, EmailStr


# Shared properties
class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    full_name: Optional[str] = None


# Properties to receive via API on creation
class UserCreate(UserBase):
    email: EmailStr
    password: str


# Properties to receive via API on update
class UserUpdate(UserBase):
    password: Optional[str] = None


class UserInDBBase(UserBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class User(UserInDBBase):
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None


# Additional properties stored in DB
class UserInDB(UserInDBBase):
    date_created: datetime
    date_modified: datetime
    hashed_password: str


# Additional properties to return via API
class UserLogin(BaseModel):
    username: EmailStr
    password: str


# Properties to receive via API on creation
class UserWithToken(User):
    access_token: Optional[str] = None
    token_type: Optional[str] = None

# Property to activate user
class UserActivation(BaseModel):
    is_active: bool = False
