import pytest
from pedido import cobrar_cartao
from pedido import finalizar_pedido
from unittest.mock import patch

def test_falha_no_sistema():
    with patch("pedido.cobrar_cartao") as mock_cobrar:
        mock_cobrar.side_effect = RuntimeError("Falha na cobrança")

        with pytest.raises(RuntimeError, match="Falha na cobrança"):
            finalizar_pedido("123438293023949", 1000)

def test_multiplos_comportamentos():
    with patch("pedido.cobrar_cartao") as mock_cobrar:
            mock_cobrar.side_effect = [None, RuntimeError("Serviço indisponível")]
        
            resultado = finalizar_pedido("1231243441", 1000)
            assert resultado["status"] == "pago"


            with pytest.raises(RuntimeError):
                 finalizar_pedido("12345325323", 1000)

def fake_cobranca(numero_cartao, valor):
     if len(numero_cartao) != 16:
          raise ValueError("Cartão inválido")

def test_executando_funcao_falsa():
     with patch("pedido.cobrar_cartao") as mock_cobrar:
        mock_cobrar.side_effect = fake_cobranca

        with pytest.raises(ValueError, match="Cartão inválido"):
            finalizar_pedido("123141414", 234)

def test_funcao_chamada_antes_da_falha():
     with patch("pedido.cobrar_cartao") as mock_cobrar:
          mock_cobrar.side_effect = RuntimeError("Erro na cobrança")


          with pytest.raises(RuntimeError, match="Erro na cobrança"):
               finalizar_pedido(12434, 1412)

          mock_cobrar.assert_called_once_with(12434, 1412)  

def test_assert_not_called():
     with patch("pedido.cobrar_cartao") as mock_cobrar:
          mock_cobrar.side_effect = None


     with pytest.raises(ValueError, match="Valor inválido"):
          finalizar_pedido("23", -10)
    
          mock_cobrar.assert_not_called_with("23", -10)

