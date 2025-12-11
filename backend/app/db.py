from sqlmodel import create_engine, SQLModel, Session
from app.core.config import settings

engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, echo=False)

def init_db():
    # importa modelos para que se registren
    from app import models  # noqa: F401
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
