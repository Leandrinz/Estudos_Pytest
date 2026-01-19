livros = []

def adicionar_novo_livro_na_lista(lista, titulo, ano, autor):
    for livro in lista:
        if livro["titulo"] == titulo:
            raise ValueError("Livro já cadastrado")
    
    novo_livro = {"titulo": titulo, "ano": ano, "autor": autor}
    lista.append(novo_livro)
    return novo_livro

def remover_livro_na_lista(lista, titulo_para_remover):
    livro_encontrado = None
    for livro in lista:
        if livro["titulo"].lower() == titulo_para_remover.lower():
            livro_encontrado = livro
            break
    
    if livro_encontrado:
        lista.remove(livro_encontrado)
        return True
    else:
        raise ValueError("Livro não encontrado")

def buscar_livro_na_lista(lista, titulo_para_encontrar):
    for livro in lista:
        if livro["titulo"].lower() == titulo_para_encontrar.lower():
            return True
    return False

def menu():
    print("\n" + "-=" * 15)
    print("BEM VINDO A BIBLIOTECA")
    print("1 - Adicionar livro")
    print("2 - Buscar livro")
    print("3 - Remover livro")
    print("3 - Sair")
    print("-=" * 15)

def tela_adicionar():
    titulo = input("Digite o nome do livro: ")
    ano = int(input("Digite o ano: "))
    autor =  input("Digite o nome do autor: ")
    try:
        adicionar_novo_livro_na_lista(livros, titulo, ano, autor)
        print("Livro adicionaado com sucesso!")
    except ValueError as e:
        print(f"Erro: {e}")

def tela_remover():
    titulo = input("Digite o livro para ser removido: ")
    try:
        remover_livro_na_lista(livros, titulo)
    except ValueError as e:
        print(f"Erro: {e}")

def tela_buscar():
    titulo = input("Digite o livro a ser buscado: ")
    achou = buscar_livro_na_lista(livros, titulo)
    if achou:
        print("Livro encontrado no acervo")
    else:
        print("Livro não encontrado")

if __name__ == "__main__":
    while True:
        menu()
        op = int(input("Opção: "))
        match op:
            case 1:
                tela_adicionar()
            
            case 2:
                tela_buscar()

            case 3:
                tela_remover()

            case 0:
                break