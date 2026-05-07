from Sistema import verificar_condicao

def test_menor_de_idade():
    resultado = verificar_condicao(17)
    assert resultado == "Jovem Aprendiz"

def test_clt():
    resultado = verificar_condicao(19)
    assert resultado == "CLT"

def test_aposentado():
    resultado = verificar_condicao(1000)
    assert resultado == "Aposentado"