def enviar_notificacao(email, mensagem):
    if "@" not in email:
        raise ValueError("Email inválido")

    return f"Notificação enviada para {email}"
