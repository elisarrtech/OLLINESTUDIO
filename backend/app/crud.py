from sqlmodel import Session, select
from typing import Optional, List

from app.models import User, ClassSession, Booking
from app.core.security import get_password_hash

# Users
def get_user_by_email(session: Session, email: str) -> Optional[User]:
    return session.exec(select(User).where(User.email == email)).first()

def create_user(session: Session, email: str, password: str, full_name: Optional[str] = None) -> User:
    user = User(email=email, full_name=full_name, hashed_password=get_password_hash(password))
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

# Classes
def create_class(session: Session, cls_data: ClassSession) -> ClassSession:
    session.add(cls_data)
    session.commit()
    session.refresh(cls_data)
    return cls_data

def list_classes(session: Session, skip: int = 0, limit: int = 100) -> List[ClassSession]:
    return session.exec(select(ClassSession).offset(skip).limit(limit)).all()

# Bookings
def create_booking(session: Session, user_id: int, class_id: int) -> Booking:
    booking = Booking(user_id=user_id, class_id=class_id)
    session.add(booking)
    session.commit()
    session.refresh(booking)
    return booking

def get_bookings_for_class(session: Session, class_id: int) -> List[Booking]:
    return session.exec(select(Booking).where(Booking.class_id == class_id)).all()
