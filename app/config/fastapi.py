import os
from dotenv import load_dotenv

load_dotenv()  # Carrega as variáveis do .env

IS_DEV_MODE = os.getenv("DEVELOPMENT") == "1"

if IS_DEV_MODE:
    AppConfig = {
        "title": "Social Fix API",
        "description": "API para criar eventos de caridade e conectar voluntários.",
        "version": "1.0.0",
        "openapi_url": "/openapi.json",
        "docs_url": "/docs",
        "redoc_url": "/redoc"
    }
else:
    AppConfig = {
        "title": "Social Fix API",
        "description": "API para criar eventos de caridade e conectar voluntários.",
        "version": "1.0.0",
        "openapi_url": None,
        "docs_url": None,
        "redoc_url": None
    }
