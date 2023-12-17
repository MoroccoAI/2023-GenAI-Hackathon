# crud/license.py
from sqlalchemy.orm import Session
from typing import List
from api.software.models.license import License
from api.software.schemas.license import LicenseCreate, LicenseUpdate

def create_license(db: Session, license: LicenseCreate) -> License:
    db_license = License(**license.dict())
    db.add(db_license)
    db.commit()
    db.refresh(db_license)
    return db_license

def get_license(db: Session, license_id: int) -> License:
    return db.query(License).filter(License.id == license_id).first()

def get_license_by_name(db: Session, license_name: str) -> License:
    return db.query(License).filter(License.name == license_name).first()

def get_all_licenses(db: Session) -> List[License]:
    return db.query(License).all()

def update_license(db: Session, license_id: int, license: LicenseUpdate) -> License:
    db_license = db.query(License).filter(License.id == license_id).first()
    for field, value in license.dict().items():
        setattr(db_license, field, value)
    db.commit()
    db.refresh(db_license)
    return db_license

def delete_license(db: Session, license_id: int) -> License:
    db_license = db.query(License).filter(License.id == license_id).first()
    db.delete(db_license)
    db.commit()
    return db_license
