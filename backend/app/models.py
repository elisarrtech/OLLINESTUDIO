from typing import Optional
from sqlmodel import SQLModel, Field
from datetime import datetime, date, time
from enum import Enum

class UserRole(str, Enum):
    admin = "admin"
    instructor = "instructor"
    cliente = "cliente"

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(index=True, nullable=False, unique=True)
    full_name: Optional[str] = None
    hashed_password: str
    role: UserRole = Field(default=UserRole.cliente)
    is_active: bool = True
    created_at: datetime = Field(default_factory=datetime.utcnow)

class ClassSession(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: Optional[str] = None
    date: date
    start_time: time
    end_time: time
    capacity: int = 10
    created_at: datetime = Field(default_factory=datetime.utcnow)

class Booking(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    class_id: int = Field(foreign_key="classsession.id")
    created_at: datetime = Field(default_factory=datetime.utcnow)
