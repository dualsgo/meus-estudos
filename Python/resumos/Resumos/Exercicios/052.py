# Exercício Python #052 - Números primos
# Exercício Python 052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

número = int(input('Digite um número: '))
divisores = 0
for divisor in range(1, número+1):
	print(f'\033[1;31m{divisor}\033[m' if número % divisor == 0 else f'{divisor}', end=', ' if divisor < número else '\n')
	divisores += 1 if número % divisor == 0 else 0
print(f'{número}', 'é primo' if divisores == 2 else 'não é primo!')