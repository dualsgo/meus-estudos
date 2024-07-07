# Exercício Python #011 - Pintando Parede
# Exercício Python 011: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

while True:
	try:
		largura = float(input('Digite a largura da parede: '))
		altura = float(input('Digite a altura da parede: '))
		area = largura * altura
		litro_rende = area / 2
		print(
			f'{'Largura':<10}{largura:>10.2f}{'m':<2}\n'
			f'{'Altura':<10}{altura:>10.2f}{'m':<2}\n'
			f'{'Área':<10}{area:>10.2f}{'m²':>2}\n'
			f'{'Tinta':<10}{litro_rende:>10.2f}{'l':<2}')
		break
	except ValueError:
		print(f'Você digitou um valor inválido!')