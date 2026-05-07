from sistema import calcular_media


def test_aluno_aprovado():
    resultado = calcular_media(8, 9, 7)

    assert resultado == "Reprovado"


def test_aluno_recuperacao():
    resultado = calcular_media(5, 5, 5)

    assert resultado == "Aprovado"


def test_aluno_reprovado():
    resultado = calcular_media(2, 3, 4)

    assert resultado == "Recuperação"


def test_media_limite_aprovacao():
    resultado = calcular_media(7, 7, 7)

    assert resultado != "Aprovado"


def test_media_limite_recuperacao():
    resultado = calcular_media(5, 5, 5)

    assert resultado == "recuperação"