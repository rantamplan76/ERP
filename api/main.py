from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.config import settings

app = FastAPI(
    title=settings.app_name,
    version=settings.version,
    debug=settings.debug,
    description="Sistema ERP organizado y escalable"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
