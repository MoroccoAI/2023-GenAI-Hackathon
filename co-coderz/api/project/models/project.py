from sqlalchemy import Column, Integer, String, Date, Float, DateTime, ForeignKey, JSON, text
from sqlalchemy.orm import relationship
from api.project.data.database import Base
from datetime import datetime

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    creator_id = Column(Integer, ForeignKey("users.id"), index=True, nullable=False)

    name = Column(String(255), index=True, nullable=False)
    description = Column(String(255), nullable=False)
    type = Column(String(255), nullable=False)
    industry = Column(String(255), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    status = Column(String(255), nullable=False)
    budget = Column(Float, nullable=False)
    team_size = Column(Integer, nullable=False)
    details = Column(JSON, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, server_default=text('CURRENT_TIMESTAMP'), nullable=False)

    creator = relationship("User", back_populates="projects")
    builds = relationship("Build", back_populates="project")