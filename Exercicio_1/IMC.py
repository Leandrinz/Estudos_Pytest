# Com base nesse Sistema, crie um arquivo de Teste com 4 casos de testes que cubra cada um dos casos.

def faixa_imc(imc):
    if (imc < 18.5):
        return "Abaixo do Peso"
    elif (imc >= 18.5 and imc <= 24.9):
        return "Peso Normal"
    elif (imc >= 25.0 and imc <= 29.9):
        return "Sobrepeso"
    else:
        return "Obesidade"