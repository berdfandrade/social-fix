import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, Session, declarative_base
from sqlalchemy.exc import SQLAlchemyError

# Carregar as variáveis do ambiente do arquivo .env
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# Criar o engine de conexão
engine = create_engine(DATABASE_URL, pool_pre_ping=True)

# Criar uma fábrica de sessões
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def Connection():
    """Fornece uma sessão de banco de dados para ser usada via Depends()."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def test_connection():
    """Testa a conexão com o banco de dados."""
    try:
        with SessionLocal() as session:
            session.execute(text("SELECT 1"))
        print("✅ Conexão com o banco de dados bem-sucedida!")
    except SQLAlchemyError as e:
        print("❌ Erro ao conectar ao banco de dados:", e)


# Executa o teste de conexão apenas quando o script é rodado diretamente
if __name__ == "__main__":
    test_connection()
