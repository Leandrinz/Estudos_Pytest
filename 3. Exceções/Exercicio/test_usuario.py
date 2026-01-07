import pytest
import usuario

def test_idade_negativa():
    with pytest.raises(ValueError, match="Idade não pode ser negativa"):
        usuario.criar_usuario("Leandro", -12)

def test_menor_de_idade():
    with pytest.raises(ValueError, match="Usuário deve ser maior de idade"):
        usuario.criar_usuario("Leandro", 17)

def test_tudo_certo():
    usuarioo = usuario.criar_usuario("Leandro", 19)
    assert usuarioo["idade"] == 19