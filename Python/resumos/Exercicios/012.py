# Exercício Python #012 - Calculando Descontos
# Exercício Python 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

while True:
	try:
		preco = float(input('Digite o valor do produto: R$ '))
		descontar = int(input('Porcentagem de desconto: % '))
	except ValueError:
		print('O valor informado não é válido!')
	except ZeroDivisionError:
		print(f'Divisão por zero não é possível!')
	else:

		print(f'{'Valor original':<15}{'R$':>6}{preco:>10.2f}')
		print(f'{'Desconto':<10}{descontar:^5}{'%':<3}{'R$':>3}{descontar:>10.2f}')
		print(f'{'Valor final':<15}{'R$':>6}{preco - descontar:>10.2f}')
		break