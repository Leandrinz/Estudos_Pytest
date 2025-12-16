from quadrado import quadrado

def test_quadrado_positivo():
    assert quadrado(5) == 25


def test_quadrado_negativo():
    assert quadrado(-5) == 25


def test_quadrado_zero():
    assert quadrado(0) == 0