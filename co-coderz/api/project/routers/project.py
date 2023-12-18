from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.project.data.database import get_db
from api.project.crud.project import (
    get_project,
    get_projects,
    create_project,
    update_project,
    delete_project,
)
from api.project.schemas.project import Project, ProjectCreate, ProjectUpdate
from typing import List

router = APIRouter()

@router.get("/{project_id}", response_model=Project)
def read_project(project_id: int, db: Session = Depends(get_db)):
    project = get_project(db, project_id)
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return project

@router.get("/", response_model=List[Project])
def read_projects( creator_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    projects = get_projects(db, creator_id, skip=skip, limit=limit)
    return projects

@router.post("/", response_model=Project)
def create_project_route(project: ProjectCreate, db: Session = Depends(get_db)):
    return create_project(db, project)

@router.put("/{project_id}", response_model=Project)
def update_project_route(project_id: int, project: ProjectUpdate, db: Session = Depends(get_db)):
    updated_project = update_project(db, project_id, project)
    if updated_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return updated_project

@router.delete("/{project_id}", response_model=Project)
def delete_project_route(project_id: int, db: Session = Depends(get_db)):
    deleted_project = delete_project(db, project_id)
    if deleted_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return deleted_project
