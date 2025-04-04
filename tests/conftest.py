import pytest
from fastapi.testclient import TestClient
from testcontainers.postgres import PostgresContainer
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.user import Base
from sqlalchemy.orm import Session
from app.main import app

@pytest.fixture(scope="session")
def postgres_container():
    """Cria um contêiner PostgreSQL para testes."""
    with PostgresContainer("postgres:latest") as postgres:
        yield postgres


@pytest.fixture(scope="function")
def db(postgres_container):
    """Cria uma conexão temporária com o banco PostgreSQL de testes."""
    engine = create_engine(postgres_container.get_connection_url())
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    # Criar as tabelas no banco de testes
    Base.metadata.create_all(bind=engine)
    session = TestingSessionLocal()

    yield session  # Retorna a sessão para o teste

    session.close()
    Base.metadata.drop_all(bind=engine)  # Remove as tabelas após o teste
