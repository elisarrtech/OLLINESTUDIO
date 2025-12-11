from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.db import init_db
from app.api import routes_auth, routes_classes, routes_bookings

app = FastAPI(title="OLLIN STUDIO API")

# BACKEND_CORS_ORIGINS puede ser lista o string CSV en .env
raw = settings.BACKEND_CORS_ORIGINS
if isinstance(raw, str):
    origins = [o.strip() for o in raw.split(",") if o.strip()]
else:
    origins = raw

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins or ["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routes_auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(routes_classes.router, prefix="/api/classes", tags=["classes"])
app.include_router(routes_bookings.router, prefix="/api/bookings", tags=["bookings"])


@app.on_event("startup")
def on_startup():
    init_db()
    # Opcional: crear superuser automático si FIRST_SUPERUSER_EMAIL está configurado
    from app.core.initial_data import create_first_superuser
    create_first_superuser()
