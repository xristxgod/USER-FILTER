from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "CRUD User"
    db_path: str

    class Config:
        env_file = ".env"


@lru_cache()
def get_settings():
    return Settings()


__all__ = [
    "get_settings"
]
