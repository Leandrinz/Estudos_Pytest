--- Múltiplas dependências e fluxo complexo ---

1) O problema (contexto):
    - Vamos um cenário em que:
        . Cobra o cartão
        . Salva o pedido no banco
        . Envia a notificação
        . Retorna o resultado final


2) Código base:

    from pagamento import cobrar_cartao
    from notificacao import enviar_notificacao
    from repositorio import salvar_pedido


    def finalizar_pedido(cartao, valor, email):
        cobrar_cartao(cartao, valor)
        salvar_pedido(cartao, valor)

        enviar_notificacao(email, "Pedido confirmado")

        return {
            "cartao": cartao,
            "valor": valor,
            "status": "confirmado"
        }
    

3) O que mockar (e o que não se deve mockar):
    - Deve ser mocado:
        . cobrar_cartao -> Serviço externo
        . salvar_pedido -> Banco de dados
        . enviar_notificacao -> email/ serviço externo
    
    - Não deve ser mockado:
        . finalizar_pedido (função testada)
        . lógica interna simples
        . retorno final


4) Teste correto com múltiplos mocks:
    
    import pytest
    from unittest.mock import patch
    from pedido import finalizar_pedido

    def test_fluxo_complexo_com_sucesso():
        with patch("pedido.cobrar_cartao") as mock_cobrar, \
             patch("pedido.salvar_pedido") as mock_salvar, \
             patch("pedido.enviar_notificacao") as mock_notificar:
            
            resultado = finalizar_pedido(
                cartao=1234,
                valor=100,
                email="test@email.com"
            )

            mock_cobrar.assert_called_once_with(1234, 100)
            mock_notificar.assert_called_once_with(
                "teste_email.com",
                "Pedido confirmado"
            )

            assert resultado["status"] == "confirmado"


5) Testando falha no meio do fluxo:
    def test_falha_na_cobranca_nao_salva_nem_notifica():
        with patch("pedido.cobrar_cartao") as mock_cobrar, \
            patch("pedido.salvar_pedido") as mock_salvar, \
            patch("pedido.enviar_notificacao") as mock_notificar:

            mock_cobrar.side_effect = RuntimeError("Falha na cobrança")

            with pytest.raises(RuntimeError):
                finalizar_pedido(1234, 100, "teste@email.com")

            mock_salvar.assert_not_called()
            mock_notificar.assert_not_called()
