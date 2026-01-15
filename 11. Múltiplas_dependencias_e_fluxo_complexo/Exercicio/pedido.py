from pagamento import cobrar_cartao
from repositorio import salvar_pedido
from notificacao import enviar_notificacao


def finalizar_pedido(cartao, valor, email):
    cobrar_cartao(cartao, valor)
    salvar_pedido(cartao, valor)
    enviar_notificacao(email, "Pedido confirmado")

    return {
        "cartao": cartao,
        "valor": valor,
        "status": "confirmado"
    }
