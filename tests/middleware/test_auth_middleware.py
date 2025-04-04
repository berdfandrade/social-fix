import pytest
from fastapi import FastAPI, HTTPException, status, Request
from fastapi.testclient import TestClient
from datetime import timedelta
from app.middlewares.auth import AuthMiddleWare
from app.services.auth import AuthService

# Configuração do FastAPI com middleware
app = FastAPI()
app.add_middleware(AuthMiddleWare)


# Criando uma rota protegida para testar
@app.get("/protected")
def protected_route(request: Request):
    return {"message": "Access granted", "user": request.state.user}


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def invalid_credentials():
    """Retorna a exceção esperada para tokens inválidos"""
    return HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid or expired token",
        headers={"WWW-Authenticate": "Bearer"},
    )


@pytest.fixture
def valid_token():
    """Gera um token JWT válido para os testes"""
    user_data = {"sub": "1"}  # ID do usuário
    return AuthService.create_access_token(
        data=user_data, expires_delta=timedelta(minutes=5)
    )


def test_decode_invalid_token():
    user = AuthService.decode_token("invalid_token")
    assert user is None


def test_middleware_allows_public_routes(client):
    """Testa se rotas públicas são acessíveis sem autenticação"""
    response = client.get("/docs")  # "/docs" deve ser acessível sem token
    assert response.status_code == 200


def test_middleware_blocks_request_without_token(client):
    """Testa se requisições sem token são bloqueadas"""
    response = client.get("/protected")  # Endpoint protegido sem token
    assert response.status_code == 401
    assert response.json()["detail"] == "Missing or invalid token"


def test_middleware_blocks_invalid_token(client):
    """Testa se um token inválido retorna erro"""
    headers = {"Authorization": "Bearer invalid_token"}
    response = client.get("/protected", headers=headers)
    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid or expired token"


def test_middleware_allows_valid_token(client, valid_token):
    """Testa se um token válido permite acessar a rota"""
    headers = {"Authorization": f"Bearer {valid_token}"}
    response = client.get("/protected", headers=headers)
    print("Token Inválido:", response.status_code, response.json())  # 🔍 Debug
    assert response.status_code == 200
    assert response.json()["message"] == "Access granted"
