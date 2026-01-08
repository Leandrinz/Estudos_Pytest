--- Fixtures --- 

1) O problema que as fixtures resolvem:
    . Imagine que vários testes precisam do mesmo usuário:
        Sem fixture (ruim e repetitivo):
            

            def test_usuario_nome():
                usuario = criar_usuario("Leandro", 20)
                assert usuario["nome"] == "Leandro"
            

            def test_usuario_idade():
                usuario = criar_usuario("Leandro", 20)
                assert usuario["idade"] == 20
            
            Repetição = manutenção ruim

2) Criando a fixture:
    import pytest
    from usuario import criar_usuario

    @pytest.fixture
    def usuario_valido():
        return criar_usuario("Leandro", 20, "leandro@email.com")
    
    Isso cria um objeto reutilizável

3) Usando a fixture no teste:
    O pytest implementa de forma automática a fixture pelo nome:
        
        def test_nome_usuario(usuario_valido):
            assert usuario_valido["nome"] == "Leandro"

4) Fixture != função comum:
    . Você não chama a fixture
    . Você declara ela como parâmetro
    . O pytest faz o resto

    - Errado:
        usuario = usuario_valido()
    - Correto:
        def test_algo(usuario_valido):
            .
            .

5) Fixture com yield (setup + teardown):
    Equivalente ao setUp / tearDown:
        @pytest.fixture
        def recurso():
            print("setup")
            yield "recurso pronto"
            print("teardown")

    Fluxo:

        setup

        teste

        teardown

6) Reutilizando fixtures entre arquiivos:
    Fixtures podem ficar em um arquivo especial:
        tests/
        |-- conftest.py
        |-- test_usuario.py
    
    conftest.py:
        import pytest
        from usuario import criar_usuario

        @pytest.fixture
        def usuario_valido():
            return criar_usuario("Leandro", 20)

    O pytest enxerga automaticamente essa arquivo, não precisa importar nada.

7) Boas práticas com fixtures:
    . Fixture cria contexto
    . Fixture não cria lógica

    - Errado:
        @pytest.fixture
        def usuario():
            assert idade >= 18
    
    - Certo:    
        @pytest.fixture
        def usuario():
            return criar_usuario("Leandro", 20)
