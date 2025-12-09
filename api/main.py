from fastapi import FastAPI, Depends
from core.security import get_current_user_id
from fastapi.middleware.cors import CORSMiddleware
import logging
from core.config import settings
from core.logging import setup_logging

setup_logging()
# ✅ Logger para main
logger = logging.getLogger(__name__)


app = FastAPI(
    title=settings.app_name,
    version=settings.version,
    debug=settings.debug,
    description="Sistema ERP organizado y escalable"
)

# ✅ Log importante: inicio de aplicación
logger.info("Iniciando aplicación %s v%s", settings.app_name, settings.version)


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Log de configuración crítica
logger.info("CORS configurado - permitiendo todos los orígenes")


@app.get("/")
def read_root():
    return {
        "message": "ERP System API",
        "version": settings.version,
        "status": "running"
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}
