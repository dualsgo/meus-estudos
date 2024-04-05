# Exercício Python #087 - Mais sobre Matriz em Python
# Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

from random import randint
matriz = [[randint(0, 9) for i in range(3)] for i in range(3)]

pares = coluna = 0
maior = max(matriz[1])
for linha in matriz:
    print(*[f'[{valor:^3}]' for valor in linha], sep='', end='\n')
    for i, valor in enumerate(linha):
        pares += valor if valor % 2 == 0 else 0
        if i == 2:  # Se for a terceira coluna
            coluna += valor


print(f'A soma dos valores pares é {pares}')
print(f'A soma dos valores da terceira coluna é {coluna}')
print(f'O maior valor da segunda linha é {maior}')