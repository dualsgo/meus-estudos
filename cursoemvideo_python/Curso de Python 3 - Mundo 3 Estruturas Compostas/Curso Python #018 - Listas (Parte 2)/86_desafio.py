# Exercício Python #086 - Matriz em Python - Aula 00 até 18 - Mundo 3
# Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

from random import randint
matriz = [[], [], []]

for linha in range(3):
    for coluna in range(3):
        numero = randint(0, 99)
        print(f'Digite o valor da posição [{linha}][{coluna}] - {numero}')
        matriz[linha].append(numero)

for linha in range(3):
    for coluna in range(3):
        print(f'[ {matriz[linha][coluna]:2} ] ', end='')
    print()

# Resumida

matriz = [[randint(0, 9) for i in range(3)] for i in range(3)]
for linha in matriz:
    print(*[f'[{valor:^3}]' for valor in linha], sep='', end='\n')

# Versão atual

matriz = [[randint(0, 9) for valor in range(3)] for linha in range(3)]
for linha in matriz:
	for valor in linha:
		print(f'[{valor:^3}]', end=' ')
	print('')