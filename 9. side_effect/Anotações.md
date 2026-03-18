# 🧪 Pytest - Mock: side_effect

---

## 1) O que é `side_effect`

`side_effect` permite que um mock:

- Lance exceções  
- Retorne valores diferentes a cada chamada  
- Execute uma função real ou fake  
- Mude de comportamento a cada chamada  

💡 É como dizer: `"Quando essa função falsa for chamada, faça X"`.

---

## 2) Por que é necessário

Sem o `side_effect`, o mock:

- Apenas **registra chamadas**  
- Sempre retorna `None`  

Na realidade, dependências externas podem falhar:

- Serviços falham  
- Exceções acontecem  
- Retornos variam  

✅ `side_effect` deixa os testes mais realistas.

---

## 3) Exemplo base com código real

**email_service.py**
```python
def enviar_email(email):
    print(f"Email enviado para {email}")
```

**usuario.py**
```python
from email_service import enviar_email

def criar_usuario(nome, email):
    enviar_email(email)
    return {"nome": nome, "email": email}
```

---

## 4) `side_effect` lançando exceção

Simulando falha no serviço de email:

```python
from unittest.mock import patch
import pytest
from usuario import criar_usuario

def test_erro_ao_enviar_email():
    with patch("usuario.enviar_email") as mock_email:
        mock_email.side_effect = RuntimeError("Falha no serviço")

        with pytest.raises(RuntimeError, match="Falha no serviço"):
            criar_usuario("Leandro", "leandro@email.com")
```

💡 O mock **finge que o serviço quebrou**.

---

## 5) `side_effect` com múltiplos retornos

Cada chamada consome um item da lista:

```python
def test_varios_comportamentos():
    with patch("usuario.enviar_email") as mock_email:
        mock_email.side_effect = [None, RuntimeError("Erro")]

        # Primeira chamada funciona
        criar_usuario("Leandro", "a@email.com")

        # Segunda chamada dispara exceção
        with pytest.raises(RuntimeError):
            criar_usuario("Leandro", "b@email.com")
```

---

## 6) `side_effect` executando uma função

Podemos usar uma função fake para simular validação:

```python
def fake_email(email):
    if "@" not in email:
        raise ValueError("Email inválido")

def test_validacao_email():
    with patch("usuario.enviar_email") as mock_email:
        mock_email.side_effect = fake_email

        with pytest.raises(ValueError):
            criar_usuario("Leandro", "email_invalido")
```

---

## 7) Quando usar `side_effect`

- **Use quando:**  
  - Quer simular erro  
  - Quer simular instabilidade  
  - Precisa de retorno variável  
  - Precisa testar fluxo de exceção  

- **Não use quando:**  
  - Retorno simples basta  
  - Não há variação de comportamento