from sqlalchemy.orm import Session
from api.project.models.build import Build
from api.project.schemas.build import BuildCreate, BuildUpdate

def get_build(db: Session, build_id: int):
    return db.query(Build).filter(Build.id == build_id).first()

def get_builds(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Build).offset(skip).limit(limit).all()

def create_build(db: Session, build: BuildCreate):
    db_build = Build(**build.dict())
    db.add(db_build)
    db.commit()
    db.refresh(db_build)
    return db_build

def update_build(db: Session, build_id: int, build: BuildUpdate):
    db_build = db.query(Build).filter(Build.id == build_id).first()
    if db_build:
        for key, value in build.dict(exclude_unset=True).items():
            setattr(db_build, key, value)
        db.commit()
        db.refresh(db_build)
    return db_build

def delete_build(db: Session, build_id: int):
    db_build = db.query(Build).filter(Build.id == build_id).first()
    if db_build:
        db.delete(db_build)
        db.commit()
        db.refresh(db_build)
    return db_build
