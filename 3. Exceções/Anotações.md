--- Testando exceções com Pytest ---

1) O problema que iremos resolver:
    
    Até agora a função aceita qualquer idade:
        criar_usuario("Leandro", -10)

    Isso não faz sentido, mas o código aceita.

    Portanto, iremos corrigir isso com o uso de exceções


2) Atualizamos o código do arquivo "usuario.py" (verifique as mudanças realizadas e compare com a da aula de "Asserts")


3) Testando exceção com pytest:
    
    def test_idade_negativa_dispara_erro():
        with pytest.raises(ValueError):
            criar_usuario("Leandro", -1)

    Se não lançar ValueError, o teste falha
    Se lançar, o teste passa


4) Testando a mensagem da exceção:

    def test_idade_negativa_mensagem():
        with pytest.raises(ValueError, match="Idade não pode ser negativa):
            criar_usuario("Leandro", -5)


5) Testando menor de idade:

    def test_usuario_menor_de_idade():
        with pytest.raises(ValueError, match="Usuário deve ser maior de idade):
            criar_usuario("Leandro", 17)


6) Teste Positivo:

    def test_usuario_valido_nao_dispara_excecao():
        usuario = criar_usuario("Leandro", 19)
        assert usuario["idade"] == 19