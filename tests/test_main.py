from fastapi.testclient import TestClient
from app.main import app

# Criando o cliente de testes
client = TestClient(app)


def test_login_page_load():
    # Fazendo uma requisição GET para a rota "/"
    response = client.get("/")

    # Verificando se o status code da resposta é 200 (OK)
    assert response.status_code == 200

    # Verificando se o Content-Type da resposta é 'text/html'
    assert response.headers["Content-Type"].startswith("text/html")

    # Verificando se o título da página está correto
    assert "<title>Página de Login</title>" in response.text

    # Verificando se o texto esperado aparece na página (exemplo: título do formulário)
    assert '<h2 class="login-header">Social Fix</h2>' in response.text

    # Verificando se os campos de input estão presentes
    assert (
        '<input type="text" class="form-control" id="username" name="username" required>'
        in response.text
    )
    assert (
        '<input type="password" class="form-control" id="password" name="password" required>'
        in response.text
    )

    # Verificando se o botão de login está presente
    assert (
        '<button type="submit" class="btn btn-primary">Entrar</button>' in response.text
    )
