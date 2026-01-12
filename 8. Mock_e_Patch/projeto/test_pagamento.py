from unittest.mock import patch
from notificacao import enviar_notificacao
from pagamento import processar_pagamento
import pytest

def test_enviou_notificacao_pagamento_valido():
    with patch("pagamento.enviar_notificacao") as mock_notificacao:
        processar_pagamento("leandro@email.com", 10)

        mock_notificacao.assert_called_once_with(
            "leandro@email.com",
            "Pagamento realizado com sucesso"
            )

def test_nao_envia_notificacao_com_valor_invalido():
        with patch("pagamento.enviar_notificacao") as mock_notificacao:
                with pytest.raises(ValueError, match="Valor inválido"):
                      processar_pagamento("Leandro", 0)

                mock_notificacao.assert_not_called()
                
def test_retorna_dados_corretamente():
      with patch("pagamento.enviar_notificacao") as mock_notificacao:
            usuarioo = processar_pagamento("leandro@email.com", 20)

            assert usuarioo["email"] == "leandro@email.com"
            assert usuarioo["valor"] == 20
            assert usuarioo["status"] == "confirmado"