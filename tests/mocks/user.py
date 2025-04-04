from app.schemas.user import UserCreate
import random
import uuid
from datetime import datetime

USER = UserCreate(
    username=f"user{random.randint(1000, 9999)}",
    email=f"test{random.randint(1000, 9999)}@email.com",
    full_name="Usuário de Teste",
    password="SecurePassword123!",
    phone="(31) 99999-9999",
    birth_date=datetime(1995, 5, 20),
    gender="Masculino",
    country="Brasil",
    state="Minas Gerais",
    city="Belo Horizonte",
    zip_code="30130-000",
    bio="Apaixonado por tecnologia e voluntariado.",
    skills="Programação, Design, Comunicação",
    interests="Educação, Meio Ambiente, Saúde",
    is_volunteer=True,
    is_organizer=False,
    profile_picture=f"https://api.dicebear.com/7.x/identicon/svg?seed={uuid.uuid4()}",
)
