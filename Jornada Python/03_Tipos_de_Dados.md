# Tipos de Dados em Python

## EXPLICAÇÃO

Os tipos de dados fundamentais em Python definem como os valores são armazenados e quais operações são possíveis:

1. **Strings (`str`):** Dados de texto delimitados por aspas simples (`'`) ou duplas (`"`). São iteráveis e suportam acesso por índice e fatiamento (*slicing*).
2. **Números:**
    * **Inteiros (`int`):** Números sem parte fracionária.
    * **Ponto Flutuante (`float`):** Números decimais (usam ponto `.` como separador).
    * **Complexos (`complex`):** Números com parte imaginária `j`.
3. **Booleanos (`bool`):** Valores lógicos `True` ou `False`. São subtipos de inteiros (True = 1, False = 0).
4. **None:** Representa a ausência de valor.

**Conversão (Casting):** É possível forçar a conversão de tipos usando funções como `int()`, `float()` e `str()`.

## EXEMPLO PRÁTICO

```python
# Strings e Slicing
linguagem = "Python"
print(linguagem[0])    # 'P'
print(linguagem[::-1]) # 'nohtyP' (Invertida)

# Números (Escrita científica)
velocidade_luz = 3e8   # 300000000.0 (float)
planck = 6.626e-34

# Booleanos em aritmética
print(True + True)     # 2

# Verificação de Tipo
print(type(10))        # <class 'int'>
print(type(10.5))      # <class 'float'>

# Uso do None
resultado = None
if resultado is None:
    print("Sem valor atribuído")
```
