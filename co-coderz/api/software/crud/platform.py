# crud/platform.py
from sqlalchemy.orm import Session
from typing import List
from api.software.models.platform import Platform
from api.software.schemas.platform import PlatformCreate, PlatformUpdate

def create_platform(db: Session, platform: PlatformCreate) -> Platform:
    db_platform = Platform(**platform.dict())
    db.add(db_platform)
    db.commit()
    db.refresh(db_platform)
    return db_platform

def get_platform(db: Session, platform_id: int) -> Platform:
    return db.query(Platform).filter(Platform.id == platform_id).first()

def get_platform_by_name(db: Session, platform_name: str) -> Platform:
    return db.query(Platform).filter(Platform.name == platform_name).first()

def get_all_platforms(db: Session) -> List[Platform]:
    return db.query(Platform).all()

def update_platform(db: Session, platform_id: int, platform: PlatformUpdate) -> Platform:
    db_platform = db.query(Platform).filter(Platform.id == platform_id).first()
    for field, value in platform.dict().items():
        setattr(db_platform, field, value)
    db.commit()
    db.refresh(db_platform)
    return db_platform

def delete_platform(db: Session, platform_id: int) -> Platform:
    db_platform = db.query(Platform).filter(Platform.id == platform_id).first()
    db.delete(db_platform)
    db.commit()
    return db_platform
