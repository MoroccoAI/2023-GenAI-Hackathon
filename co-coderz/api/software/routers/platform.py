# routers/platform.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from api.software.crud import platform as platform_crud
from api.software.data.database import get_db
from api.software.schemas.platform import Platform, PlatformCreate, PlatformUpdate

router = APIRouter()

@router.post("/", response_model=Platform)
def create_platform(platform: PlatformCreate, db: Session = Depends(get_db)):
    return platform_crud.create_platform(db, platform)

@router.get("/{platform_id}", response_model=Platform)
def read_platform(platform_id: int, db: Session = Depends(get_db)):
    return platform_crud.get_platform(db, platform_id)

@router.get("/name/{platform_name}", response_model=Platform)
def read_platform_by_name(platform_name: str, db: Session = Depends(get_db)):
    return platform_crud.get_platform_by_name(db, platform_name)

@router.get("/", response_model=List[Platform])
def read_all_platforms(db: Session = Depends(get_db)):
    return platform_crud.get_all_platforms(db)

@router.put("/{platform_id}", response_model=Platform)
def update_platform(platform_id: int, platform: PlatformUpdate, db: Session = Depends(get_db)):
    return platform_crud.update_platform(db, platform_id, platform)

@router.delete("/{platform_id}", response_model=Platform)
def delete_platform(platform_id: int, db: Session = Depends(get_db)):
    return platform_crud.delete_platform(db, platform_id)
