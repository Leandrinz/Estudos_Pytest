# 🧪 Asserts e Mensagens de Erro Inteligentes (pytest)

---

# 1) O `assert` do pytest

No pytest, usamos o **`assert` normal do Python**:

```python
def test_soma():
    assert 2 + 3 == 5
```

💡 Porém, o pytest **intercepta o assert** e analisa a expressão, mostrando **erros detalhados automaticamente**.

---

# 2) Comparações mais comuns

## Igualdade

```python
def test_igualdade():
    assert 10 == 10
```

---

## Diferente

```python
def test_diferente():
    assert 10 != 3
```

---

## Maior / Menor

```python
def test_maior_menor():
    assert 10 > 5
    assert 3 < 7
```

---

# 3) Testando coleções (`in`)

Muito usado em testes reais.

## Exemplo 1 — Lista

```python
def test_item_em_lista():
    lista = [1, 2, 3]
    assert 2 in lista
```

---

## Exemplo 2 — Dicionário

```python
def test_chave_em_dict():
    usuario = {"nome": "Leandro", "idade": 20}
    assert "nome" in usuario
```

---

# 4) `is`, `is not` e `None`

## Verificando `None`

```python
def test_none():
    resultado = None
    assert resultado is None
```

---

## Verificando valor não nulo

```python
def test_not_none():
    valor = 10
    assert valor is not None
```

---

# 5) Mensagens de erro do pytest

Teste com erro proposital:

```python
def test_erro_exemplo():
    assert 10 == 5
```

Saída típica:

```
>       assert 10 == 5
E       assert 10 == 5
E       + where 10 == 10
E       + and 5 == 5
```

💡 O pytest mostra:

- valor esperado
- valor obtido
- análise da expressão

Muito mais detalhado que o PyUnit.

---

# 6) Comparação de strings (diff automático)

```python
def test_string():
    assert "pytest é ótimo" == "pytest é otimo"
```

O pytest mostra exatamente:

- onde as strings diferem
- caractere por caractere

---

# 7) Assert com mensagem personalizada

```python
def test_com_mensagem():
    assert 2 + 2 == 5, "Soma incorreta"
```

## Boa prática:

- Use quando a regra de negócio **não é óbvia**
- Em geral, **confie na mensagem automática do pytest**

---

# 8) Regra de ouro nos asserts

👉 **Um comportamento por teste**

---

## ❌ Ruim

```python
def test_ruim():
    assert soma(2, 3) == 5
    assert soma(5, 5) == 10
    assert soma(0, 0) == 0
```

---

## ✔ Melhor

```python
def test_soma_basica():
    assert soma(2, 3) == 5
```

💡 No futuro, isso pode ser melhorado com **parametrização de testes**.

---

# ✔ Conclusão

O `assert` do pytest é poderoso porque:

- é simples (usa o próprio Python)
- gera mensagens automáticas detalhadas
- facilita encontrar erros rapidamente

Seguindo boas práticas, seus testes ficam:

- mais organizados
- mais legíveis
- mais fáceis de manter