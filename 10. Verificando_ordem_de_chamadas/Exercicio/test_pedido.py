import pytest
from pagamento import cobrar_cartao
from pedido import finalizar_pedido
from unittest.mock import call
from unittest.mock import patch

def test_finaliza_3_vezes_e_cobrar_3_vezes():
    with patch("pedido.cobrar_cartao") as mock_cobrar:
        
        finalizar_pedido(1111, 100)
        finalizar_pedido(2222, 200)
        finalizar_pedido(3333, 300)

        assert mock_cobrar.call_count == 3

def test_ultima_chamada():
    with patch("pedido.cobrar_cartao") as mock_cobrar:
        
        finalizar_pedido(1111, 222)
        finalizar_pedido(2345, 201)

        args, kwargs = mock_cobrar.call_args
        assert args == (2345, 201)

def test_ordem_cobranca():
    with patch("pedido.cobrar_cartao") as mock_cobrar:
        
        finalizar_pedido(1111, 1000)
        finalizar_pedido(1000, 2032)

        mock_cobrar.assert_has_calls([
            call(1111, 1000),
            call(1000, 2032),
        ])

def test_final():
    with patch("pedido.cobrar_cartao") as mock_cobrar:
        mock_cobrar.side_effect = [None, RuntimeError]

        finalizar_pedido(1, 1)

        with pytest.raises(RuntimeError):
            finalizar_pedido(2, 2)

        assert mock_cobrar.call_count == 2