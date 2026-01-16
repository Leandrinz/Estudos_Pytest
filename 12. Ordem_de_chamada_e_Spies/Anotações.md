--- Ordem de chamadas e spies ---

1) Regra:
    . Só testamos a ordem quando a ordem é regra de negócio

    - Errado testar quando:
        . É detalhe de implementação
        . Pode mudar sem quebrar comportamento
    
    - Certo testar ordem quando:
        . Uma coisa não pode acontecer antes da outra
        . Existe risco real (ex: Cobrar antes de validar, salvar antes de cobrar)


2) Como verificar ordem de chamadas:
    - Método -> mock_calls

    - Exemplo simples:

        from unittest.mock import patch, call
        from pedido import finalizar_pedido

        def test_ordem_das_chamadas():
            with patch("pedido.cobrar_cartao") as mock_cobrar, \
                patch("pedido.salvar_pedido") as mock_salvar, \
                patch("pedido.enviar_notificacao") as mock_notificacao:

                finalizar_pedido(1234, 100, "email@email.com")

                assert mock_cobrar.mock_calls == [call(1234, 100)]
    
    . Porém isso não resolve tudo, por que cada mock tem seu próprio histórico


3) Testando ordem ENTRE funções diferentes:
    - mockar tudo no MESMO namespace:

        def test_ordem_completa_do_fluxo():
            with patch("pedido.cobrar_cartao") as cobrar, \
                patch("pedido.salvar_pedido") as salvar, \
                patch("pedido.enviar_notificacao") as notificar:

                finalizar_pedido(1, 2, "a@a.com")

                chamadas = (
                    cobrar.mock_calls +
                    salvar.mock_calls +
                    notificar.mock_calls
                )

                assert chamadas == [
                    call(1, 2),
                    call(1, 2),
                    call("a@a.com", "Pedido confirmado")
                ]

    . Isso só deve ser usado quando a ordem importa de verdade


4) Alternativa mais elegante (spy):
    - Em vez de mockar tudo, você pode observar chamadas reais:

        with patch("pedido.cobrar_cartao", wraps=cobrar_cartao) as spy:
            finalizar_pedido(1234, 100, "a@a.com")
            spy.assert_called_once()


5) Forma definitiva:
    - attach_mock:

        from unittest.mock import Mock, call, patch
        from pedido import finalizar_pedido

        def test_cobrar_antes_de_salvar_pedido():
            tracker = Mock()

            with patch("pedido.cobrar_cartao") as mock_cobrar, \
                patch("pedido.salvar_pedido") as mock_salvar:

                tracker.attach_mock(mock_cobrar, "cobrar")
                tracker.attach_mock(mock_salvar, "salvar")

                finalizar_pedido(2, 4, "leandrin@email.com")

                assert tracker.mock_calls == [
                    call.cobrar(2, 4),
                    call.salvar(2, 4)
                ]
