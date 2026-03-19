# 🧪 Pytest - Fixtures

---

# 1) O problema que as fixtures resolvem

Quando vários testes precisam do **mesmo objeto** (ex: usuário), sem fixtures você acaba repetindo código:

```python
# Sem fixture (ruim e repetitivo)
def test_usuario_nome():
    usuario = criar_usuario("Leandro", 20)
    assert usuario["nome"] == "Leandro"

def test_usuario_idade():
    usuario = criar_usuario("Leandro", 20)
    assert usuario["idade"] == 20
```

💡 Problemas:

- Repetição de código  
- Manutenção difícil  

---

# 2) Criando a fixture

```python
import pytest
from usuario import criar_usuario

@pytest.fixture
def usuario_valido():
    return criar_usuario("Leandro", 20, "leandro@email.com")
```

- Cria um **objeto reutilizável**  
- Pode ser usado em qualquer teste que precisar de um usuário válido

---

# 3) Usando a fixture no teste

O pytest **injetará a fixture automaticamente** pelo nome:

```python
def test_nome_usuario(usuario_valido):
    assert usuario_valido["nome"] == "Leandro"
```

---

# 4) Fixture != função comum

- Você **não chama** a fixture manualmente  
- Você **declara como parâmetro** do teste  
- O pytest faz a execução

```python
# Errado
usuario = usuario_valido()

# Correto
def test_algo(usuario_valido):
    ...
```

---

# 5) Fixture com `yield` (setup + teardown)

- Equivalente ao `setUp` / `tearDown` do PyUnit

```python
@pytest.fixture
def recurso():
    print("setup")
    yield "recurso pronto"
    print("teardown")
```

Fluxo de execução:

1. `setup`  
2. Executa o teste  
3. `teardown`

---

# 6) Reutilizando fixtures entre arquivos

- Coloque as fixtures em um arquivo especial `conftest.py`:

```
tests/
|-- conftest.py
|-- test_usuario.py
```

- Exemplo `conftest.py`:

```python
import pytest
from usuario import criar_usuario

@pytest.fixture
def usuario_valido():
    return criar_usuario("Leandro", 20)
```

💡 O pytest **enxerga automaticamente** esse arquivo, não precisa importar nada.

---

# 7) Boas práticas com fixtures

- **Fixture cria contexto**  
- **Fixture não cria lógica de teste**

```python
# Errado
@pytest.fixture
def usuario():
    assert idade >= 18

# Certo
@pytest.fixture
def usuario():
    return criar_usuario("Leandro", 20)
```

- Use fixtures para **preparar dados ou objetos**  
- Mantenha a lógica de verificação dentro dos testes