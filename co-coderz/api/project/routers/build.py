from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.project.data.database import get_db
from api.project.crud.build import (
    get_build,
    get_builds,
    create_build,
    update_build,
    delete_build,
)
from api.project.schemas.build import Build, BuildCreate, BuildUpdate
from typing import List

router = APIRouter()

@router.get("/{build_id}", response_model=Build)
def read_build(build_id: int, db: Session = Depends(get_db)):
    build = get_build(db, build_id)
    if build is None:
        raise HTTPException(status_code=404, detail="Build not found")
    return build

@router.get("/", response_model=List[Build])
def read_builds(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    builds = get_builds(db, skip=skip, limit=limit)
    return builds

@router.post("/", response_model=Build)
def create_build_route(build: BuildCreate, db: Session = Depends(get_db)):
    return create_build(db, build)

@router.put("/{build_id}", response_model=Build)
def update_build_route(build_id: int, build: BuildUpdate, db: Session = Depends(get_db)):
    updated_build = update_build(db, build_id, build)
    if updated_build is None:
        raise HTTPException(status_code=404, detail="Build not found")
    return updated_build

@router.delete("/{build_id}", response_model=Build)
def delete_build_route(build_id: int, db: Session = Depends(get_db)):
    deleted_build = delete_build(db, build_id)
    if deleted_build is None:
        raise HTTPException(status_code=404, detail="Build not found")
    return deleted_build
