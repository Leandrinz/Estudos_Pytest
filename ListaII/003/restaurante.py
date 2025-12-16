def total_a_pagar(kilo = 0):
    try: 
        divida = kilo * 20
        if kilo < 0:
            return "Erro, digite um valor positivo!"
        return divida
    except TypeError:
        return "Erro! Digite um número."

ah = total_a_pagar("teste")
print(ah)