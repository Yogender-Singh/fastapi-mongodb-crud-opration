from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "FastAPI App"
    mongo_url: str = "mongodb://localhost:27017"
    debug: bool = True

    class Config:
        env_file = ".env"


settings = Settings()
