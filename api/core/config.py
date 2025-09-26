from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    # App básica
    app_name: str = "ERP System"
    version: str = "1.0.0"
    debug: bool = False
    
    # Base de datos
    database_url: str = "sqlite:///./erp.db"
    
    # Seguridad
    secret_key: str = "your-secret-key"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    
    # CORS
    allowed_origins: List[str] = ["http://localhost:3000"]
    
    class Config:
        # Leer .env desde la raíz del proyecto (carpeta padre)
        env_file = "../.env"
        env_file_encoding = 'utf-8'
        case_sensitive = False
        env_list_separator = ","

settings = Settings()