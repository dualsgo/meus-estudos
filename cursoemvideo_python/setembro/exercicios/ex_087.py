"""Desafio 087 -  (Aula 01 a 18): Aprimore o desafio anterior, mostrando no final.
- A soma de todos os valores pares digitados
- A soma dos valores da terceira coluna
- O maior valor da segunda linha
"""
from random import randint
from time import sleep
matriz = []
matriz_pares = []
terceira_coluna = []

for l in range(3):
    linha = []
    for c in range(3):
        print(f'O número sorteado para a coluna [{c}] linha [{l}] é: ', end='')
        numero = randint(0, 99)
        print(numero)
        sleep(0.5)
        linha.append(numero)
        if numero % 2 == 0:
            matriz_pares.append(numero)
        if c == 2:
            terceira_coluna.append(numero)

    matriz.append(linha)

print('A MATRIZ 3X3 É')

for linha in matriz:
    # Loop para percorrer os elementos de cada linha
    for elemento in linha:
        print(f'[{elemento:2}]', end=' ')
    print()  # Pula para a próxima linha após imprimir os elementos da linha

print(f'A soma de todos os valores pares é: {sum(matriz_pares)}.')
print(f'A soma dos valores da terceira coluna é: {sum(terceira_coluna)}.')
print(f'O maior valor da segunda linha é: {max(matriz[1])}.')
