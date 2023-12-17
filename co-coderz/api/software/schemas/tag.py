# schemas/tag.py
from pydantic import BaseModel, constr
from typing import Dict, List

class TagBase(BaseModel):
    name: constr(min_length=1, max_length=255)
    description: constr(min_length=1)
    related_tags: List[str] = []
    redirect: Dict[str, str] = {}
    external_links: Dict[str, str] = {}

class TagCreate(TagBase):
    pass

class TagUpdate(TagBase):
    pass

class Tag(TagBase):
    id: int

    class Config:
        orm_mode = True
