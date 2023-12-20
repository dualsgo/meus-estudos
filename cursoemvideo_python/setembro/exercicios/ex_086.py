"""Desafio 086 -  (Aula 01 a 18): Crie um programa que crie uma matriz de dimensão de 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela com a formatação correta.
[1] [2] [3]
[4] [5] [6]
[7] [8] [9]
"""
from random import randint
from time import sleep
matriz = []
for l in range(3):
    linha = []
    for c in range(3):
        print(f'O número sorteado para a coluna [{c}] linha [{l}] é: ', end='')
        numero = randint(0, 99)
        print(numero)
        sleep(0.5)
        linha.append(numero)
    matriz.append(linha)

print('A MATRIZ 3X3 É')

for linha in matriz:
    # Loop para percorrer os elementos de cada linha
    for elemento in linha:
        print(f'[{elemento:2}]', end=' ')
    print()  # Pula para a próxima linha após imprimir os elementos da linha


