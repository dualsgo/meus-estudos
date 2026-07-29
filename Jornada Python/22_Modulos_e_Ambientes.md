# Módulos, Pacotes e Ambientes Virtuais

## EXPLICAÇÃO

À medida que projetos crescem, é impossível manter tudo em um único arquivo. Python usa uma estrutura modular para organizar código e gerenciar dependências externas.

1. **Módulo**: Qualquer arquivo `.py`. Pode ser importado por outros.
2. **Pacote**: Uma pasta contendo múltiplos módulos e um arquivo (opcional nas versões novas) `__init__.py`.
3. **PIP (Package Installer for Python)**: Ferramenta para instalar bibliotecas de terceiros (ex: `pip install requests`).
4. **Ambientes Virtuais (`venv`)**: Criam "bolhas" isoladas para cada projeto. Isso evita que a biblioteca do Projeto A quebre o Projeto B devido a versões diferentes.
   * Criar: `python -m venv venv`
   * Ativar (Windows): `.\venv\Scripts\activate`

## EXEMPLO PRÁTICO

```python
# Estrutura Sugerida:
# meu_projeto/
# ├── venv/
# ├── main.py
# └── utilitarios/
#     ├── __init__.py
#     └── moedas.py

# No arquivo utilitarios/moedas.py:
def formatar(valor):
    return f"R$ {valor:>.2f}".replace('.', ',')

# No arquivo main.py:
from utilitarios import moedas

preco = 1500.5
print(f"O preço formatado é: {moedas.formatar(preco)}")

# Comando para instalar dependências externas:
# Terminal: pip install pandas numpy
```
