from datetime import datetime

from app.schemas.common import OrmBaseModel
from fastapi import Depends

from app.schemas.user import UserResponse


class BlogBaseSchema(OrmBaseModel):
    title: str
    content: str
    is_published: bool = True


class BlogResponse(BlogBaseSchema):
    id: int
    posted_on: datetime
    posted_by: UserResponse


class CreateBlogSchema(BlogBaseSchema):
    pass
    

class UpdateBlogSchema(BlogBaseSchema):
    pass


class CommentBaseSchema(OrmBaseModel):
    comment: str


class CommentResponse(CommentBaseSchema):
    id: int
    blog: BlogResponse
    user: UserResponse
