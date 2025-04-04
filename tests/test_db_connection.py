import os
import pytest
from tests.tools.wrapper import it, TestName
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from dotenv import load_dotenv

# Carregar as variáveis do ambiente do arquivo .env
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# Criar o engine de conexão
engine = create_engine(DATABASE_URL)

# Criar uma sessão
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture
def db_session():
    # Cria uma sessão para testar a conexão
    session = SessionLocal()
    yield session
    session.close()
    
@it("🔗 Should return the connection with DB")
def test_connection(db_session):
    try:
        # Tenta realizar uma consulta simples para testar a conexão
        result = db_session.execute(text("SELECT 1"))
        assert result.fetchone() is not None, "Falha na consulta de teste."
        print("Conexão com o banco de dados bem-sucedida!")
    except SQLAlchemyError as e:
        pytest.fail(f"Erro ao conectar ao banco de dados: {e}")


