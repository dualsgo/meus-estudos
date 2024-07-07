# Exercício Python #016 - Quebrando um número
# Exercício Python 016: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

# Ex: Digite um número: 6.127
# O número 6.127 tem a parte Inteira 6.

while True:
	try:
		numero = float(input('Digite um número qualquer: '))
	except ValueError:
		print(f'O valor não é válido para essa operação!')
	else:

		parte_fracionaria = numero % 1
		parte_inteira = numero // 1


		print(
			f'{'Número digitado:':<20}{numero:>10.4f}\n'
			f'{'Parte inteira:':<20}{parte_inteira:^10.0f}\n'
			f'{'Parte fracionaria:':<20}{parte_fracionaria:>10.4f}'
			)

		break