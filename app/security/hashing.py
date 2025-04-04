import bcrypt

def hash_password(password : str) -> str:
    """Gera um hash seguro para a senha"""
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password.decode()

def verify_password(password : str, hashed_password : str) -> bool:
    """Verifica se a senha corresponde ao hash armazenado."""
    return bcrypt.checkpw(password.encode(), hashed_password.encode())