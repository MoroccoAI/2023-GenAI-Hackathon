from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    auth0_id: str
    full_name: str
    company: Optional[str] = None
    role: Optional[str] = None

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass

class User(UserBase):
    id: int

    class Config:
        orm_mode = True
