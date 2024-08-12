# Exercício Python #096 - Função que calcula área - Aula 00 até 20 - Mundo 3
# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.


def valor(mensagem):
	while True:
		try:
			return float(input(mensagem))
		except ValueError:
			print('Valor inválido para essa operação!')


largura = valor('Digite a largura do terreno: ')
comprimento = valor('Digite o comprimento do terreno: ')
área_do_terreno = largura * comprimento

print(f'{f'LARGURA (m)':^15}{f'COMPRIMENTO (m)':^15}{f'ÁREA (m²)':^15}')
print(f'{largura:^15}{comprimento:^15}{área_do_terreno:^15}')