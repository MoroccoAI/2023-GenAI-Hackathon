from pydantic import BaseModel
from datetime import date, datetime

class ProjectBase(BaseModel):
    name: str
    description: str
    type: str
    industry: str
    start_date: date
    end_date: date
    status: str
    budget: float
    team_size: int
    details: dict
    creator_id: int

class ProjectCreate(ProjectBase):
    pass

class ProjectUpdate(ProjectBase):
    pass

class Project(ProjectBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
