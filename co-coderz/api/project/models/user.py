from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from api.project.data.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    auth0_id = Column(String(255), unique=True, nullable=False)

    full_name = Column(String(255), nullable=False)
    company = Column(String(255), nullable=True)
    role = Column(String(255), nullable=True)
    
    projects = relationship("Project", back_populates="creator")