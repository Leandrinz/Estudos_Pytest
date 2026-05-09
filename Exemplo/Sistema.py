# Verificação de idade pra mercado- 3 etapas - Jovem aprendiz / CLT / Aposentado

def recebe_idade(idade):
    if (idade >= 14 and idade <= 18):
        return "Jovem Aprediz"
    elif (idade > 18 and idade <= 60):
        return "CLT"
    else:
        return "Aposentado"
