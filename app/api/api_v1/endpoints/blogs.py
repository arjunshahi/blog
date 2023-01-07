from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_current_user, get_db
from app.models.users import User
from app.schemas.blog import BlogResponse, CreateBlogSchema
from app.services.blog import BlogService

router = APIRouter()
blog_service = BlogService()


@router.get("/", response_model=List[BlogResponse], status_code=200)
def list_blogs(db: Session = Depends(get_db), skip: int = 0, limit: int = 10):
    blogs = blog_service.get_all_blogs(db=db, skip=skip, limit=limit)
    return blogs


@router.post("/", response_model=BlogResponse, status_code=201)
def create_blog(
    payload: CreateBlogSchema,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    blog = blog_service.create_blog(db=db, payload=payload, user=user)
    return blog


@router.get("/me", response_model=List[BlogResponse], status_code=200)
def blogs_me(
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
    skip: int = 0,
    limit: int = 10,
):
    blogs = blog_service.blogs_me(db=db, skip=skip, limit=limit, user=user)
    return blogs


@router.get("/{blog_id}", response_model=BlogResponse, status_code=200)
def get_blog_by_id(blog_id, db: Session = Depends(get_db)):
    blog = blog_service.get_blog_by_id(db=db, id=blog_id)
    return blog
