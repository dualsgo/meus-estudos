# Exercício Python 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

while True:
	try:
		maior = float('-inf')
		menor = float('inf')

		for i in range(3):
			número = int(input('Digite um valor: '))

			if número > maior:
				maior = número
			elif número < menor:
				menor = número

		print(f'O maior é {maior} e o menor é {menor}')
		break

	except ValueError:
		print(f'Valor inválido.')