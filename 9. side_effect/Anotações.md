--- side_effect ---

1) O que é side_effect:
    - side_effect permite que um mock:


        . Lançe exceções
        . Retorne valores diferentes
        . Execute uma função
        . Mude de comportamento a cada chamada
        . É como dizer: "Quando essa função falsa for chamada, faça X".

    
2) Por que é necessário:
    - Sem o side_effect o mock:
        . Apenas registra chamadas
        . Sempre retorna None
    
    - Porém, na realidade:
        . Serviços falham
        . Exceções acontecem
        . Retornos variam
    . O side_effect deixa o teste realista


3) Exemplo base com código real:
    - "email_service.py":
        def enviar_email(email):
            print(f"Email enviado para {email}")
    
    - "usuario.py":
        from email_service import enviar email

        def criar_usuario(nome, email):
            enviar_email(email)
            return {"nome": nome, "email": email}


4) side_effect lançando exceção:
    - Testando falha do serviço de email:
        
        from unittesst.mock import patch
        import pytest
        from usuario import criar_usuario

        def test_erro_ao_enviar_email():
            with patch("usuario.enviar_email") as mock_email:
                mock_email.side_effect = RuntimeError("Falha no serviço")

                with pytest.raises(RuntimeError, match="Falha no serviço"):
                    criar_usuario("Leandro", "leandro@email.com")
    . O mock finge que o serviço quebrou.


5) side_effect com múltiplos retornos:

    def test_varios_comportamentos():
        with patch("usuario.enviar_email") as mock_email:
            mock_email.side_effect = [None, RuntimeError("Erro")]

            criar_usuario("Leandro", "a@email.com")

            with pytest.raises(RuntimeError):
                criar_usuario("Leandro", "b@email.com")

    . Cada chamada consome um item da lista


6) side_effect executando uma função:
    
    def fake_email(email):
        if "@" not in email:
            raise ValueError("Email inválido")

    def test_validacao_email():
        with patch("usuario.enviar_email") as mock_email:
            mock_email.side_effect = fake_email

            with pytest.raises(ValueError):
                criar_usuario("Leandro", "email_invalido")


7) Quando usaar side_effect:
    - Usar quando:
        . Quer simular erro
        . Quer simular instabilidade
        . Precisa de retorno variável
        . Precisa testar fluxo de exceção
    
    - Não usar quando:
        . Retorno simples basta
        . Não há variação de comportamento