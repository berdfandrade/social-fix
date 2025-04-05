import pytest
from fastapi import FastAPI, HTTPException, status, Request
from tests.tools.wrapper import it, TestName
from fastapi.testclient import TestClient
from datetime import timedelta
from app.middlewares.auth import AuthMiddleWare
from app.services.auth import AuthService
import json


@TestName("🔐 AuthMiddleware")
class TestAuthMiddleware:
    def setup_class(self):

        self.app = FastAPI()
        self.app.add_middleware(AuthMiddleWare)

        @self.app.get("/protected")
        def protected_route(request: Request):
            return {"message": "Access granted", "user": request.state.user}

        self.client = TestClient(self.app)

    def get_valid_token(self):

        user_data = {"sub": "1"}
        return AuthService.create_access_token(
            data=user_data, expires_delta=timedelta(minutes=5)
        )

    @it("Should try to decode an invalid token")
    def test_decode_invalid_token(self):
        user = AuthService.decode_token("invalid_token")
        assert user is None

    @it("Public routes should be access without auth")
    def test_middleware_allows_public_routes(self):
        """Rotas públicas devem ser acessíveis sem autenticação"""
        response = self.client.get("/docs")
        assert response.status_code == 200

    @it("Should block request without token")
    def test_middleware_blocks_request_without_token(self):
        """"""
        response = self.client.get("/protected")
        assert response.status_code == 401
        assert response.json()["detail"] == "Missing or invalid token"

    @it("Should return 401 for a invalid token")
    def test_middleware_blocks_invalid_token(self):
        """Token inválido deve retornar erro 401"""
        headers = {"Authorization": "Bearer invalid_token"}
        response = self.client.get("/protected", headers=headers)
        assert response.status_code == 401
        assert response.json()["detail"] == "Invalid or expired token"

    @it("Should allows route with valid token")
    def test_middleware_allows_valid_token(self):
        """Token válido deve permitir acesso"""
        token = self.get_valid_token()
        headers = {"Authorization": f"Bearer {token}"}
        response = self.client.get("/protected", headers=headers)
        assert response.status_code == 200
        assert response.json()["message"] == "Access granted"
