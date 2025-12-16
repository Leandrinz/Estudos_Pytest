

def area_circulo(raio = 0, pi = 3):
    try:
        area = pi * (raio * raio)
    except (TypeError):
        return "Digite um número!"
    else:
        if raio == 0:
            return 0
        elif raio < 0:
            return "Erro! Número negativo!"
        else:    
            return area

area = area_circulo(3)
print(f"Área: {area}")