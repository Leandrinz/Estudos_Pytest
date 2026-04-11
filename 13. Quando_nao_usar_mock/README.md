# 🚫 Quando NÃO Usar Mock

---

## 1️⃣ Erro clássico: mockar tudo

```python
def test_alguma_coisa():
    with patch("modulo.funcao_a"), \
         patch("modulo.funcao_b"), \
         patch("modulo.funcao_c"):
        ...
```

❌ Problemas:
- Teste fica frágil  
- Qualquer refatoração quebra o teste  
- Você testa **implementação**, não **comportamento**

---

## 2️⃣ Regra de ouro

- **Mock apenas o que você NÃO controla**

### Não mockar:
- Funções puras (cálculos, regras de negócio)  
- Funções do mesmo módulo  
- Código simples e determinístico

### Mockar:
- Banco de dados  
- APIs externas  
- Envio de emails  
- Sistemas de pagamento  
- IO (arquivos, rede)

---

## 3️⃣ Exemplo ruim (mock desnecessário)

```python
def calcular_total(itens):
    return sum(itens)

def test_total():
    with patch("modulo.sum") as mock_sum:
        mock_sum.return_value = 10
        assert calcular_total([1, 2, 3]) == 10
```

❌ Por quê?
- Não testou nada útil  
- Quebra princípio de teste unitário  

---

## 4️⃣ Exemplo correto (sem mock)

```python
def test_total():
    assert calcular_total([1, 2, 3]) == 6
```

✅ Simples, robusto, confiável

---

## 5️⃣ Quando mock AUMENTA a qualidade

```python
def enviar_email(email):
    smtp.send(email)

def test_envia_email():
    with patch("email.smtp.send") as mock_send:
        enviar_email("a@b.com")
        mock_send.assert_called_once()
```

💡 Aqui:
- Mock evita envio real  
- Isola efeitos colaterais  
- Aumenta confiabilidade do teste