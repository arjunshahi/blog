from app.core.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

sql_engine = create_engine(settings.DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=sql_engine)
