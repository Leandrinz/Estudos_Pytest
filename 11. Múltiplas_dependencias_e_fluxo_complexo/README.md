# 🧪 Pytest / Mock - Múltiplas Dependências e Fluxo Complexo

---

## 1️⃣ Contexto do Problema

Imagine um cenário realista:

- Cobra o cartão  
- Salva o pedido no banco  
- Envia a notificação  
- Retorna o resultado final  

Precisamos garantir que:

1. Cada passo seja chamado corretamente  
2. Falhas interrompam o fluxo corretamente  

---

## 2️⃣ Código Base

```python
from pagamento import cobrar_cartao
from notificacao import enviar_notificacao
from repositorio import salvar_pedido

def finalizar_pedido(cartao, valor, email):
    cobrar_cartao(cartao, valor)
    salvar_pedido(cartao, valor)

    enviar_notificacao(email, "Pedido confirmado")

    return {
        "cartao": cartao,
        "valor": valor,
        "status": "confirmado"
    }
```

---

## 3️⃣ O que mockar

### Deve ser mockado:
- `cobrar_cartao` → serviço externo  
- `salvar_pedido` → banco de dados  
- `enviar_notificacao` → email / serviço externo  

### Não deve ser mockado:
- `finalizar_pedido` (função testada)  
- lógica interna simples  
- retorno final

---

## 4️⃣ Teste correto com múltiplos mocks

```python
import pytest
from unittest.mock import patch
from pedido import finalizar_pedido

def test_fluxo_complexo_com_sucesso():
    with patch("pedido.cobrar_cartao") as mock_cobrar, \
         patch("pedido.salvar_pedido") as mock_salvar, \
         patch("pedido.enviar_notificacao") as mock_notificar:
        
        resultado = finalizar_pedido(
            cartao=1234,
            valor=100,
            email="test@email.com"
        )

        mock_cobrar.assert_called_once_with(1234, 100)
        mock_notificar.assert_called_once_with(
            "test@email.com",
            "Pedido confirmado"
        )

        assert resultado["status"] == "confirmado"
```

✅ Verifica:
- Chamadas corretas  
- Argumentos corretos  
- Retorno final correto

---

## 5️⃣ Testando falha no meio do fluxo

```python
def test_falha_na_cobranca_nao_salva_nem_notifica():
    with patch("pedido.cobrar_cartao") as mock_cobrar, \
         patch("pedido.salvar_pedido") as mock_salvar, \
         patch("pedido.enviar_notificacao") as mock_notificar:

        mock_cobrar.side_effect = RuntimeError("Falha na cobrança")

        with pytest.raises(RuntimeError):
            finalizar_pedido(1234, 100, "test@email.com")

        mock_salvar.assert_not_called()
        mock_notificar.assert_not_called()
```

💡 Isso garante que, em caso de falha:

- O fluxo para imediatamente  
- Nenhuma ação subsequente é executada