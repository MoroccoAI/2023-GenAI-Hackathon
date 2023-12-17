# schemas/license.py
from pydantic import BaseModel, constr

class LicenseBase(BaseModel):
    name: constr(min_length=1, max_length=255)
    description: constr(min_length=1)
    software_count: int

class LicenseCreate(LicenseBase):
    pass

class LicenseUpdate(LicenseBase):
    pass

class License(LicenseBase):
    id: int

    class Config:
        orm_mode = True
