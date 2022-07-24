
import os

from pydantic import BaseSettings


class LocalConfig(BaseSettings):
    ENV: str = "development"
    DEBUG: bool = True
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000


class DBConfig(BaseSettings):
    DATABASE_PORT: int = 5432
    DATABASE_SERVER: str = "books-db"
    DATABASE_USER: str = "postgres"
    DATABASE_PASSWORD: str = "postgres"
    DATABASE_DB: str = "books-db"


def get_db_url():
    c = DBConfig()
    return f"postgresql://{c.DATABASE_USER}:{c.DATABASE_PASSWORD}@{c.DATABASE_SERVER}:{c.DATABASE_PORT}/{c.DATABASE_DB}"


def get_config():
    env = os.getenv("ENV", "local")
    config_type = {
        "local": LocalConfig(),
    }
    return config_type[env]


config = get_config()
DATABASE_URL = get_db_url()
