def criar_usuario(nome, idade, email=None):
    if idade < 0:
        raise ValueError("Idade não pode ser negativa")
    
    if idade < 18:
        raise ValueError("Usuário deve ser maior de idade")
    
    return{
        "nome": nome,
        "idade": idade,
        "email": email
    }