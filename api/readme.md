# ERP System - Backend API

Backend del sistema ERP construido con FastAPI.

## 🚀 Instalación

### Prerrequisitos
- Python 3.8+
- pip

### Instalación local
```bash
# Desde la raíz del proyecto ERP
cd api

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# o
venv\Scripts\activate     # Windows

# Instalar dependencias
pip install -r requirements.txt
```

## ⚙️ Configuración

### Variables de entorno
Las variables se configuran en `.env` en la raíz del proyecto:

```bash
# Desde ERP/
cp .env.sample .env
```

**Variables principales:**
- `SECRET_KEY`: Clave JWT (generar con `openssl rand -hex 32`)
- `DATABASE_URL`: Conexión a base de datos
- `DEBUG`: Modo desarrollo
- `ALLOWED_ORIGINS`: Dominios permitidos para CORS

### Estructura de archivos de configuración
```
ERP/
├── .env           # ✅ Variables de entorno AQUÍ
├── .env.sample    # ✅ Plantilla para .env
└── api/
    └── core/
        └── config.py  # Lee ../.env automáticamente
```

## 🏃‍♂️ Ejecución

### Desarrollo (recomendado)
```bash
# Desde ERP/ (raíz del proyecto)
fastapi dev api/main.py

# O desde api/
cd api
fastapi dev main.py
```
### Desarrollo alternativo (uvicorn directo)
```bash
cd api
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Producción
```bash
cd api
fastapi run main.py --host 0.0.0.0 --port 8000

# O con uvicorn
uvicorn main:app --host 0.0.0.0 --port 8000
```

## 📁 Estructura de la API

```
api/
├── main.py                 # Punto de entrada
├── core/                   # Funcionalidades base
│   ├── config.py          # Configuración global
│   ├── security.py        # Autenticación JWT
│   ├── database.py        # Conexión BD
│   └── dependencies.py    # Dependencias compartidas
├── modules/                # Módulos del negocio
│   └── users/             # Módulo usuarios
│       ├── router.py      # Endpoints
│       ├── models.py      # Modelos de BD
│       ├── schemas.py     # Validación Pydantic
│       └── service.py     # Lógica de negocio
├── shared/                 # Utilidades compartidas
│   ├── utils.py
│   └── constants.py
└── tests/                  # Pruebas
```

## 🔗 Endpoints

### Autenticación
- `POST /api/users/login` - Login de usuario
- `GET /api/users/me` - Información usuario actual

### Usuarios
- `GET /api/users/` - Listar usuarios
- `POST /api/users/` - Crear usuario
- `PUT /api/users/{id}` - Actualizar usuario

### Sistema
- `GET /` - Estado de la API
- `GET /health` - Health check
- `GET /docs` - Documentación Swagger

## 🧪 Testing

```bash
# Ejecutar tests
pytest

# Con coverage
pytest --cov=.

# Tests específicos
pytest tests/test_users.py
```

## 🗄️ Base de Datos

### SQLite (Desarrollo)
Por defecto usa SQLite. El archivo se crea automáticamente.

### PostgreSQL (Producción)
```bash
DATABASE_URL=postgresql://username:password@localhost:5432/erp_db
```

### Migraciones
```bash
# Generar migración
alembic revision --autogenerate -m "descripción"

# Aplicar migraciones
alembic upgrade head
```

## 🔒 Autenticación

La API usa **JWT Bearer tokens**:

```bash
# Login
curl -X POST "http://localhost:8000/api/users/login" \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com", "password": "password"}'

# Usar token
curl -H "Authorization: Bearer <token>" \
  "http://localhost:8000/api/users/me"
```

## 🐛 Debug

### Logs
Los logs se muestran en consola en modo desarrollo.

### Swagger UI
Documentación interactiva disponible en:
- http://localhost:8000/docs (Swagger)
- http://localhost:8000/redoc (ReDoc)

## 📦 Dependencias principales

- **fastapi**: Framework web
- **uvicorn**: Servidor ASGI
- **pydantic**: Validación de datos
- **python-jose**: JWT tokens
- **passlib**: Hashing de passwords
- **sqlalchemy**: ORM (próximamente)

## 🔄 Desarrollo

### Agregar nuevo módulo
1. Crear carpeta en `modules/nombre_modulo/`
2. Implementar router, models, schemas, service
3. Registrar router en `main.py`

### Estructura de módulo
```python
# modules/mi_modulo/router.py
from fastapi import APIRouter
router = APIRouter()

@router.get("/")
def get_items():
    return []
```

```python
# main.py
from modules.mi_modulo.router import router as mi_modulo_router
app.include_router(mi_modulo_router, prefix="/api/mi-modulo", tags=["Mi Módulo"])
```

## 🔄 Comandos útiles

```bash
# Desarrollo con auto-reload
fastapi dev api/main.py

# Producción
fastapi run api/main.py

# Especificar host y puerto
fastapi dev api/main.py --host 0.0.0.0 --port 3000

# Desde carpeta api/
cd api && fastapi dev main.py
```