# models/license.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from api.software.data.database import Base
from api.software.models.software import software_license_association

class License(Base):
    __tablename__ = 'licenses'
    id = Column(Integer, primary_key=True, index=True, unique=True, nullable=False)

    name = Column(String(length=255), nullable=False)
    description = Column(String, nullable=False)
    software_count = Column(Integer, default=0, nullable=False)

    # Relationship
    software = relationship('Software', secondary=software_license_association, back_populates='licenses')
