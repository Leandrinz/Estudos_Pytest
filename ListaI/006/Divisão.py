def divisao(numero = 0, denominador = 0):
    try:
        Resultado = numero / denominador
    except TypeError:
        return "Digite números para a divisão!"
    except ZeroDivisionError:
        return "Não é possível divisir por 0!"
    else:
        return Resultado



divisao(0)