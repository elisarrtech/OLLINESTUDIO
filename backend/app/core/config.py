from pydantic import BaseSettings, AnyHttpUrl
from typing import List, Optional

class Settings(BaseSettings):
    PROJECT_NAME: str = "ollin-studio-api"
    SECRET_KEY: str = "CHANGE_ME_TO_A_STRONG_SECRET"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7
    # Usa postgres en producción: postgresql://user:pass@postgres:5432/ollin
    SQLALCHEMY_DATABASE_URI: str = "sqlite:///./dev.db"
    BACKEND_CORS_ORIGINS: List[str] = ["http://localhost:5173", "https://ollinestudio.netlify.app"]
    FIRST_SUPERUSER_EMAIL: Optional[str] = None

    class Config:
        env_file = ".env"

settings = Settings()
