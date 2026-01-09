from usuario import criar_usuario
import pytest

@pytest.fixture(scope="function")
def usuario_valido():
    return criar_usuario("Leandro Savio", 20, "Leandro@gmail.com")

# 1. O Usuário deve ser criado corretamente
def test_usuario_criado_corretamente(usuario_valido): 
    assert usuario_valido["nome"] == "Leandro Savio"
    assert usuario_valido["idade"] == 20
    assert usuario_valido["email"] == "Leandro@gmail.com"

# 2. O nome do usuário deve conter pelo menos o primeiro nome

def test_contem_primeiro_nome(usuario_valido):
    assert "Leandro" in usuario_valido["nome"]

# 3. A idade deve ser >= 18
def test_idade_maior_que_18(usuario_valido):

    assert usuario_valido["idade"] >= 18

# 4. o email pode ser None
def test_email_igual_none(): 
    usuarioo = criar_usuario(
        nome = "Leandro",
        idade = 20,
    ) 

    assert usuarioo["email"] is None

# 5. O usuario não deve ter idade negativa 
def test_idade_nao_eh_negativa(usuario_valido): 

    assert usuario_valido["idade"] >= 0