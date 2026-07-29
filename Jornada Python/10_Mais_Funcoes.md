# Funções: Escopo, Docstrings e Módulos

## EXPLICAÇÃO

Aprofundando em funções, abordamos como o Python gerencia variáveis, documentação e reutilização de código externo.

1. **Escopo de Variáveis**:
   * **Local**: Variáveis criadas dentro de uma função. Só existem lá dentro.
   * **Global**: Variáveis criadas fora das funções. São visíveis em todo o código (leitura).
   * **Palavra-chave `global`**: Usada dentro de uma função para permitir a **modificação** de uma variável global.
2. **Docstrings**: Strings de documentação entre aspas triplas `""" """` logo abaixo da definição da função. Elas explicam o que a função faz e podem ser lidas com `help(funcao)`.
3. **Módulos e Bibliotecas**:
   * `import modulo`: Importa todas as funcionalidades (ex: `math.sqrt()`).
   * `from modulo import item`: Importa apenas o que é necessário.
   * `as`: Cria um "apelido" (*alias*) para o módulo (ex: `import numpy as np`).

## EXEMPLO PRÁTICO

```python
# Exemplo de Escopo e Global
contador = 0

def incrementar():
    global contador
    contador += 1
    print(f"Dentro: {contador}")

incrementar()
print(f"Fora: {contador}")

# Exemplo de Docstring
def soma(a, b):
    """Retorna a soma de dois números."""
    return a + b

help(soma)

# Uso de Módulos
import math as m
print(m.sqrt(16)) # Raiz quadrada
```
