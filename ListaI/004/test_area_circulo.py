from Area_circulo import area_circulo

def test_area_0():
    assert area_circulo(0) == 0


def test_negativo():
    assert area_circulo(-3) == "Erro! Número negativo!"


def test_letras():
    assert area_circulo("xyz") == "Digite um número!"