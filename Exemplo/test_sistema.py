from Sistema import recebe_idade
# 3 testes

def test_Jovem_aprendiz():
    resultado = recebe_idade(15)
    assert resultado == "Jovem Aprediz"

def test_CLT():
    resultado = recebe_idade(50)
    assert resultado == "CLT"

def test_aposentado():
    resultado = recebe_idade(61)
    assert resultado == "Aposentado"