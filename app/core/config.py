import os
from typing import List

from dotenv import load_dotenv
from pydantic import AnyHttpUrl

load_dotenv()

class Settings:
    PROJECT_NAME: str = "Blog"
    PROJECT_VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"

    # db
    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

    # jwt 
    ACCESS_TOKEN_EXPIRATION:int = 15 # mins
    REFRESH_TOKEN_EXPIRATION:int = 4320 # mins
    JWT_ALGORITHM = "HS256"
    JWT_SECRET_KEY:str = os.getenv("JWT_SECRET_KEY")

    # cors 
    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200", "http://localhost:3000"]'
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = os.getenv("BACKEND_CORS_ORIGINS")

    class Config:
        case_sensitive = True


settings = Settings()
