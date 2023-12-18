# schemas/software.py
from pydantic import BaseModel, constr
from typing import Optional, List
from api.software.schemas.license import License
from api.software.schemas.platform import Platform
from api.software.schemas.tag import Tag

class SoftwareBase(BaseModel):
    name: constr(min_length=1, max_length=255)
    website_url: Optional[str]
    description: constr(min_length=1)
    source_code_url: Optional[str]
    stargazers_count: Optional[int]
    updated_at: Optional[str]
    archived: Optional[bool]
    demo_url: Optional[str]
    depends_3rdparty: bool
    related_software_url: Optional[str]

class SoftwareCreate(SoftwareBase):
    license_ids: Optional[List[int]]
    platform_ids: Optional[List[int]]
    tag_ids: Optional[List[int]]

class SoftwareUpdate(SoftwareBase):
    pass

class Software(SoftwareBase):
    id: int
    licenses: Optional[List[License]]
    platforms: Optional[List[Platform]]
    tags: Optional[List[Tag]]

    class Config:
        orm_mode = True
