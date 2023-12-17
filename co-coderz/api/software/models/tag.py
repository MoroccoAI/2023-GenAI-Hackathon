# Assuming you're using SQLAlchemy
from sqlalchemy import Column, Integer, String, Text, JSON
from sqlalchemy.orm import relationship
from api.software.data.database import Base
from api.software.models.software import software_tag_association

class Tag(Base):
    __tablename__ = "tags"
    id = Column(Integer, primary_key=True, index=True, unique=True, nullable=False)

    name = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    external_links = Column(JSON, nullable=True)
    redirect = Column(JSON, nullable=True)
    related_tags = Column(JSON, nullable=True)

    # Relationships
    software = relationship('Software', secondary=software_tag_association, back_populates='tags')
