# Exercício Python 011: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

def medida(mensagem):
	while True:
		try:
			return float(input(mensagem))
		except ValueError:
			print('O valor fornecido não é válido para essa operação.')

largura = medida('Largura: ')
altura = medida('Altura: ')
metro_quadrado = largura * altura
rendimento = metro_quadrado / 2

print(f'''
{'Largura:':<10}{largura:>5.2f}m
{'Altura:':<10}{altura:>5.2f}m
{'-' * 16}
{'Metro²':<10}{metro_quadrado:>5.2f}
{'Tinta:'}{rendimento:>6.1f}L''')