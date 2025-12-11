# Script utilitario para crear admin desde CLI (ejecutar en Railway run o localmente)
from app.db import init_db
from sqlmodel import Session
from app.db import engine
from app import crud

def create_admin(email: str, password: str, full_name: str = "Admin"):
    init_db()
    with Session(engine) as session:
        existing = crud.get_user_by_email(session, email)
        if existing:
            print("Admin ya existe:", email)
            return
        crud.create_user(session, email=email, password=password, full_name=full_name, role="admin")
        print("Admin creado:", email)

if __name__ == "__main__":
    import os
    email = os.environ.get("FIRST_SUPERUSER_EMAIL", "admin@ollin.example")
    password = os.environ.get("FIRST_SUPERUSER_PASSWORD", "changeme123")
    create_admin(email, password)
