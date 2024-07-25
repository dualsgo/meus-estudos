# Exercício Python #086 - Matriz em Python
# Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
from random import randint
matriz = [[randint(0, 9) for i in range(3)] for i in range(3)]

for linha in matriz:
    print(*[f'[{valor:^3}]' for valor in linha], sep='', end='\n')