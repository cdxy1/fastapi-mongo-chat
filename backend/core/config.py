from pydantic import MongoDsn, RedisDsn
from pydantic_settings import BaseSettings, SettingsConfigDict

from backend.utils.config import get_env


class ModelConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=get_env(), env_file_encoding="utf-8", extra="ignore"
    )
    
class DatabaseConfig(ModelConfig):
    DATABASE_USER: str
    DATABASE_PASSWORD: str
    DATABASE_HOST: str
    DATABASE_PORT: int
    DATABASE_NAME: str
    
class RedisConfig(ModelConfig):
    REDIS_HOST: str
    REDIS_PORT: int
    
class SecurityConfig(ModelConfig):
    SECRET_KEY: str
    ALGORITHM: str

class MongoConfig(DatabaseConfig):
    @property
    def DATABASE_URL(self) -> str:
        return f"mongodb://{self.DATABASE_USER}:{self.DATABASE_PASSWORD}@{self.DATABASE_HOST}:{self.DATABASE_PORT}"
        
class RedisConfig(RedisConfig):
    @property
    def REDIS_URL(self):
        return f"redis://{self.REDIS_HOST}:{self.REDIS_PORT}"

MONGO_DB = MongoConfig()
REDIS = RedisConfig()
SECURITY = SecurityConfig()
