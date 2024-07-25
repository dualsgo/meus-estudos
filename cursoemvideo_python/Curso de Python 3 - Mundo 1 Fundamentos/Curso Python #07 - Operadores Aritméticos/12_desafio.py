# Exercício Python #012 - Calculando Descontos - Aula 00 até 07 - Mundo 1
# Faça um algorítimo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

from emoji import emojize
while True:
	try:
		preço = float(input(emojize('Digite o valor do produto: :cifrão: ', language='pt')))
		com_desconto = preço * .95
		print(f'{'Valor do produto:':<20} R${preço:>10.2f}\n{'Com desconto (5%):':<20} R${com_desconto:>10.2f}')
		break
	except ValueError:
		print('Inválido! Tente novamente.')
  
# Versão 2

while True:
	try:
		preco = float(input('Digite o valor do produto: R$ '))
		descontar = float(input('Porcentagem de desconto: % '))
		print(f'{'-'*31}')
		print(f'{'Valor original':<15}{'R$':>6}{preco:>10.2f}')
		print(f'{'Desconto':<10}{descontar/100:^8.1%}{'R$':>3}{preco * (descontar/100):>10.2f}')
		print(f'{'-'*31}')
		print(f'{'Valor final':<15}{'R$':>6}{preco * ((100 - descontar)/100):>10.2f}')
		print(f'{'-'*31}')

		break

	except ValueError:
		print('O valor informado não é válido!')
	except ZeroDivisionError:
		print(f'Divisão por zero não é possível!')