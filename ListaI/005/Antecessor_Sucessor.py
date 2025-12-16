def antecessor_sucessor(numero = 0):
    try:
        antecessor = numero - 1
        sucessor = numero + 1
    except TypeError:
        return "Erro, Digite um número!"
    else:
        return [antecessor, sucessor]
    

antecessor_sucessor(0)