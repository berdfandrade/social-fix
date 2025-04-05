from tests.tools.wrapper import it, TestName
from app.security.hashing import hash_password, verify_password


@TestName("🔑 Hash password")
class TestHashPassword:

    @it("Should return a hashed password")
    def test_hash_password(self):

        password = "my_s4f3_p4ssw0rd"
        hashed_password = hash_password(password)

        assert isinstance(hashed_password, str)
        assert hashed_password != password
        assert hashed_password.startswith("$2b$")

    @it("Should be a valid hash")
    def test_verify_password(self):

        password = "minha_senha_segura"
        hashed_password = hash_password(password)

        assert verify_password(password, hashed_password)
        assert not verify_password("senha_errada", hashed_password)

    @it("Should return a unique hash")
    def test_hash_uniqueness(self):

        password = "teste123"
        hash1 = hash_password(password)
        hash2 = hash_password(password)

        assert hash1 != hash2
