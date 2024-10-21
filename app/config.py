from pydantic import BaseSettings
import os


class Settings(BaseSettings):
    # Project settings
    project_name: str
    project_version: str
    project_description: str
    frontend_base_url: str
    allowed_origins: list

    # Database settings
    mongodb_uri: str
    redis_host: str
    redis_port: int
    rabbitmq_uri: str

    # Auth settings
    jwt_secret: str
    jwt_algorithm: str
    jwt_expiration: int

    # Email settings
    smtp_host: str
    smtp_port: int
    smtp_username: str
    smtp_password: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
