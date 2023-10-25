from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict


class Settings(BaseSettings):
    """Environment variables configuration"""

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    DATABASE_URL: str
    APP_NAME: str
    DOCS_PATH: str
    APP_DESCRIPTION: str
    ORIGINS: str


settings = Settings()
