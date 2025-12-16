from dolar import conversao_dolar


def test_0():
    assert conversao_dolar(0) == 0


def test_negativo():
    assert conversao_dolar(-3) == "Digite um valor positivo!"


def test_negativo():
    assert conversao_dolar("suru") == "Erro, digite um número!"


def test_certo():
    assert conversao_dolar(54) == 10