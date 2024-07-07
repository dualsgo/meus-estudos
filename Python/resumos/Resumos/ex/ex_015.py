# Exercício Python 015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

from emoji import emojize


def obter_valores(mensagem):
	while True:
		try:
			return float(input(mensagem))
		except ValueError:
			print(emojize(':xis: Tente novamente. :xis:', language='pt'))


def total_a_pagar(km, dias):
	valor_por_km = .15
	valor_diária = 60

	total_km = km * valor_por_km
	total_diária = dias * valor_diária

	total = total_km + total_diária

	print(
		f'{"Km percorrido:":<20}{km:>10.1f}\n'
		f'{"Valor (Km):":<20}\033[1;32mR${total_km:>8.2f}\033[m\n{"-" * 30}\n'
		f'{"Dias alugado:":<20}{int(dias):>10}\n'
		f'{"Valor (Dias)":<20}\033[1;32mR${total_diária:>8.2f}\033[m\n{"-" * 30}\n'
		f'{"Total a pagar":<20}\033[1;31mR${total:>8.2f}\033[m')


km_percorrido = obter_valores(emojize(':carro: Quantidade de KM percorridos: ', language='pt'))
dias_alugado = obter_valores(emojize(':calendário: Quantidade de DIAS alugados: ', language='pt'))
total_a_pagar(km_percorrido, dias_alugado)