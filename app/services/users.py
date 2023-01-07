from passlib.context import CryptContext
from sqlalchemy import exists
from sqlalchemy.orm import Session

from app.models.users import User
from app.schemas.user import CreateUserSchema

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserService:
    def _get_password_hash(self, password):
        return pwd_context.hash(password)

    def _verify_password(self, plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)

    def check_email_exists(self, email, db: Session):
        return db.query(exists().where(User.email == email)).scalar()

    def create_user(self, payload: CreateUserSchema, db: Session):
        payload.password = self._get_password_hash(payload.password)
        user = User(**payload.dict())
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    def get_user_by_id(self, id, db: Session):
        return db.query(User).get(id)

    def authenticate(self, email, password, db: Session):
        user = db.query(User).filter_by(email=email).first()
        if user and self._verify_password(password, user.password):
            return user
        return None

    def get_all_users(self, db: Session, skip: int = 0, limit: int = 10):
        return db.query(User).offset(skip).limit(limit).all()
