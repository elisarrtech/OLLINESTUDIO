from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from typing import List

from app.schemas import ClassCreate, ClassRead
from app.db import get_session
from app.models import ClassSession
from app import crud

router = APIRouter()

@router.post("/", response_model=ClassRead)
def create_class(payload: ClassCreate, session: Session = Depends(get_session)):
    cls = ClassSession(**payload.dict())
    session.add(cls)
    session.commit()
    session.refresh(cls)
    return cls

@router.get("/", response_model=List[ClassRead])
def get_classes(session: Session = Depends(get_session)):
    return session.exec(ClassSession.select()).all()
