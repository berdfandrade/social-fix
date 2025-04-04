from app.security.hashing import hash_password, verify_password


def test_hash_password():
    password = "my_s4f3_p4ssw0rd"
    hashed_password = hash_password(password)

    assert isinstance(hashed_password, str)  # assegura que o hash é uma string
    assert hashed_password != password  # O hash nunca pode ser igual à senha original
    assert hashed_password.startswith("$2b$")  # bcrypt usa esse prefixo


def test_verify_password():
    password = "minha_senha_segura"
    hashed_password = hash_password(password)

    assert verify_password(
        password, hashed_password
    )  # Deve retornar True para a senha correta
    assert not verify_password(
        "senha_errada", hashed_password
    )  # Deve retornar False para senha errada


def test_hash_uniqueness():
    """Testa se o hash gerado é sempre diferente, mesmo para a mesma senha"""
    password = "teste123"
    hash1 = hash_password(password)
    hash2 = hash_password(password)

    assert hash1 != hash2  # bcrypt adiciona salt, então cada hash deve ser diferente
