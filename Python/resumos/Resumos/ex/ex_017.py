# Exercício Python 017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.


def comprimento(mensagem):
	while True:
		try:
			return float(input(mensagem))
		except ValueError:
			print('Valor inválido!')


oposto = comprimento('Comprimento do cateto oposto: ')
adjacente = comprimento('Comprimento do cateto adjacente: ')
hipotenusa = (oposto ** 2 + adjacente ** 2) ** .5

print(f'{'Cateto oposto:':<20}{oposto:>10.3g}\n{'Cateto adjacente:':<20}{adjacente:>10.3g}\n{'Hipotenusa:':<20}{hipotenusa:>10.3g}')