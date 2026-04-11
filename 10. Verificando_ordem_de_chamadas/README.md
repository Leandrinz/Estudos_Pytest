# 🧪 Pytest / Mock - Verificando Ordem de Chamadas

---

## 📌 Contexto

Até agora testamos:

- Se a função foi chamada  
- Se lançou erro  
- Se retornou certo  

Agora vamos testar algo mais avançado:

- A função foi chamada na **ordem correta**?  
- Todas as chamadas aconteceram como deveriam?

---

## 1) `call_count`

Verifica **quantas vezes** uma função foi chamada.

```python
def test_chamada_duas_vezes():
    with patch("pedido.cobrar_cartao") as mock_cobrar:
        finalizar_pedido(1111, 100)
        finalizar_pedido(2222, 200)

        assert mock_cobrar.call_count == 2
```

💡 Útil para:

- Loops  
- Retries  
- Múltiplos pedidos

---

## 2) `call_args`

Permite inspecionar os **argumentos da última chamada**.

```python
def test_ultima_chamada():
    with patch("pedido.cobrar_cartao") as mock_cobrar:
        finalizar_pedido(1234, 100)
        finalizar_pedido(5678, 200)

        args, kwargs = mock_cobrar.call_args
        assert args == (5678, 200)
```

---

## 3) `call_args_list` (histórico completo)

Mostra **todas as chamadas**, na ordem que ocorreram.

```python
def test_historico_de_chamadas():
    with patch("pedido.cobrar_cartao") as mock_cobrar:
        finalizar_pedido(1111, 100)
        finalizar_pedido(2222, 200)

        assert mock_cobrar.call_args_list == [
            ((1111, 100), {}),
            ((2222, 200), {}),
        ]
```

---

## 4) `assert_has_calls`

Forma **mais limpa** de verificar múltiplas chamadas na ordem certa.

```python
from unittest.mock import call

def test_ordem_das_chamadas():
    with patch("pedido.cobrar_cartao") as mock_cobrar:
        finalizar_pedido(1111, 100)
        finalizar_pedido(2222, 200)

        mock_cobrar.assert_has_calls([
            call(1111, 100),
            call(2222, 200),
        ])
```

💡 Se a ordem mudar, o teste falha.

---

## 5) Ordem entre funções diferentes

Podemos testar múltiplas funções que devem ser chamadas:

```python
with patch("pedido.cobrar_cartao") as mock_cobrar, \
     patch("pedido.salvar_pedido") as mock_salvar:
    
    finalizar_pedido(1234, 500)

    assert mock_cobrar.call_count == 1
    assert mock_salvar.call_count == 1
```

✅ Isso garante que **cada função foi chamada a quantidade correta de vezes**.