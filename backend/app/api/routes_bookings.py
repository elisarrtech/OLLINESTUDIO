from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from app.schemas import BookingCreate, BookingRead
from app.db import get_session
from app import crud
from app.api.deps import get_current_user

router = APIRouter()

@router.post("/", response_model=BookingRead)
def book_class(payload: BookingCreate, session: Session = Depends(get_session), current_user = Depends(get_current_user)):
    # Validar capacidad
    count = crud.count_bookings_for_class(session, payload.class_id)
    # Obtener clase para revisar capacity (simple consulta)
    from app.models import ClassSession
    cls = session.get(ClassSession, payload.class_id)
    if not cls:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Clase no encontrada")
    if count >= cls.capacity:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Clase llena")
    booking = crud.create_booking(session, user_id=current_user.id, class_id=payload.class_id)
    return booking
