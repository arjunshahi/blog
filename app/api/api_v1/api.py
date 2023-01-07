from fastapi import APIRouter

from app.api.api_v1.endpoints import blogs, users, token

api_router = APIRouter()
api_router.include_router(token.router, prefix="/token", tags=["token"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(blogs.router, prefix="/blogs", tags=["blogs"])
