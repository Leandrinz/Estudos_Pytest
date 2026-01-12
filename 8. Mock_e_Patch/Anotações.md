---  Mock e Patch ---

1) O problema que o mock resolve:
    
    - Até agora, os testes trabalharam com:
        . Funções puras
        . Entrada -> saída
        . Sem dependências externas
    
    - Na prática, funções reais dependem de:
        . Outras funções
        . Serviços externos (email, API, banco)
        . Dados dinâmicos (hora atual, UUID, random)

    . Testar isso quebra o conceito de teste unitário


2) O que é Mock:
    
    - Mock significa:
        . Substituir uma dependência real por uma falsa e controlável
    
    - O objetivo é:
        . Isolar a unidade testada   
        . Controlar o comportamento da dependência
        . Verificar se ela foi usada corretamente


3) O que é Patch:

    - patch é a ferramente que:
        . Substitui temporariamente uma função, classe ou objeto
        . Apenas durante o teste
        . Sem alterar código
    
    - No pytest, usamos:
        from unittest.mock import patch


4) Exemplo de código com dependência:
    "email_service.py":
        def enviar_email(email):
            print(f"Enviando email para {email}")
    
    "usuario.py":
        from email_service import enviar_email

        def criar_usuario(nome, idade, email):
            if idade < 18:
                raise ValueError("Usuário deve ser maior de idade")

            enviar_email(email)

            return {
                "nome": nome,
                "idade": idade,
                "email": email
            }

    . Problema:
        Executar testes aqui chamaria uma dependência externa.


5) Aplicando patch no teste:
    
    - Teste com mock:

        from usuario import criar_usuario
        from unittest.mock import patch

        def test_envia_email_ao_criar_usuario():
            with patch("usuario.enviar_email") as mock_email:
                criar_usuario("Leandro", 20, "leandro@email.com")

                mock_email.assert_called_once_with("leandro@email.com")


6) Regra fundamental do patch:
    . Sempre faça o patch onde a função é usada, não onde foi criada

    . Errado:
        patch("email_service.enviar_email")
    
    . Correto:
        patch("usuario.enviar_email")


7) O que o mock permite verificar:
    - Com o objeto mock, você pode:
       . Verificar se foi chamado
       . Verificar quantas vezes
       . Verificar os argumentos usados
    
    - Exemplos:
        . mock.assert_called()
        . mock.assert_called_once()
        . mock.assert_not_called()
        . mock.assert_called_with("email@email.com")
        . mock.call_count

8) Quando usar o mock(e quando não usar):
    
    - Use quando:
        . A dependência não é o foco do teste
        . Envolve recursos externos
        . Pode causar efeitos colaterais
    
    - Não use quando:
        . Lógica interna simples
        . Funções puras