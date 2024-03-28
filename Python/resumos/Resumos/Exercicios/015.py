# Exercício Python #015 - Aluguel de Carros
# Exercício Python 015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

while True:

	try:
		dias_utilizando = int(input('Quantidade de dias alugado: '))
		km_percorrido = float(input('Quantidade de Km percorrido: '))

	except ValueError:
		print('Valores não válidos!')

	else:

		valor_diaria = dias_utilizando * 60
		valor_km = km_percorrido * .15
		preco_total = valor_diaria + valor_km

		print(
			f'{'-' * 30}\n'
			f'{'Km percorrido:':<15}{km_percorrido:>15}\n'
			f'{'Valor km:':<15}{'R$':>5}{valor_km:>10}\n'
			f'{'-'*30}\n'		
			f'{'Dias Alugado:':<15}{dias_utilizando:>15}\n'
			f'{'Valor:':<15}{'R$':>5}{valor_diaria:>10.2f}\n'
			f'{'-'*30}\n'
			f'{'Total:':<15}{'R$':>5}{preco_total:>10.2f}\n'
			f'{'-'*30}')

		break