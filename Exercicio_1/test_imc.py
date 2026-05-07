from IMC import faixa_imc

def test_abaixo_do_peso():
    resultado = faixa_imc(15.0)
    assert resultado == "Abaixo do Peso"

def test_peso_normal():
    resultado = faixa_imc(18.6)
    assert resultado == "eso Normal"

def test_sobrepeso():
    resultado = faixa_imc(29.9)
    assert resultado == "Sobrepeso"

def test_obesidade():
    resultado = faixa_imc(50.0)
    assert resultado == "Obesidade"