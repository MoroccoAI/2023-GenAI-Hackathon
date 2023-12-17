from sqlalchemy import Column, Integer, DateTime, ForeignKey, JSON
from sqlalchemy.orm import relationship
from api.project.data.database import Base

class Build(Base):
    __tablename__ = "builds"

    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"), index=True, nullable=False)
    
    software_ids = Column(JSON(Integer), nullable=False)
    generated_at = Column(DateTime, nullable=False)

    project = relationship("Project", back_populates="builds")
