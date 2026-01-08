--- Organização de arquivos e discover no pytest ---

1) Como o pytest encontra seus testes (discover):
    - O pytest descobre seus testes de forma automatica com base nessas regras:
        . Arquivos:
            . test_*.py
            . *_test.py
        . Funções:
            . def test_alguma_coisa()
        . Classes (opcional):
            . class TestAlgo:
            . Métodos também começam com test_
            . Não herda de nada

2) Estrutura de projeto recomendada:
    projeto/
    |
    |-- usuario.py
    |-- emprestimo.py
    |
    |_tests/
      |--__init__.py (opcional)
      |-- test_usuario.py
      |-- test_emprestimo.py
    
    O pytest entra na pasta tests/ automaticamente

3) Rodando testes (comandos essenciais):
    . Rodar tudo:
        pytest
    . Modo verboso:
        pytest -v
    . Rodar uma pasta:
        pytest tests/
    . Rodar um arquivo específico:
        pytest tests/test_usuario.py
    . Rodar um único teste:
        pytest tests/test_usuario.py::test_usuario_criado_corretamente
        
        Muito usado no dia a dia!!!

4) Filtrar testes por nome(-k):
    Rodar testes que contenham uma palavra no nome:
        pytest -k idade
    
    Exemplo:
        . Roda test_idade_negativa
        . Roda test_idade_valida

5) Parar no primeiro erro:
    pytest -x