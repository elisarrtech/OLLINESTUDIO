from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from typing import List

from app.schemas import ClassCreate, ClassRead
from app.db import get_session
from app import crud
from app.models import ClassSession
from app.api.deps import require_role
from app.models import UserRole

router = APIRouter()

@router.post("/", response_model=ClassRead, dependencies=[Depends(require_role(UserRole.instructor))])
def create_class(payload: ClassCreate, session: Session = Depends(get_session)):
    cls = ClassSession(**payload.dict())
    return crud.create_class(session, cls)

@router.get("/", response_model=List[ClassRead])
def get_classes(session: Session = Depends(get_session)):
    return crud.list_classes(session)
