from pydantic import MongoDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseModelConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_file="./.env", env_file_encoding="utf-8", extra="ignore"
    )
    DATABASE_USER: str
    DATABASE_PASSWORD: str
    DATABASE_HOST: str
    DATABASE_PORT: int
    DATABASE_NAME: str


class MongoConfig(DatabaseModelConfig):
    @property
    def DATABASE_URL(self) -> MongoDsn:
        return MongoDsn.build(
            scheme="mongodb",
            username=self.DATABASE_USER,
            password=self.DATABASE_PASSWORD,
            host=self.DATABASE_HOST,
            port=self.DATABASE_PORT,
            path=self.DATABASE_NAME,
        )
