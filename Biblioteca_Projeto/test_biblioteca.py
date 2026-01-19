from biblioteca import adicionar_novo_livro_na_lista, remover_livro_na_lista, buscar_livro_na_lista
import pytest

# --- PARAMETRIZAÇÃO DA LISTA E BIBLIOTECA ---
@pytest.fixture
def lista_exemplo():
    return [{"titulo": "Batman","ano": 2000, "autor": "Stan Lee"}]

@pytest.fixture
def biblioteca_exemplo_com_um_livro():
    return [{"titulo": "Bíblia Sagrada", "ano": 2014, "autor": "Deus"}]

# --- TESTES DE ADICIONAR LIVRO ---
def test_deve_adicionar_livro_com_sucesso():
    minha_lista = []

    adicionar_novo_livro_na_lista(minha_lista, "Batman", 2000, "Stan Lee")

    assert len(minha_lista) == 1
    assert minha_lista[0]["titulo"] == "Batman"

def test_nao_deve_adicionar_livro_duplicado(lista_exemplo):
    with pytest.raises(ValueError, match="Livro já cadastrado"):
        adicionar_novo_livro_na_lista(lista_exemplo, "Batman", 2000, "Stan Lee")

# --- TESTES DE REMOVER LIVRO ---
def test_remover_livro_com_sucesso(lista_exemplo):
    remover_livro_na_lista(lista_exemplo, "Batman")

    assert len(lista_exemplo) == 0

def test_erro_ao_remover():
    minha_lista = []

    with pytest.raises(ValueError, match="Livro não encontrado"):
        remover_livro_na_lista(minha_lista, "Batman")

# --- TESTES DE BUSCA ---
@pytest.mark.parametrize("termo, esperado", [
     ("Bíblia Sagrada", True),
     ("bíblia sagrada", True), 
     ("Java", False)
])
def test_buscar_livro(biblioteca_exemplo_com_um_livro, termo, esperado):
    resultado = buscar_livro_na_lista(biblioteca_exemplo_com_um_livro, termo)
    assert resultado == esperado