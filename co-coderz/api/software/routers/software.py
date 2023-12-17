# routers/software.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from api.software.crud import software as software_crud
from api.software.data.database import get_db
from api.software.schemas.software import Software, SoftwareCreate, SoftwareUpdate

router = APIRouter()

@router.post("/", response_model=Software)
def create_software(software: SoftwareCreate, db: Session = Depends(get_db)):
    return software_crud.create_software(db, software)

@router.get("/{software_id}", response_model=Optional[Software])
def read_software(software_id: int, db: Session = Depends(get_db)):
    return software_crud.get_software(db, software_id)

@router.get("/", response_model=List[Software])
def read_all_software(db: Session = Depends(get_db)):
    return software_crud.get_all_software(db)

@router.put("/{software_id}", response_model=Optional[Software])
def update_software(software_id: int, software: SoftwareUpdate, db: Session = Depends(get_db)):
    return software_crud.update_software(db, software_id, software)

@router.delete("/{software_id}", response_model=Optional[Software])
def delete_software(software_id: int, db: Session = Depends(get_db)):
    return software_crud.delete_software(db, software_id)
