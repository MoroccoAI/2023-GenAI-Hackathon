# routers/tag.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from api.software.crud import tag as tag__crud
from api.software.data.database import get_db
from api.software.schemas.tag import Tag, TagCreate, TagUpdate

router = APIRouter()

@router.post("/", response_model=Tag)
def create_tag(tag: TagCreate, db: Session = Depends(get_db)):
    return tag__crud.create_tag(db, tag)

@router.get("/{tag_id}", response_model=Tag)
def read_tag(tag_id: int, db: Session = Depends(get_db)):
    return tag__crud.get_tag(db, tag_id)

@router.get("/name/{tag_name}", response_model=Tag)
def read_tag_by_name(tag_name: str, db: Session = Depends(get_db)):
    return tag__crud.get_tag_by_name(db, tag_name)

@router.get("/", response_model=List[Tag])
def read_all_tags(db: Session = Depends(get_db)):
    return tag__crud.get_all_tags(db)

@router.put("/{tag_id}", response_model=Tag)
def update_tag(tag_id: int, tag: TagUpdate, db: Session = Depends(get_db)):
    return tag__crud.update_tag(db, tag_id, tag)

@router.delete("/{tag_id}", response_model=Tag)
def delete_tag(tag_id: int, db: Session = Depends(get_db)):
    return tag__crud.delete_tag(db, tag_id)
