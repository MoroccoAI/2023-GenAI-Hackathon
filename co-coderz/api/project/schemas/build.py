from pydantic import BaseModel

class BuildBase(BaseModel):
    project_id: int
    software_ids: dict
    generated_at: str

    class Config:
        orm_mode = True

class BuildCreate(BuildBase):
    pass

class BuildUpdate(BuildBase):
    pass

class Build(BuildBase):
    id: int

    class Config:
        orm_mode = True