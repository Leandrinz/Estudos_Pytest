import pytest
from unittest.mock import patch
from pedido import finalizar_pedido

def test_fluxo_feliz_completo():
    with patch("pedido.cobrar_cartao") as mock_cobrar, \
         patch("pedido.salvar_pedido") as mock_salvar, \
         patch("pedido.enviar_notificacao") as mock_notificacao:
        
        resultado = finalizar_pedido(
            cartao=4321,
            valor=1000,
            email= "leandrin@email.com"
        )

        mock_cobrar.assert_called_once_with(4321, 1000)
        mock_notificacao.assert_called_once_with("leandrin@email.com", "Pedido confirmado")
        mock_salvar.assert_called_once_with(4321, 1000)

        assert resultado["status"] == "confirmado"


def test_falha_na_cobranca():
    with patch("pedido.cobrar_cartao") as mock_cobrar, \
         patch("pedido.salvar_pedido") as mock_salvar, \
         patch("pedido.enviar_notificacao") as mock_notificacao:
        
        mock_cobrar.side_effect = RuntimeError

        with pytest.raises(RuntimeError):
            finalizar_pedido(1234, 1000, "leandrin@email.com")
        
        mock_salvar.assert_not_called()
        mock_notificacao.assert_not_called()


def test_falha_ao_salvar():
    with patch("pedido.cobrar_cartao") as mock_cobrar, \
         patch("pedido.salvar_pedido") as mock_salvar, \
         patch("pedido.enviar_notificacao") as mock_notificacao:
        
        mock_salvar.side_effect = RuntimeError

        with pytest.raises(RuntimeError):
            finalizar_pedido(1234, 1000, "leandrin@email.com")
        

def test_falha_ao_enviar_notificacao():
    with patch("pedido.cobrar_cartao") as mock_cobrar, \
         patch("pedido.salvar_pedido") as mock_salvar, \
         patch("pedido.enviar_notificacao") as mock_notificacao:
        
        mock_notificacao.side_effect = RuntimeError

        with pytest.raises(RuntimeError):
            finalizar_pedido(1234, 1000, "leandrin@email.com")

        mock_cobrar.assert_called_once()
        mock_salvar.assert_called_once()



