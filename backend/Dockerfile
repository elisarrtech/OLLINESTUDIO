 url=https://github.com/elisarrtech/OLLINESTUDIO/blob/main/backend/Dockerfile
FROM python:3.11-slim

# Instala dependencias del sistema necesarias para compilación y psycopg2
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copia requirements y actualiza pip antes de instalar
COPY requirements.txt .
RUN pip install --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código
COPY . .

# Usa gunicorn + uvicorn workers para producción (Railway expone PORT)
# Si prefieres uvicorn directamente, reemplaza la línea CMD por uvicorn ...
CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "-w", "4", "-b", "0.0.0.0:$PORT", "app.main:app"]
