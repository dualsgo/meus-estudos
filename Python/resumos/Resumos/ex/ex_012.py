# Exercício Python 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
from emoji import emojize
while True:
	try:
		preço = float(input(emojize('Digite o valor do produto: :cifrão: ', language='pt')))
		com_desconto = preço * .95
		print(f'{'Valor do produto:':<20} R${preço:>10.2f}\n{'Com desconto (5%):':<20} R${com_desconto:>10.2f}')
		break
	except ValueError:
		print('Inválido! Tente novamente.')