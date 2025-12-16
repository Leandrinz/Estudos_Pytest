def calculo_salario(valor_hora = 0, horas_trabalhadas = 0, desconto_inss = 0):
    try:
        Salario_bruto = horas_trabalhadas * valor_hora
        total_desconto = (desconto_inss / 100) * Salario_bruto
        salario_liquido = Salario_bruto - total_desconto
    except TypeError:
        return "Informe números!"
    if (valor_hora < 0 or horas_trabalhadas < 0 or desconto_inss < 0):
        return "Informe valores válidos"
    else:
        return salario_liquido


ah = calculo_salario(-2, -3, -4)
print(ah)