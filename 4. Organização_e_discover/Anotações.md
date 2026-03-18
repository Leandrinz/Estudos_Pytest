# 🧪 Organização de Arquivos e Discover no Pytest

---

# 1) Como o pytest encontra seus testes (discover)

O pytest **descobre testes automaticamente** seguindo regras específicas:

- **Arquivos**:
  - `test_*.py`
  - `*_test.py`

- **Funções**:
  - Devem começar com `test_`, ex: `def test_alguma_coisa():`

- **Classes (opcional)**:
  - Começam com `TestAlgo`
  - Métodos também começam com `test_`
  - Não precisam herdar de nada

💡 Seguindo essas regras, o pytest consegue identificar e rodar todos os testes automaticamente.

---

# 2) Estrutura de projeto recomendada

```text
projeto/
|
|-- usuario.py
|-- emprestimo.py
|
|_tests/
   |-- __init__.py  (opcional)
   |-- test_usuario.py
   |-- test_emprestimo.py
```

O pytest **entra automaticamente** na pasta `tests/` para procurar testes.

---

# 3) Rodando testes (comandos essenciais)

- **Rodar todos os testes:**

```bash
pytest
```

- **Modo verboso (mais detalhes):**

```bash
pytest -v
```

- **Rodar uma pasta específica:**

```bash
pytest tests/
```

- **Rodar um arquivo específico:**

```bash
pytest tests/test_usuario.py
```

- **Rodar um único teste dentro de um arquivo:**

```bash
pytest tests/test_usuario.py::test_usuario_criado_corretamente
```

💡 Muito útil no dia a dia quando você quer testar apenas uma função.

---

# 4) Filtrar testes por nome (`-k`)

Você pode rodar **apenas testes que contenham uma palavra** no nome:

```bash
pytest -k idade
```

Exemplo:

- Roda `test_idade_negativa`
- Roda `test_idade_valida`

---

# 5) Parar no primeiro erro

```bash
pytest -x
```

💡 Ideal para **depuração rápida**, quando você quer corrigir o primeiro erro antes de rodar todos os testes.

---

# ✔ Conclusão

Seguindo essas boas práticas:

- Os testes ficam organizados  
- É fácil encontrar e rodar qualquer teste  
- O pytest descobre automaticamente o que precisa ser executado  

Isso torna o desenvolvimento **mais ágil e confiável**.