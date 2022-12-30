from typing import Optional, List

from datetime import datetime

from pydantic import BaseModel, EmailStr


# Shared properties
class TitleBase(BaseModel):

    show_id: Optional[str] = None
    category: Optional[str] = None
    title: Optional[str] = None
    director: Optional[str] = None
    cast_members: Optional[str] = None
    country: Optional[str] = None
    date_added: Optional[datetime] = None
    release_year: Optional[str] = None
    rating: Optional[str] = None
    duration: Optional[str] = None
    listed_in: Optional[str] = None
    description: Optional[str] = None


# Properties to receive via API on creation
class TitleCreate(TitleBase):
    pass


# Properties to receive via API on update
class TitleUpdate(TitleBase):
    pass


class TitleInDBBase(TitleBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class Title(TitleInDBBase):
    pass


class Titles:
    total_count: int
    Titles: List[Title] = []
