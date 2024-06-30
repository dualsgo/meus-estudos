# Exercício Python #010 - Conversor de Moedas
# Exercício Python 010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

while True:
	try:
		carteira = float(input('Digite o valor que possui: R$ '))
		print(f'{'REAL':<8}{'BRL':^3}{carteira:>8.2f}')
		print(f'{'DÓLAR':<8}{'USD':^3}{carteira / 5:>8.2f}')
		print(f'{'EURO':<8}{'EUR':^3}{carteira / 5.4:>8.2f}')
		print(f'{'YUAN':<8}{'CNY':^3}{carteira / .69:>8.2f}')
		print(f'{'IENE':<8}{'JPY':^3}{carteira / .033:>8.2f}')
		break
	except ValueError:
		print(f'Valor digitado não é válido!')
	# 1 Dólar (EUA) =
	# 5 Real Brasileiro
	# Última atualização · 24 de março às 18:24 UTC
