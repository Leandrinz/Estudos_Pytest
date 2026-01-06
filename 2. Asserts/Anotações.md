--- Asserts e mensagens de erro inteligentes ---
1) O assert do pytest:
    No pytest, você usa o assert normal do python:
        def test_soma():
            assert 2 + 3 == 5
    
    Porém, o pytest intercepta esse assert e analisa a expressão. Por isso ele mostra os erros de forma detalhada.


2) Comparações mais comuns:
    - Igualdade 
        def test_igualdade():
            assert 10 == 10
    
    - Diferente
        def test_diferente():
            assert 10 != 3
    
    - Maior / Menor
        def test_maior_menor():
            assert 10 > 5
            assert 3 < 7


3) Testando coleções (in) - Bastante usado em testes reais:
    # Exemplo 1:
    def test_item_em_lista():
        lista = [1, 2, 3]
        assert 2 in lista
    
    # Exemplo 2:
    def test_chave_em_dict():
        usuario = {"nome": "Leandro", "idade": 20}  
        assert "nome" in usuario


4) is, is not e None:
    # Exemplo 1:
    def test_none():
        resultado = None
        assert resultado is None
    
    # Exemplo 2:
    def test_not_none():
        valor = 10
        assert valor is not None


5) Mensagens de erro:
    Observe este teste quebrado de propósito:
        def test_erro_exemplo():
            assert 10 == 5
    
    O pytest irá nos mostrar algo como:
        >       assert 10 == 5
        E       assert 10 == 5
        E       + where 10 == 10
        E       + and 5 == 5
    
    Comparado ao PyUnit, isso nos dá maior controle do que de fato aconteceu de errado no nosso teste.


6) Comparação de strings (diff automático)
    def test_string():
        assert "pytest é ótimo" == "pytest é otimo"
    
    O pytest irá nos mostrar onde a string difere, letra por letra


7) Assert com mensagem personalizada:
    Tomemos este exemplo:
        def test_com_mensagem():
            assert 2 + 2 == 5, "Soma incorreta"
    
    Boa prática:
        - Use quando a regra de negócio não é óbvia
        - Em geral, confie na mensagem do pytest

8) Regra de ouro nos asserts:
    Um comportamento por teste!!!

    Ruim:
        def test_ruim():
            assert soma(2, 3) == 5
            assert soma(5, 5) == 10
            assert soma(0, 0) == 0
    
    Melhor (vamos melhorar ainda mais futuramente com o conceito de parametrização em uma aula futura):
        def test_soma_basica():
            assert soma(2, 3) == 5