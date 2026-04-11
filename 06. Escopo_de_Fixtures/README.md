# 🧪 Pytest - Escopo de Fixtures

---

## 1) O que é escopo de fixture

O **escopo define por quanto tempo a fixture "vive"**.

Por padrão:

```python
@pytest.fixture
def usuario():
    ...
```

- Equivale a `scope="function"`  
- Ou seja: a fixture é criada **uma vez por teste**

---

## 2) `scope="function"`

```python
@pytest.fixture(scope="function")
def usuario():
    print("criando usuario")
    return criar_usuario("Leandro", 20)
```

- Executa **antes de cada teste**  
- **Isolamento total**  
- Mais seguro

---

## 3) `scope="module"`

```python
@pytest.fixture(scope="module")
def usuario():
    print("criando usuario uma vez por módulo")
    return criar_usuario("Leandro", 20)
```

- Criada **uma vez por arquivo de teste**  
- Reutilizada em todos os testes do arquivo  
- Mais rápida, menos isolada

---

## 4) `scope="session"`

```python
@pytest.fixture(scope="session")
def usuario():
    print("criando usuario uma vez por sessão")
    return criar_usuario("Leandro", 20)
```

- Criada **uma vez por execução do pytest**  
- Compartilhada entre todos os testes  
- Máximo desempenho, isolamento mínimo

---

## 5) Regra

- Quanto maior o escopo → menor isolamento  
- Quanto menor o escopo → maior segurança

---

## 6) Utilidade real

### Cenário 1 — Custo / Performance:

```python
@pytest.fixture
def banco():
    print("Conectando ao banco...")
    time.sleep(2)
    return conectar_banco()
```

- Se você tiver 30 testes com **scope=function** → conecta 30 vezes (≈60 segundos)  
- Agora com **scope=module** → conecta **1 vez por arquivo**, economizando muito tempo

💡 Em resumo:

- O escopo não muda **o que a fixture faz**, mas **quantas vezes ela é executada**  
- Pode economizar muito tempo dependendo do cenário