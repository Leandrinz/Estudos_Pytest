def nnome_idade (idade = 0, nome = "Desconhecido"):
    if type(idade) != int:
        return "Erro! Digite um número em idade!"
    elif type(nome) != str:
        return "Erro! Digite uma string em nome!"
    else: 
        return f"Olá, {nome}! Você tem {idade} anos."


ah = nnome_idade(19, "Leandro")
