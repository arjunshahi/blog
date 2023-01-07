import traceback

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from sqlalchemy.orm import Session

from app.core.config import settings
from app.db.session import SessionLocal
from app.schemas.token import TokenResponse
from app.services.users import UserService

reusable_oauth2 = OAuth2PasswordBearer(tokenUrl=f"{settings.API_V1_STR}/token")


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def get_current_user(
    db: Session = Depends(get_db), token: str = Depends(reusable_oauth2)
):
    try:
        payload = jwt.decode(token, settings.JWT_SECRET_KEY, [settings.JWT_ALGORITHM])
    except Exception as e:
        print(e, traceback.format_exc())
        raise HTTPException(
            status_code=403,
            detail="Could not validate credentials",
        )

    user = UserService().get_user_by_id(db=db, id=payload.get("user_id"))
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
