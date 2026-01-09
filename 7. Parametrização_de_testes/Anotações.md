--- Parametrização de testes --- 

1) O problema clássico:
    Sem parametrização, acabamos assim:
        def test_idade_valida_1():
            assert criar_usuario("A", 18)["idade"] >= 18

        def test_idade_valida_2():
            assert criar_usuario("B", 20)["idade"] >= 18

        def test_idade_valida_3():
            assert criar_usuario("C", 30)["idade"] >= 18

    Funciona, mas:
        . O código fica repetido
        . Difícil de manter
        . Leitura ruim
    

2) A solução = parametrize:

    import pytest

    @pytest.mark.parametrize("idade", [18, 20, 30])
    def test_idades_validas(idade):
        usuario = criar_usuario("Leandro", idade)
        assert usuario["idade"] >= 18
    
    . Em apenas um teste, criamos vários cenários


3) Vários parâmetros:

    @pytest.mark.parametrize(
        "nome,idade",
        [
            ("Leandro", 20),
            ("Maria", 25),
            ("João", 18),
        ]
    )
    def test_usuario_valido(nome, idade):
        usuario = criar_usuario(nome, idade)
        assert usuario["nome"] == nome
        assert usuario["idade"] >= 18


4) Parametrização + exceções:
    Perfeito para validar erros:
        @pytest.mark.parametrize("idade", [-1, -10])
        def test_idade_negativa_dispara_erro(idade):
            with pytest.raises(ValueError):
                criar_usuario("Leandro", idade)


5) Parametrização + mensagem da exceção:
    @pytest.mark.parametrize(
        "idade, mensagem",
        [
            (-1, "idade não pode ser negativa),
            (17, "Usuário deve ser maior de idade"),
        ]
    )
    def test_idades_invalidas(idade, mensagem):
        with pytest.raises(ValueError, match=mensagem):
            criar_usuario("Leandro", idade)