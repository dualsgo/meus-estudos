# Exercício Python #044 - Gerenciador de Pagamentos
# Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros
from time import sleep

while True:
	try:
		valor_produto = float(input('Valor do produto: R$ '))
	except ValueError:
		print('ERROR')
	else:
		while True:
			try:

				pagamento = int(input(
					"Forma de pagamento:\n[1] Dinheiro\n[2] PIX\n[3] Cartão de débito\n[4] Cartão de crédito"))
			except ValueError:
				print('Valor inválido!')
				sleep(1)
			else:
				if pagamento in range(1, 5):
					break
				else:
					print('Opção inválida')
					sleep(1)

		desconto = 0
		per = 0

		if pagamento == 1:
			desconto = 0.1
			per = 10
			print(f'Pagamento em dinheiro')
		elif pagamento == 2:
			desconto = 0.05
			per = 5
			print(f'Pagamento em PIX')
		elif pagamento == 3:
			desconto = 0.05
			per = 5
			print(f'Pagamento com cartão de débito')

			print(f'{'Valor do produto':<20}{'R$':>5}{valor_produto:>10.2f}')
			print(f'{'Desconto':<20}{f'{per}%':>5}{valor_produto * desconto:>10.2f}')
			print(f'{'Valor final':<20}{'R$':>5}{valor_produto - (valor_produto*desconto):>10.2f}')

		elif pagamento == 4:
			print(f'Pagamento com cartão de crédito')
			while True:
				try:
					parcelamento = int(input('Quantidade de parcelas: '))
				except ValueError:
					print('Valor inválido!')
					sleep(1)
				else:
					if parcelamento == 1:
						print(f'Crédito à vista')
						print(f'{'Valor do produto':<15}{'R$':>2}{valor_produto:>10.2f}')

					elif parcelamento <= 12:
						print(f'Crédito parcelado em {parcelamento} vezes')
						if parcelamento == 2:
							print(f'{'Valor do produto':<20}{'R$':>5}{valor_produto:>10.2f}')
							print(f'{'Parcelas':<20}{f'{parcelamento}x':>5}{valor_produto/parcelamento:>10.2f}')
							print(f'{'Valor final':<20}{'R$':>5}{valor_produto:>10.2f}')


						else:
							juros = .20
							valor_com_juros = valor_produto+ (valor_produto*juros)
							print(f'{'Valor do produto':<20}{'R$':>5}{valor_produto:>10.2f}')
							print(f'{'Valor dos Juros':<20}{'R$':>5}{valor_produto*juros:>10.2f}')
							print(f'{'Parcelas':<20}{f'{parcelamento}x':>5}{valor_com_juros/parcelamento:>10.2f}')
							print(f'{'Valor final':<20}{'R$':>5}{valor_com_juros:>10.2f}')
					break

		break