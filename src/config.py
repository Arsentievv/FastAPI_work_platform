from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path
from pydantic import Field


class WorkPlatformBase(BaseSettings):
    PROJECT_NAME: str = "Work Platform"
    BASE_DIR: str = str(Path().absolute())


class WorkPlatformDB(WorkPlatformBase):
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str
    DB_HOST: str
    DB_PORT: str

    @property
    def database_url_asyncpg(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    model_config = SettingsConfigDict(env_file="C:\\Users\\Aleksey Arsentyev\\Desktop\\study\\FastAPI_work_platform\\.env")


class WorkPlatformSettings(WorkPlatformDB):
    DEBUG: bool = Field(True)
    postgres: WorkPlatformDB = WorkPlatformDB()


def get_settings(db_only=False):
    return WorkPlatformDB() if db_only else WorkPlatformSettings()