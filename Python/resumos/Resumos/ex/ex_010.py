# Exercício Python 010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

# 1 USD = 5,56 BRL
# 1 EUR = 6,05 BRL

from emoji import emojize

while True:
	try:
		BRL = float(input(emojize(':cifrão: Digite o valor em BRL: ', language='pt')))
		USD = BRL / 5.56
		EUR = BRL / 6.05

		print(emojize(f'''Na cotação atual (03/07/2024):
:dinheiro_voando: {BRL:.2f} BRL
:nota_de_dólar: {USD:.2f} USD
:nota_de_euro: {EUR:.2f} EUR''', language='pt'))
		break

	except ValueError:
		print(f'Valor inválido!')

# Fazer um conversor com menu