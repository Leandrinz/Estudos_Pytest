from pagamento import cobrar_cartao
from notificacao import enviar_notificacao

def finalizar_pedido(numero_cartao, valor, email=None):
    
    cobrar_cartao(numero_cartao, valor)

    if email:
        enviar_notificacao(email, "Pedido confirmado")

    return {
        "cartao": numero_cartao,
        "valor": valor,
        "status": "confirmado"
    }
