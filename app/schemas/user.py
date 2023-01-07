from datetime import datetime

from pydantic import BaseModel, EmailStr
from typing import List
from app.schemas.common import OrmBaseModel

class UserBaseSchema(OrmBaseModel):
    full_name: str
    email: EmailStr


class UserResponse(UserBaseSchema):
    id: int
    is_active: bool
    is_superuser: bool
    joined_on: datetime


class CreateUserSchema(UserBaseSchema):
    password: str


class UpdateUserSchema(UserBaseSchema):
    pass
