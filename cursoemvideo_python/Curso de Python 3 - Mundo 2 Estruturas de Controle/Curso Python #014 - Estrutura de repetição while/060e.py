# Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.
#
# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

while True:
	try:
		número = int(input('Digite um valor para verificar seu fatorial: '))
		fatorial = 1
		print(f'{número}! = ', end='')

		for valor in range(número, 0, -1):
			print(valor, end=' X ' if valor > 1 else ' = ')
			fatorial *= valor

		print(fatorial)
		break
	except ValueError:
		print('Valor inválido')