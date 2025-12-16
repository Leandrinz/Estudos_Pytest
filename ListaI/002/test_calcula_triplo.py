from calcula_triplo import triplo


def test_triplo_positivo():
    assert triplo(3) == 9


def test_triplo_negativo():
    assert triplo(-5) == -15


def test_triplo_zero():
    assert triplo(0) == 0