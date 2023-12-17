# models/software.py
from sqlalchemy import Table, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Boolean
from api.software.data.database import Base

# Association Tables
software_license_association = Table(
    'software_license_association',
    Base.metadata,
    Column('software_id', Integer, ForeignKey('software.id')),
    Column('license_id', Integer, ForeignKey('licenses.id'))
)

software_platform_association = Table(
    'software_platform_association',
    Base.metadata,
    Column('software_id', Integer, ForeignKey('software.id')),
    Column('platform_id', Integer, ForeignKey('platforms.id'))
)

software_tag_association = Table(
    'software_tag_association',
    Base.metadata,
    Column('software_id', Integer, ForeignKey('software.id')),
    Column('tag_id', Integer, ForeignKey('tags.id'))
)

class Software(Base):
    __tablename__ = 'software'
    id = Column(Integer, primary_key=True, index=True, unique=True, nullable=False)
    name = Column(String(length=255), nullable=False)
    website_url = Column(String, nullable=True)
    description = Column(String, nullable=False)
    source_code_url = Column(String, nullable=True)
    stargazers_count = Column(Integer, nullable=True)
    updated_at = Column(String, nullable=True)
    archived = Column(Boolean, nullable=True)
    demo_url = Column(String, nullable=True)
    depends_3rdparty = Column(Boolean, nullable=False)
    related_software_url = Column(String, nullable=True)

    # Relationships
    licenses = relationship('License', secondary=software_license_association, back_populates='software')
    platforms = relationship('Platform', secondary=software_platform_association, back_populates='software')
    tags = relationship('Tag', secondary=software_tag_association, back_populates='software')
