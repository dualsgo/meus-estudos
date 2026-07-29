# Operadores em Python

## EXPLICAÇÃO

Operadores são ferramentas para realizar cálculos e tomar decisões lógicas.

1. **Aritméticos:**
    * `+`, `-`, `*`, `/` (Divisão sempre resulta em `float`).
    * `**` (Potência).
    * `//` (Divisão inteira - arredonda para baixo).
    * `%` (Módulo - resto da divisão).
2. **Atribuição Composta:** Une operação e atribuição (ex: `x += 1`).
3. **Precedência:** Python segue ordem matemática (Unários > Potência > Mult/Div > Soma/Sub). Parênteses `()` alteram essa ordem.

**Regra de Ouro:** O arredondamento da divisão inteira (`//`) sempre vai em direção ao valor inteiro **menor** (importante para números negativos).

## EXEMPLO PRÁTICO

```python
# Divisão Inteira e Módulo
print(14 // 4)  # 3 (Quociente)
print(14 % 4)   # 2 (Resto)

# Divisão com Negativos
print(-6 // 4)  # -2 (Arredonda para o menor)

# Atribuição Composta
n = 10
n *= 2          # n = n * 2 -> 20
n -= 5          # n = n - 5 -> 15

# Precedência e Parênteses
resultado = (10 + 2) * 3  # 36
resultado_sem = 10 + 2 * 3 # 16

# Exponenciação
print(2 ** 3)   # 8
```
