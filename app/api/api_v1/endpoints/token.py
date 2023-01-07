from typing import List

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.schemas.token import TokenResponse
from app.services.users import UserService
from app.utils.token import create_access_token, create_refresh_token

router = APIRouter()
user_service = UserService()


@router.post("/", response_model=TokenResponse, status_code=200)
def get_token(
    formdata: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    user = user_service.authenticate(
        db=db, email=formdata.username, password=formdata.password
    )
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    elif not user.is_active:
        raise HTTPException(status_code=400, detail="Inactive User")

    token_data = {
        "access_token": create_access_token(user_id=user.id),
        "refresh_token": create_refresh_token(user_id=user.id),
        "token_type": "bearer"
    }
    return token_data
