from Antecessor_Sucessor import antecessor_sucessor

def test_0():
    assert antecessor_sucessor(0) == [-1,1]


def test_letra():
    assert antecessor_sucessor("xyz") == "Erro, Digite um número!"


def test_negativo():
    assert antecessor_sucessor(-2) == [-3,-1]