from servico import cobrar_cartao

def finalizar_pedido(numero_cartao, valor):
    if valor <= 0:
        raise ValueError("Valor inválido")
    
    cobrar_cartao(numero_cartao, valor)

    return{
        "status": "pago",
        "valor": valor
    }