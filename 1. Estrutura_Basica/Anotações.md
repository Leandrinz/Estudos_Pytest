# 🧪 Estrutura básica de pytest

O **pytest** é um framework de testes em Python que permite escrever testes de forma **simples e direta**, sem necessidade de classes ou configurações complexas.

---

# 1) Teste Simples

No pytest, não precisamos de classe nem de `self`.  
Basta criar **funções que comecem com `test_`**.

```python
# arquivo: test_exemplo.py

def test_soma():
    assert 2 + 3 == 5
```

O pytest automaticamente:

- encontra arquivos que começam com `test_`
- executa funções que começam com `test_`

---

# 2) Rodando os testes

No terminal, dentro da pasta do projeto:

```bash
pytest
```

---

## Mais detalhes na execução

Para exibir mais informações:

```bash
pytest -v
```

O `-v` significa **verbose** (modo detalhado).

---

# 💡 Dica

O pytest mostra mensagens de erro **muito mais claras** que o PyUnit.

Exemplo de falha:

```python
def test_soma():
    assert 2 + 2 == 5
```

Saída do pytest:

```
E       assert 4 == 5
```

Ou seja, ele mostra:

- valor obtido → `4`
- valor esperado → `5`

Enquanto o PyUnit geralmente mostraria apenas:

```
AssertionError
```

---

# ✔ Conclusão

O pytest é muito usado porque:

- é simples de escrever
- não exige classes
- possui mensagens de erro claras
- facilita a criação de testes rápidos

Ideal para quem está começando com **testes automatizados**.