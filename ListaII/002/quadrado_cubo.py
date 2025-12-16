def calculo_quadrado_cubo(numero_quadrado = 0, numero_cubo = 0):
    try:
        quadrado = numero_quadrado * numero_quadrado 
        cubo = numero_cubo ** 3
        vetor = [quadrado, cubo]
    except TypeError:
        return "Burro, Burro e Burro!"
    else:
        return vetor



ah = calculo_quadrado_cubo(19, 20)
print(ah)