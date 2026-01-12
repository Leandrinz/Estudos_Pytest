from notificacao import enviar_notificacao

def processar_pagamento(email, valor):
    if valor <= 0:
        raise ValueError("Valor inválido")
    
    enviar_notificacao(email, "Pagamento realizado com sucesso")

    return {
        "email": email,
        "valor": valor,
        "status": "confirmado"
    }