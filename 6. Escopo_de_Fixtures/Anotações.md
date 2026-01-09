--- Escopo de Fixture ---

1) O que é escopo de fixture:
    O escopo define por quanto tempo a fixture "vive"
    Por padrão:
        @pytest.fixture
        def usuario():
            .
            .
            .
    scope="function"
    Ou seja:
        A fixture é criada uma vez por teste


2) scope="function":
    
    @pytest.fixture(scope="function")
    def usuario():
        print("criando usuario")
        return criar_usuario("Leandro", 20)
    
    . Executa antes de cada teste
    . Isolamento total
    . Mais seguro


3) scope="module":

    @pytest.fixture(scope="module")
    def usuario():
        print("criando usuario uma vez por modulo")
        return criar_usuario("Leandro", 20)
    
    . Criando uma vez por arquivo de teste
    . Reutilizada em todos os testes do arquivo
    . Mais rápida, menos isolada


4) scope="session":
    @pytest.fixture(scope="session")
    def usuario():
        print("criando usuario uma vez por sessão")
        return criar_usuario("Leandro", 20)
    
    . Criada uma vez por execução do pytest
    . Compartilhada entre todos os testes
    . Máximo desempenho, isolamento mínimo

5) Regra:
    . Quanto maior o escopo, menor o isolamento
    . Quanto menor o escopo, maior a segurança

6) Utilidade real:
    . Cenário 1 -- Custo (perfomance):
        imagine:
            @pytest.fixture
            def banco():
                print("Conectando ao banco...)
                time.sleep(2)
                return conectar_banco()
        
        Se você tiver:
            . 30 testes
            . Escopo function
            = Você conecta 30 vezes (60 segundos)
        
        Agora com:
            @pytest.fixture(scope"module")
            def banco():
                .
                .
                .
        
            . Conecta 1 vez só (aqui o escopo salva tempo)
    
    = Em resumo, o escopo não muda o que a fixture faz, mas quantas vezes ela faz, e dependendo de como vc faz lhe economiza um tempo danado.