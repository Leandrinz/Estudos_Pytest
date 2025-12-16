from restaurante import total_a_pagar


def test_negativo():
    assert total_a_pagar(-1) == "Erro, digite um valor positivo!"


def test_string():
    assert total_a_pagar("str") == "Erro! Digite um número."


def test_normal():
    assert total_a_pagar(3) == 60