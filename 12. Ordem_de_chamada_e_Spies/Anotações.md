# 🧪 Pytest / Mock - Ordem de Chamadas e Spies

---

## 1️⃣ Regra de Ouro

Só testamos a ordem quando **a ordem é regra de negócio**:

- ❌ Errado testar:
  - Detalhes de implementação  
  - Quando pode mudar sem quebrar comportamento  

- ✅ Certo testar:
  - Uma ação **não pode ocorrer antes da outra**  
  - Há risco real de comportamento incorreto (ex: cobrar antes de validar, salvar antes de cobrar)

---

## 2️⃣ Verificando ordem de chamadas em um único mock

- Cada mock tem seu próprio histórico (`mock_calls`):

```python
from unittest.mock import patch, call
from pedido import finalizar_pedido

def test_ordem_das_chamadas():
    with patch("pedido.cobrar_cartao") as mock_cobrar, \
         patch("pedido.salvar_pedido") as mock_salvar, \
         patch("pedido.enviar_notificacao") as mock_notificacao:

        finalizar_pedido(1234, 100, "email@email.com")

        # Apenas histórico do mock_cobrar
        assert mock_cobrar.mock_calls == [call(1234, 100)]
```

> Atenção: isso **não resolve a ordem entre mocks diferentes**.

---

## 3️⃣ Testando ordem entre funções diferentes

- Combine os históricos no **mesmo namespace**:

```python
def test_ordem_completa_do_fluxo():
    with patch("pedido.cobrar_cartao") as cobrar, \
         patch("pedido.salvar_pedido") as salvar, \
         patch("pedido.enviar_notificacao") as notificar:

        finalizar_pedido(1, 2, "a@a.com")

        chamadas = cobrar.mock_calls + salvar.mock_calls + notificar.mock_calls

        assert chamadas == [
            call(1, 2),
            call(1, 2),
            call("a@a.com", "Pedido confirmado")
        ]
```

> Use apenas quando a **ordem realmente importa**.

---

## 4️⃣ Usando Spy (observar chamadas reais)

- Em vez de mockar tudo, você pode **envolver a função real**:

```python
from pedido import finalizar_pedido, cobrar_cartao
from unittest.mock import patch

def test_spy_cobrar_cartao():
    with patch("pedido.cobrar_cartao", wraps=cobrar_cartao) as spy:
        finalizar_pedido(1234, 100, "a@a.com")
        spy.assert_called_once()
```

> O `wraps` permite que a função real seja executada, mas ainda verificamos as chamadas.

---

## 5️⃣ Forma definitiva: attach_mock

- Para **monitorar múltiplos mocks em um único tracker**:

```python
from unittest.mock import Mock, call, patch
from pedido import finalizar_pedido

def test_cobrar_antes_de_salvar_pedido():
    tracker = Mock()

    with patch("pedido.cobrar_cartao") as mock_cobrar, \
         patch("pedido.salvar_pedido") as mock_salvar:

        tracker.attach_mock(mock_cobrar, "cobrar")
        tracker.attach_mock(mock_salvar, "salvar")

        finalizar_pedido(2, 4, "leandrin@email.com")

        assert tracker.mock_calls == [
            call.cobrar(2, 4),
            call.salvar(2, 4)
        ]
```

✅ Vantagens:
- Ordem exata das chamadas  
- Visualização centralizada de múltiplos mocks  
- Segurança de que a lógica crítica segue a sequência correta