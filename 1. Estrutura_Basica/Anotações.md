--- Estrutura básica de pytest ---
1) Teste Simples
    No pytest, não precisa de classe nem de self, só funções que começam com test_:
        # arquivo: test_exemplo.py

        def test_soma():
            assert 2 + 3 == 5

2) Rodando os testes
    No terminal:
        pytest
    Para mais detalhes:
        pytest -v

Dica: pytest já dá mensagens claras quando um teste falha, mostrando os valores esperados e os que foram exibidos, diferente do PyUnit que só dizia "AssertionError"