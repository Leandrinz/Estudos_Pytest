--- Quando não usar mock ---

1) Erro clássico -> Mockar tudo:
    Exemplo:
        def test_alguma_coisa():
            with patch("modulo.funcao_a"), \
                 patch("modulo.funcao_b"), \
                 patch("modulo.funcao_c"):
                 . . .
    - Problema:
        . Teste fica frágil
        . Qualquer refatoração quebra o teste
        . Você testa implementação, não comportamento


2) Regra de ouro:
    - Mock apenas o que você NÃO controla

    - Não mockar:
        . Funções puras (cálculo, regra de negócio)
        . Funções do mesmo módulo
        . Código simples e determinístico
    
    - Mockar:
        . Banco de dados
        . API externa
        . Envio de email
        . Sistema de pagamento
        . IO (arquivo, rede)


3) Exemplo ruim:
    def calcular_total(itens):
        return sum(itens)
    
    def test_total():
        with patch("modulo.sum") as mock_sum:
            mock_sum.return_value = 10
            assert calcular_total([1, 2, 3]) == 10
    
    - Você não testou nada útil.


4) Exemplo correto (sem mock):
    def test_total():
        assert calcular_total([1, 2, 3]) == 6
    
    . Simples
    . Robusto


5) Quando mock AUMENTA qualidade:
    
    def enviar_email(email):
        smtp.send(email)
    
    def test_envia_email():
        with patch("email.smtp.send") as mock_send:
            enviar_email("a@b.com")
            mock_send.assert_called_once()
    
    - Aqui:
        . mock evita envio real
        . isola efeito colateral
        . aumenta confiabilidade