# routers/license.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from api.software.crud import license as license_crud
from api.software.data.database import get_db
from api.software.schemas.license import License, LicenseCreate, LicenseUpdate

router = APIRouter()

@router.post("/", response_model=License)
def create_license(license: LicenseCreate, db: Session = Depends(get_db)):
    return license_crud.create_license(db, license)

@router.get("/{license_id}", response_model=License)
def read_license(license_id: int, db: Session = Depends(get_db)):
    return license_crud.get_license(db, license_id)

@router.get("/name/{license_name}", response_model=License)
def read_license_by_name(license_name: str, db: Session = Depends(get_db)):
    return license_crud.get_license_by_name(db, license_name)

@router.get("/", response_model=List[License])
def read_all_licenses(db: Session = Depends(get_db)):
    return license_crud.get_all_licenses(db)

@router.put("/{license_id}", response_model=License)
def update_license(license_id: int, license: LicenseUpdate, db: Session = Depends(get_db)):
    return license_crud.update_license(db, license_id, license)

@router.delete("/{license_id}", response_model=License)
def delete_license(license_id: int, db: Session = Depends(get_db)):
    return license_crud.delete_license(db, license_id)
