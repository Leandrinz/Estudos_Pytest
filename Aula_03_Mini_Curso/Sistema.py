def verificar_condicao(idade):
    if (idade < 18):
        return "Jovem Aprendiz"
    elif (idade >= 18 and idade <= 60):
        return "CLT"
    else:
        return "Aposentado"
