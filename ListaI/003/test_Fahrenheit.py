from Fahrenheit import ffahrenheit


def test_ebulicao():
    assert ffahrenheit(100) == 212


def test_Congelamento():
    assert ffahrenheit(0) == 32


def test_Corporal():

    resultado = ffahrenheit(37)
    
    assert round(resultado, 2) == 98.6




