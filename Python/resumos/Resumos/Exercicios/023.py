# Exercício Python #023 - Separando dígitos de um número
# Exercício Python 023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados

while True:
	try:
		numero = int(input('Digite um valor: '))
	except ValueError:
		print('Apenas valores numéricos!')
	else:
		milhar = numero // 1000 % 10
		centena = numero // 100 % 10
		dezena = numero // 10 % 10
		unidade = numero % 10

		print(f'{'-' * 23}')
		print(f'{'M':^5}|{'C':^5}|{'D':^5}|{'U':^5}')
		print(f'{'-' * 23}')
		print(f'{milhar:^5}|{centena:^5}|{dezena:^5}|{unidade:^5}')
		print(f'{'-' * 23}')
		break