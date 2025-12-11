from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import date, time, datetime
from app.models import UserRole

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    full_name: Optional[str] = None
    role: UserRole = UserRole.cliente

class UserRead(BaseModel):
    id: int
    email: EmailStr
    full_name: Optional[str]
    role: UserRole
    is_active: bool

    class Config:
        orm_mode = True

class LoginPayload(BaseModel):
    email: EmailStr
    password: str

class ClassCreate(BaseModel):
    title: str
    description: Optional[str] = None
    date: date
    start_time: time
    end_time: time
    capacity: int = 10

class ClassRead(ClassCreate):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

class BookingCreate(BaseModel):
    class_id: int

class BookingRead(BaseModel):
    id: int
    user_id: int
    class_id: int
    created_at: datetime

    class Config:
        orm_mode = True
