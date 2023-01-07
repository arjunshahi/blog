from sqlalchemy.orm import Session

from app.models.blog import Blog
from app.models.users import User
from app.schemas.blog import CreateBlogSchema


class BlogService:
    def create_blog(self, payload: CreateBlogSchema, db: Session, user: User):
        blog = Blog(**payload.dict())
        blog.posted_by = user
        db.add(blog)
        db.commit()
        db.refresh(blog)
        return blog

    def get_blog_by_id(self, id, db: Session):
        return db.query(Blog).get(id)

    def get_all_blogs(self, db: Session, skip: int = 0, limit: int = 10):
        return (
            db.query(Blog)
            .order_by(Blog.posted_on.desc())
            .offset(skip)
            .limit(limit)
            .all()
        )

    def blogs_me(self, user:User, db: Session, skip: int = 0, limit: int = 10):
        return (
            db.query(Blog)
            .filter(Blog.posted_by==user)
            .order_by(Blog.posted_on.desc())
            .offset(skip)
            .limit(limit)
            .all()
        )
