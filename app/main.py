import sys
from pathlib import Path
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from starlette.requests import Request
from app.routes.user import router as user_routes
from app.config.fastapi import FASTAPI_CONFIGS
from app.routes.login import router as login_routes
from app.routes.volunteer import router as volunteer_routes
from app.middlewares.auth import AuthMiddleWare

# Cria uma instância do FastAPI
app = FastAPI(**FASTAPI_CONFIGS)

# Rotas de usuário
app.include_router(login_routes)
app.include_router(user_routes)
app.include_router(volunteer_routes)
app.add_middleware(AuthMiddleWare)

# Criação de uma instância do Jinja2Templates
BASE_DIR = Path(__file__).parent  # Pega o diretório atual do main.py
templates = Jinja2Templates(directory=BASE_DIR / "templates")

# Adiciona o diretório raiz do projeto ao PYTHONPATH
ROOT_DIR = Path(__file__).parent.parent
sys.path.append(str(ROOT_DIR))


# Rota da página de login
@app.get("/", response_class=HTMLResponse, tags=["✅ Main"])
async def read_root(request: Request):
    """Página de login"""
    return templates.TemplateResponse({"request": request, "name": "FastAPI"}, "index.html")
