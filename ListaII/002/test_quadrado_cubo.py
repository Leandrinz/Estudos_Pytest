from quadrado_cubo import calculo_quadrado_cubo

def test_string_em_numero():
    assert calculo_quadrado_cubo("29", 20) == "Burro, Burro e Burro!"


def test_0():
    assert calculo_quadrado_cubo(0,0) == [0,0]


def test_normal():
    assert calculo_quadrado_cubo(2,3) == [4,27]