from fastapi import FastAPI
from app.core.config import settings
from app.db.session import sql_engine
from app.db.base import Base

def create_tables():
    Base.metadata.create_all(bind=sql_engine)


def start_app():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    # create_tables()
    # print("creating tables")
    return app

app = start_app()
