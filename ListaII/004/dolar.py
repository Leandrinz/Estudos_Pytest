def conversao_dolar(reais = 0):
    try:
        dolar = reais / 5.40
    except TypeError: 
        return "Erro, digite um número!"
    except (dolar < 0):
        return "Digite um valor positivo!"
    else: 
        return dolar


ah = conversao_dolar(45)
print(f"{ah}")