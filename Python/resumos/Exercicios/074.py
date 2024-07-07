# Exercício Python #074 - Maior e menor valores em Tupla
# Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

tupla = tuple(randint(0, 99) for i in range(5))

print(f'Os números são: ', end='')
for i, elemento in enumerate(tupla, 1):
	print(f'{elemento}', end=', ' if i < len(tupla) else '\n')
print(f'O maior valor é {max(tupla)}')
print(f'O menor valor é {min(tupla)}')