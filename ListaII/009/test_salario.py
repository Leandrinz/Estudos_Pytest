from salario_professor import calculo_salario


def test_0():
    assert calculo_salario(0,0,0) == 0


def test_negativo():
    assert calculo_salario(-2,-3,-4) == "Informe valores válidos"


def test_string():
    assert calculo_salario("ssf", 0, 4) == "Informe números!"


def test_certo():
    assert calculo_salario(1,4,6) == 3.76