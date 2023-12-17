# schemas/platform.py
from pydantic import BaseModel, constr

class PlatformBase(BaseModel):
    name: constr(min_length=1, max_length=255)
    description: constr(min_length=1)
    software_count: int

class PlatformCreate(PlatformBase):
    pass

class PlatformUpdate(PlatformBase):
    pass

class Platform(PlatformBase):
    id: int

    class Config:
        orm_mode = True
