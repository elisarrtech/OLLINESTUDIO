# OLLINESTUDIO
Sistema de reservas para clases de pilates

## Despliegue en Railway

Para desplegar el backend en Railway, asegúrate de configurar las siguientes variables de entorno:

- `DATABASE_URL`: URL de conexión a PostgreSQL (ej: `postgresql://user:pass@host:5432/dbname`)
- `SECRET_KEY`: Clave secreta para JWT (genera una clave segura)
- `BACKEND_CORS_ORIGINS`: Lista de orígenes permitidos para CORS (ej: `["http://localhost:5173","https://tuapp.netlify.app"]`)
- `ACCESS_TOKEN_EXPIRE_MINUTES`: Tiempo de expiración del token de acceso en minutos (opcional, por defecto: 10080 = 7 días)

Railway detectará automáticamente el `Dockerfile` en la carpeta `backend/` y usará la variable de entorno `$PORT` que Railway proporciona automáticamente.

