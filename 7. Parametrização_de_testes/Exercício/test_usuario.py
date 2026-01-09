import pytest
from usuario import criar_usuario

@pytest.mark.parametrize("idade", [18, 20, 30])
def test_idades_validas(idade):
    usuarioo = criar_usuario("Leandro", idade)
    assert usuarioo["idade"] >= 18


@pytest.mark.parametrize(
        "idade, mensagem",
        [
            (-1, "Idade não pode ser negativa"),
            (17, "Usuário deve ser maior de idade"),
        ]
)
def test_idades_invalidas(idade, mensagem):
    with pytest.raises(ValueError, match=mensagem):
        criar_usuario("Leandro", idade)

@pytest.mark.parametrize(
    "nome, idade",
    [
        ("Leandro", 20),
        ("Maria", 25),
        ("João", 18),
    ]
)
def test_varios_parametros(nome, idade):
    usuarioo = criar_usuario(nome, idade)
    assert usuarioo["nome"] == nome
    assert usuarioo["idade"] >= 18