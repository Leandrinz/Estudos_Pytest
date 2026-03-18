# 🧪 Pytest - Mock e Patch

---

## 1) Problema que o Mock resolve

Até agora, os testes trabalharam com:

- Funções puras (entrada → saída)  
- Sem dependências externas  

Na prática, funções reais podem depender de:

- Outras funções  
- Serviços externos (email, API, banco)  
- Dados dinâmicos (hora atual, UUID, random)  

💡 Testar isso **quebra o conceito de teste unitário**.

---

## 2) O que é Mock

- Mock significa **substituir uma dependência real por uma falsa e controlável**.  
- Objetivos:  
  - Isolar a unidade testada  
  - Controlar o comportamento da dependência  
  - Verificar se ela foi usada corretamente  

---

## 3) O que é Patch

- `patch` é a ferramenta que:  
  - Substitui temporariamente uma função, classe ou objeto  
  - Apenas durante o teste  
  - Sem alterar o código original  

- No pytest (unittest.mock):
```python
from unittest.mock import patch
```

---

## 4) Exemplo de dependência

**email_service.py**
```python
def enviar_email(email):
    print(f"Enviando email para {email}")
```

**usuario.py**
```python
from email_service import enviar_email

def criar_usuario(nome, idade, email):
    if idade < 18:
        raise ValueError("Usuário deve ser maior de idade")

    enviar_email(email)

    return {
        "nome": nome,
        "idade": idade,
        "email": email
    }
```

💡 Problema: testar isso **chamaria dependência externa**.

---

## 5) Aplicando Patch no teste

```python
from usuario import criar_usuario
from unittest.mock import patch

def test_envia_email_ao_criar_usuario():
    with patch("usuario.enviar_email") as mock_email:
        criar_usuario("Leandro", 20, "leandro@email.com")
        mock_email.assert_called_once_with("leandro@email.com")
```

---

## 6) Regra fundamental do Patch

- Faça o patch **onde a função é usada**, não onde foi criada  

❌ Errado:
```python
patch("email_service.enviar_email")
```

✅ Correto:
```python
patch("usuario.enviar_email")
```

---

## 7) O que o Mock permite verificar

Com o objeto mock, você pode:

- Verificar se foi chamado: `mock.assert_called()`  
- Verificar quantas vezes: `mock.call_count`  
- Verificar argumentos usados:  
  ```python
  mock.assert_called_once()
  mock.assert_not_called()
  mock.assert_called_with("email@email.com")
  ```

---

## 8) Quando usar (e quando não usar)

- **Use quando:**  
  - A dependência **não é o foco do teste**  
  - Envolve **recursos externos**  
  - Pode causar **efeitos colaterais**  

- **Não use quando:**  
  - Lógica interna simples  
  - Funções puras