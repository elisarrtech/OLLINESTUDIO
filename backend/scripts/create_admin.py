# backend/scripts/create_admin.py
from app.db import init_db, get_session
from app.crud import create_user, get_user_by_email

init_db()
with next(get_session()) as session:
    email = "admin@ollin.example"
    if not get_user_by_email(session, email):
        create_user(session, email=email, password="un_password_seguro", full_name="Admin", role="admin")
        print("Admin created")
    else:
        print("Admin exists")
