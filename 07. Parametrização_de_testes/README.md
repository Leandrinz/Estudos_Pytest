# 🧪 Pytest - Parametrização de Testes

---

## 1) O problema clássico

Sem parametrização, o código fica assim:

```python
def test_idade_valida_1():
    assert criar_usuario("A", 18)["idade"] >= 18

def test_idade_valida_2():
    assert criar_usuario("B", 20)["idade"] >= 18

def test_idade_valida_3():
    assert criar_usuario("C", 30)["idade"] >= 18
```

💡 Problemas:

- Código repetido  
- Difícil de manter  
- Leitura ruim  

---

## 2) Solução: `@pytest.mark.parametrize`

```python
import pytest

@pytest.mark.parametrize("idade", [18, 20, 30])
def test_idades_validas(idade):
    usuario = criar_usuario("Leandro", idade)
    assert usuario["idade"] >= 18
```

✅ Em apenas um teste, criamos **vários cenários**.

---

## 3) Vários parâmetros

```python
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
```

- Útil quando queremos **testar múltiplas combinações de dados**  
- Evita repetição e facilita manutenção

---

## 4) Parametrização + exceções

Perfeito para validar erros:

```python
@pytest.mark.parametrize("idade", [-1, -10])
def test_idade_negativa_dispara_erro(idade):
    with pytest.raises(ValueError):
        criar_usuario("Leandro", idade)
```

- Se não lançar `ValueError`, o teste **falha**  
- Se lançar, o teste **passa**

---

## 5) Parametrização + mensagem da exceção

```python
@pytest.mark.parametrize(
    "idade, mensagem",
    [
        (-1, "idade não pode ser negativa"),
        (17, "Usuário deve ser maior de idade"),
    ]
)
def test_idades_invalidas(idade, mensagem):
    with pytest.raises(ValueError, match=mensagem):
        criar_usuario("Leandro", idade)
```

- Permite validar não apenas a exceção, mas também a **mensagem correta**  
- Excelente prática para **regras de negócio**