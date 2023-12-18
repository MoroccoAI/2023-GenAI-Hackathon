# crud/software.py
from sqlalchemy.orm import Session
from typing import List, Optional
from api.software.models.software import Software
from api.software.models.license import License
from api.software.models.platform import Platform
from api.software.models.tag import Tag
from api.software.schemas.software import SoftwareCreate, SoftwareUpdate

def create_software(db: Session, software: SoftwareCreate) -> Software:
    # Extracting association IDs
    license_ids = software.license_ids or []
    platform_ids = software.platform_ids or []
    tag_ids = software.tag_ids or []

    # Creating a dictionary from the SoftwareCreate instance
    software_data = software.dict()

    # Removing association-related keys from the dictionary
    for key in ("license_ids", "platform_ids", "tag_ids"):
        if key in software_data:
            del software_data[key]

    # Creating a new Software instance with the remaining data
    db_software = Software(**software_data)

    # Adding associations
    db_software.licenses = db.query(License).filter(License.id.in_(license_ids)).all()
    db_software.platforms = db.query(Platform).filter(Platform.id.in_(platform_ids)).all()
    db_software.tags = db.query(Tag).filter(Tag.id.in_(tag_ids)).all()

    # Adding and committing the new software instance
    db.add(db_software)
    db.commit()
    db.refresh(db_software)
    return db_software

def get_software(db: Session, software_id: int) -> Optional[Software]:
    return db.query(Software).filter(Software.id == software_id).first()

def get_all_software(db: Session, page: int = 1, per_page: int = 10) -> List[Software]:
    return db.query(Software).offset((page - 1) * per_page).limit(per_page).all()


def update_software(db: Session, software_id: int, software: SoftwareUpdate) -> Optional[Software]:
    db_software = db.query(Software).filter(Software.id == software_id).first()

    if db_software:
        for field, value in software.dict().items():
            setattr(db_software, field, value)

        # Update associations
        if software.license_ids:
            db_software.licenses = db.query(License).filter(License.id.in_(software.license_ids)).all()
        if software.platform_ids:
            db_software.platforms = db.query(Platform).filter(Platform.id.in_(software.platform_ids)).all()
        if software.tag_ids:
            db_software.tags = db.query(Tag).filter(Tag.id.in_(software.tag_ids)).all()

        db.commit()
        db.refresh(db_software)
    return db_software

def delete_software(db: Session, software_id: int) -> Optional[Software]:
    db_software = db.query(Software).filter(Software.id == software_id).first()
    db.delete(db_software)
    db.commit()
    return db_software
