from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from typing import List

from app.schemas import BookingCreate, BookingRead
from app.db import get_session
from app import crud

router = APIRouter()

@router.post("/", response_model=BookingRead)
def book_class(payload: BookingCreate, session: Session = Depends(get_session)):
    # Aquí deberías validar capacidad, usuario autenticado, etc.
    booking = crud.create_booking(session, user_id=1, class_id=payload.class_id)  # placeholder user_id
    return booking
