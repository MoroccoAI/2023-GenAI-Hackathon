# crud/tag.py
from sqlalchemy.orm import Session
from typing import List
from api.software.models.tag import Tag
from api.software.schemas.tag import TagCreate, TagUpdate

def create_tag(db: Session, tag: TagCreate) -> Tag:
    db_tag = Tag(**tag.dict())
    db.add(db_tag)
    db.commit()
    db.refresh(db_tag)
    return db_tag

def get_tag_by_name(db: Session, tag_name: str) -> Tag:
    return db.query(Tag).filter(Tag.name == tag_name).first()

def get_tag(db: Session, tag_id: int) -> Tag:
    return db.query(Tag).filter(Tag.id == tag_id).first()

def get_all_tags(db: Session) -> List[Tag]:
    return db.query(Tag).all()

def update_tag(db: Session, tag_id: int, tag: TagUpdate) -> Tag:
    db_tag = db.query(Tag).filter(Tag.id == tag_id).first()
    for field, value in tag.dict().items():
        setattr(db_tag, field, value)
    db.commit()
    db.refresh(db_tag)
    return db_tag

def delete_tag(db: Session, tag_id: int) -> Tag:
    db_tag = db.query(Tag).filter(Tag.id == tag_id).first()
    db.delete(db_tag)
    db.commit()
    return db_tag
