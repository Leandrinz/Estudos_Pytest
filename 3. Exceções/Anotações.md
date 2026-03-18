# 🧪 Testando Exceções com Pytest

---

# 1) O problema que iremos resolver

Até agora, a função aceita qualquer idade:

```python
criar_usuario("Leandro", -10)
```

Isso **não faz sentido**, mas o código aceita.

👉 Portanto, precisamos **validar os dados** usando **exceções**.

---

# 2) Atualização do código

No arquivo `usuario.py`, devemos validar a idade, por exemplo:

```python
def criar_usuario(nome, idade):

    if idade < 0:
        raise ValueError("Idade não pode ser negativa")

    if idade < 18:
        raise ValueError("Usuário deve ser maior de idade")

    return {"nome": nome, "idade": idade}
```

---

# 3) Testando exceção com pytest

Usamos `pytest.raises` para verificar se uma exceção é lançada:

```python
import pytest

def test_idade_negativa_dispara_erro():
    with pytest.raises(ValueError):
        criar_usuario("Leandro", -1)
```

✔ Se lançar `ValueError` → teste passa  
❌ Se não lançar → teste falha  

---

# 4) Testando a mensagem da exceção

Também podemos validar a **mensagem do erro**:

```python
def test_idade_negativa_mensagem():
    with pytest.raises(ValueError, match="Idade não pode ser negativa"):
        criar_usuario("Leandro", -5)
```

---

# 5) Testando menor de idade

```python
def test_usuario_menor_de_idade():
    with pytest.raises(ValueError, match="Usuário deve ser maior de idade"):
        criar_usuario("Leandro", 17)
```

---

# 6) Teste positivo (sem exceção)

Aqui verificamos que **nenhum erro é lançado**:

```python
def test_usuario_valido_nao_dispara_excecao():
    usuario = criar_usuario("Leandro", 19)
    assert usuario["idade"] == 19
```

---

# ✔ Conclusão

Testar exceções é essencial para garantir que:

- entradas inválidas sejam tratadas corretamente
- regras de negócio sejam respeitadas
- erros não passem despercebidos

---

# 💡 Dica importante

Sempre teste:

- ❌ casos inválidos (devem lançar erro)
- ✔ casos válidos (devem funcionar normalmente)

Isso garante uma **cobertura de testes completa**.