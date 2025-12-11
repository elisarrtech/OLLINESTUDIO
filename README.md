# OLLINESTUDIO
Sistema de reservas para clases de pilates
# Backend - OLLIN STUDIO

Instrucciones rápidas:

1. Copia `.env.example` a `.env` y ajusta `SECRET_KEY` y `DATABASE_URL`.
2. Para desarrollo rápido con SQLite:
   - DATABASE_URL=sqlite:///./dev.db
3. Levantar con Docker Compose (si usas docker-compose desde la raíz):
   - docker-compose up --build
4. En Railway:
   - Configura root directory: backend
   - Añade variables: DATABASE_URL, SECRET_KEY, BACKEND_CORS_ORIGINS
   - Railway detecta Dockerfile e iniciará el build
5. Crear admin:
   - Ejecuta: python scripts/create_admin.py (o desde Railway: run at project console)

Notas:
- Para migraciones usa Alembic. Este scaffold usa SQLModel.create_all() por simplicidad en primer deploy.
- No subas `.env` al repo.
