--- TESTES DE INTEGRAÇÃO COM PYTEST ---

1) O que é um teste de integração:
    - É um teste que:
        . Não usa mock
        . Executa múltiplas partes reais
        . Valida o comportamento do sistema como um todo
    
    - Diferente do teste unitário:
        . Unitário = Função isolada
        . Integração = Fluxo completo


2) Quando usar teste de integração:
    - Use quando você quer garantir que:
        . Módulos conversam corretamente
        . Dados fluem como esperado
        . Nada quebra na cola entre partes
    
    - Exemplos clássicos:
        . Salvar no banco
        . API chamando serviço
        . Fluxo de pedido completo


3) Exemplo simples de fluxo real:

    # pagamento.py
    def cobrar_cartao(cartao, valor):
        if valor <= 0:
            raise ValueError("Valor inválido")
    
    # repositorio.py
    def salvar_pedido(cartao, valor):
        return {"cartao": cartao, "valor": valor}
    
    # pedido.py
    from pagamento import cobrar_cartao
    from repositorio import salvar_pedido

    def finalizar_pedido(cartao, valor):
        cobrar_cartao(cartao, valor)
        return salvar_pedido(cartao, valor)


4) Teste de integração (sem mock):
    def test_fluxo_real_completo():
        resultado = finalizar_pedido(1234, 100)

        assert resultado["cartao"] == 1234
        assert resultado["valor"] == 100

    . Simples
    . Confiável
    . Sem patch