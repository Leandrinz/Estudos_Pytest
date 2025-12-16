from nome_idade import nnome_idade


def test_nome_errado():
    assert nnome_idade(19, 19) == "Erro! Digite uma string em nome!"


def test_idade_errada():
    assert nnome_idade("19", "Leandro") == "Erro! Digite um número em idade!"


def test_tudo_certo():
    assert nnome_idade(19, "Leandro") == "Olá, Leandro! Você tem 19 anos."