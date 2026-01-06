from usuario import criar_usuario

# 1. O Usuário deve ser criado corretamente
def test_usuario_criado_corretamente(): 
    usuarioo = criar_usuario(
        nome = "Leandro",
        idade = 20,
        email = "leandro@gmail.com"
    ) 
    
    assert usuarioo["nome"] == "Leandro"
    assert usuarioo["idade"] == 20
    assert usuarioo["email"] == "leandro@gmail.com"

# 2. O nome do usuário deve conter pelo menos o primeiro nome

def test_contem_primeiro_nome():
    usuarioo = criar_usuario(
        nome = "Leandro Savio",
        idade = 19,
        email = "leandro@gmail.com"
    )

    assert "Leandro" in usuarioo["nome"]

# 3. A idade deve ser >= 18
def test_idade_maior_que_18(): 
    usuarioo = criar_usuario(
        nome = "Leandro",
        idade = 20,
        email = "leandro@gmail.com"
    ) 

    assert usuarioo["idade"] >= 18

# 4. o email pode ser None
def test_email_igual_none(): 
    usuarioo = criar_usuario(
        nome = "Leandro",
        idade = 20,
    ) 

    assert usuarioo["email"] is None

# 5. O usuario não deve ter idade negativa
def test_idade_nao_eh_negativa(): 
    usuarioo = criar_usuario(
        nome = "Leandro",
        idade = 20,
        email = "leandro@gmail.com"
    ) 

    assert usuarioo["idade"] >= 0