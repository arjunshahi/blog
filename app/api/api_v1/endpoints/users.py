from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.schemas.user import CreateUserSchema, UserResponse
from app.services.users import UserService

router = APIRouter()
user_service = UserService()


@router.post("/", response_model=UserResponse, status_code=201)
def singup_user(payload: CreateUserSchema, db: Session = Depends(get_db)):
    if user_service.check_email_exists(db=db, email=payload.email):
        raise HTTPException(status_code=400, detail="Email Already Exists.")
    user = user_service.create_user(db=db, payload=payload)
    return user


@router.get("/", response_model=List[UserResponse], status_code=200)
def list_all_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = user_service.get_all_users(db=db, skip=skip, limit=limit)
    return users


@router.get("/{user_id}", response_model=UserResponse, status_code=200)
def get_user_by_id(user_id, db: Session = Depends(get_db)):
    user = user_service.get_user_by_id(db=db, id=user_id)
    return user
