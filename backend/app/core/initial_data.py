# Script pequeño para crear un superuser si se configura en env
from app.core.config import settings
from app.db import engine
from sqlmodel import Session
from app import crud

def create_first_superuser():
    if not settings.FIRST_SUPERUSER_EMAIL or not settings.FIRST_SUPERUSER_PASSWORD:
        return
    with Session(engine) as session:
        existing = crud.get_user_by_email(session, settings.FIRST_SUPERUSER_EMAIL)
        if existing:
            return
        crud.create_user(session, email=settings.FIRST_SUPERUSER_EMAIL, password=settings.FIRST_SUPERUSER_PASSWORD, full_name="Admin", role="admin")
