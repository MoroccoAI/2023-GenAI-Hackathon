from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.project.data.database import get_db
from api.project.crud.user import get_user, get_users, create_user, update_user, delete_user
from api.project.schemas.user import User, UserCreate, UserUpdate

from typing import List 

router = APIRouter()

@router.get("/{user_id}", response_model=User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = get_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/", response_model=List[User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = get_users(db, skip=skip, limit=limit)
    return users

@router.post("/", response_model=User)
def create_user_route(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)

@router.put("/{user_id}", response_model=User)
def update_user_route(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    updated_user = update_user(db, user_id, user)
    if updated_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@router.delete("/{user_id}", response_model=User)
def delete_user_route(user_id: int, db: Session = Depends(get_db)):
    deleted_user = delete_user(db, user_id)
    if deleted_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return deleted_user