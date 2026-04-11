# 🔗 Testes de Integração com Pytest

---

## 1️⃣ O que é teste de integração

- Teste que **não usa mock**  
- Executa **múltiplas partes reais**  
- Valida **comportamento do sistema como um todo**

> Diferente do unitário:  
> - Unitário = função isolada  
> - Integração = fluxo completo, módulos juntos

---

## 2️⃣ Quando usar

- Garantir que **módulos conversam corretamente**  
- Validar **fluxo de dados real**  
- Evitar **quebras na interação entre partes**

### Exemplos clássicos:
- Salvar no banco de dados  
- API chamando outro serviço  
- Fluxo de pedido completo

---

## 3️⃣ Exemplo de fluxo real

```python
# pagamento.py
def cobrar_cartao(cartao, valor):
    if valor <= 0:
        raise ValueError("Valor inválido")

# repositorio.py
def salvar_pedido(cartao, valor):
    return {"cartao": cartao, "valor": valor}

# pedido.py
from pagamento import cobrar_cartao
from repositorio import salvar_pedido

def finalizar_pedido(cartao, valor):
    cobrar_cartao(cartao, valor)
    return salvar_pedido(cartao, valor)
```

---

## 4️⃣ Teste de integração (sem mock)

```python
def test_fluxo_real_completo():
    resultado = finalizar_pedido(1234, 100)

    assert resultado["cartao"] == 1234
    assert resultado["valor"] == 100
```

✅ Simples, confiável e **reflete o comportamento real** do sistema