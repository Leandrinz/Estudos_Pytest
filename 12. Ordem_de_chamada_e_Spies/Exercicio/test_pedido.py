import pytest
from unittest.mock import patch, call, Mock
from pedido import finalizar_pedido

def test_cobrar_antes_de_salvar_pedido():
    tracker = Mock()
    with patch("pedido.cobrar_cartao") as mock_cobrar, \
         patch("pedido.enviar_notificacao") as mock_enviar, \
         patch("pedido.salvar_pedido") as mock_salvar:
        
        tracker.attach_mock(mock_cobrar, "cobrar")
        tracker.attach_mock(mock_enviar, "enviar")
        tracker.attach_mock(mock_salvar, "salvar")

        finalizar_pedido(2, 4, "leandrin@email.com")

        assert tracker.mock_calls == [
            call.cobrar(2, 4),
            call.salvar(2, 4),
            call.enviar("leandrin@email.com", "Pedido confirmado")
        ]


def test_notificacao_nao_eh_chamado():
    tracker = Mock()
    with patch("pedido.cobrar_cartao") as mock_cobrar, \
         patch("pedido.enviar_notificacao") as mock_enviar, \
         patch("pedido.salvar_pedido") as mock_salvar:
        
        tracker.attach_mock(mock_cobrar, "cobrar")
        tracker.attach_mock(mock_enviar, "enviar")
        tracker.attach_mock(mock_salvar, "salvar")

        mock_salvar.side_effect = RuntimeError
        with pytest.raises(RuntimeError):
            finalizar_pedido(2, 4, "leandrin@email.com")

        assert tracker.mock_calls == [
            call.cobrar(2, 4),
            call.salvar(2, 4),
        ]

        mock_enviar.assert_not_called()