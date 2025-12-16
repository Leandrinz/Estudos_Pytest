from Divisão import divisao

def test_0():
    assert divisao(3,0) == "Não é possível divisir por 0!"


def test_letras():
    assert divisao("Vasco", 9) == "Digite números para a divisão!"


def test_numeros_normais():
    assert divisao(15, 5) == 3

