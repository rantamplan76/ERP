import logging
import sys
from .config import settings

def setup_logging():
    """Configura el logging para toda la aplicación"""
    # Formato de logs
    log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    date_format = "%Y-%m-%d %H:%M:%S"

    # Nivel según configuración
    log_level = logging.DEBUG if settings.debug else logging.INFO

    # ✅ FORZAR reset completo del logging
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    
    # Configuración básica
    logging.basicConfig(
        level=log_level,
        format=log_format,
        datefmt=date_format,
        handlers=[
            logging.StreamHandler(sys.stdout),  # Consola
            # logging.FileHandler('logs/app.log')  # Archivo (opcional)
        ],
        force=True  # Forzar la configuración (sobrescribe configuraciones previas)
    )
    
    # ✅ Configurar loggers específicos MÁS AGRESIVAMENTE
    loggers_to_silence = [
        "fastapi",
        "uvicorn", 
        "uvicorn.access",
        "uvicorn.error",
        "sqlalchemy.engine",
        "sqlalchemy.pool",
    ]
    
    for logger_name in loggers_to_silence:
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.WARNING)
        logger.propagate = True  # Asegurar que usa la configuración padre
    
    # Tu aplicación en debug si está activado
    logging.getLogger("core").setLevel(log_level)
    #logging.getLogger("services").setLevel(log_level)
    #logging.getLogger("routers").setLevel(log_level)
    
    
    logging.info("Logging configurado correctamente")
