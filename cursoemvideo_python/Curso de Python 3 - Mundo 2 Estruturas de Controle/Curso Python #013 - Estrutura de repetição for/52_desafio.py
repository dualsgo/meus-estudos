# Exercício Python #052 - Números primos - Aula 00 até 13 - Mundo 2
# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

while True:
	try:
		numero = int(input('Digite um valor: '))
		divisor = 0

		for i in range(1, numero+1):
			if numero % i == 0:
				divisor += 1

				print(f'\033[1;32m{i}\033[m ⮕ ', end='')
			else:
				print(f'\033[1;31m{i}\033[m ⮕ ', end='')

		primo = 'é primo!' if divisor <= 2 else 'não é primo!'
		print(f'O valor {numero} {primo}. Ele possui {divisor} divisores.')

	except ValueError:
		print('Você digitou um valor inválido para essa operação!')