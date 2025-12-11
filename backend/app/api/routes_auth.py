from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from datetime import timedelta

from app.schemas import UserCreate, UserRead, Token
from app.db import get_session
from app import crud
from app.core.security import verify_password, create_access_token

router = APIRouter()

@router.post("/register", response_model=UserRead)
def register(user_in: UserCreate, session: Session = Depends(get_session)):
    existing = crud.get_user_by_email(session, user_in.email)
    if existing:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    user = crud.create_user(session, email=user_in.email, password=user_in.password, full_name=user_in.full_name)
    return user

@router.post("/login", response_model=Token)
def login(form_data: UserCreate, session: Session = Depends(get_session)):
    user = crud.get_user_by_email(session, form_data.email)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    access_token = create_access_token(subject=str(user.id), expires_delta=timedelta(days=7))
    return {"access_token": access_token}
