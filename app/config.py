from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Memoki"
    MONGODB_URL: str
    REDIS_URL: str
    RABBITMQ_URL: str

    class Config:
        env_prefix = "MEMOKI_"
        env_file = ".env"


settings = Settings()
