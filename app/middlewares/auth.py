from fastapi import Request, HTTPException, status
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse
from app.services.auth import AuthService


class AuthMiddleWare(BaseHTTPMiddleware):
    """Middleware para autenticação global via JWT"""

    async def dispatch(self, request: Request, call_next):
        # Verifica se a rota requer autenticação (pule rotas públicas como login)
        # Devemos pular as rotas públicas
        print(f"Interceptando requisição para: {request.url.path}")
        if request.url.path in ["/token", "/docs", "/openapi.json", "/"]:
            return await call_next(request)

        # Obtém o token do cabeçalho Authorization
        auth_header = request.headers.get("Authorization")
        print("Cabeçalho Authorization:", auth_header)  # 🔍 Debug
        if not auth_header or not auth_header.startswith("Bearer "):
            return JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content={"detail": "Missing or invalid token"},
                headers={"WWW-Authenticate": "Bearer"},
            )

        # Extrai o token JWT
        token = auth_header.split(" ")[1]

        # Decodifica o token
        user = AuthService.decode_token(token)

        if not user:
            return JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content={"detail": "Invalid or expired token"},
                headers={"WWW-Authenticate": "Bearer"},
            )

        # Adiciona o usuário À requisição para uso nos endpoints
        request.state.user = user

        return await call_next(request)
