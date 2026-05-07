def calcular_media(n1, n2, n3):
    media = (n1 + n2 + n3) / 3

    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"