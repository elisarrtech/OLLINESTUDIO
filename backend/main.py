from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import routes_auth, routes_classes, routes_bookings
from app.db import init_db
from app.core.config import settings

app = FastAPI(title="OLLIN STUDIO API")

# CORS - ajusta los orígenes según tu frontend (Vite / Netlify)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
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
