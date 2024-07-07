# Exercício Python #017 - Catetos e Hipotenusa
# Exercício Python 017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

while True:
	try:
		oposto = float(input('Digite o valor do cateto oposto: '))
		adjacente = float(input('Digite o valor do cateto adjacente: '))
	except ValueError:
		print('Valor fornecido inválido! Tente novamente.')
	else:
		hipotenusa = (oposto ** 2 + adjacente ** 2) ** .5

	print(f'{'Cateto oposto':<16}{oposto:>8.2f}')
	print(f'{'Cateto adjacente':<16}{adjacente:>8.2f}')
	print(f'{'-' * 24}')
	print(f'{'Hipotenusa':<16}{hipotenusa:>8.2f}')
	break