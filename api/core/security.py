from passlib.context import CryptContext
import jwt
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer
from typing import Optional
from .config import settings

# Configuración de hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
security = HTTPBearer()

def hash_password(password: str) -> str:
    """Hashea una contraseña usando bcrypt"""
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verifica una contraseña contra su hash"""
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """Crea un JWT access token"""
    to_encode = data.copy()
    
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.access_token_expire_minutes)
    
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, 
        settings.secret_key, 
        algorithm=settings.algorithm
    )
    return encoded_jwt

def decode_access_token(token: str) -> Optional[dict]:
    """Decodifica un JWT token y devuelve el payload o None si es inválido"""
    try:
        payload = jwt.decode(
            token, 
            settings.secret_key, 
            algorithms=[settings.algorithm]
        )
        # ✅ Validar que es un dict
        if not isinstance(payload, dict):
            return None
        
        # ✅ Validar que tiene los campos mínimos esperados
        if "sub" not in payload:
            return None
            
        # ✅ Validar que 'sub' no está vacío
        if not payload["sub"]:
            return None
            
        return payload
    except jwt.InvalidTokenError:
        return None
    except Exception:  # Cualquier otro error inesperado
        return None


def get_current_user_id(token = Depends(security)) -> str:
    """Dependency que extrae el ID del usuario del token JWT"""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    # Decodificar el token
    payload = decode_access_token(token.credentials)
    if payload is None:
        raise credentials_exception

    # Extraer el ID del usuario del payload
    user_id: str = payload["sub"]  # Ya validaste que 'sub' existe y no es None
    if not user_id:
        raise credentials_exception
    
    return user_id

def get_current_user_id_optional(token = Depends(security)) -> Optional[str]:
    """Dependency opcional - devuelve user_id si hay token válido, None si no"""
    try:
        return get_current_user_id(token)
    except HTTPException:
        return None