# Exercício Python #070 - Estatísticas em produtos
# Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

total = 0
produtos_mil = 0
mais_barato = ''
valor_barato = float('inf')

while True:
	try:
		produto = input('Descrição do produto: ').strip().capitalize()
		valor = int(input('Valor do produto: R$ '))
	except ValueError:
		print(f'Valor digitado inválido!')
		continue

	total += valor
	produtos_mil += 1 if valor > 1000 else 0
	if valor < valor_barato:
		valor_barato = valor
		mais_barato = produto

	try:
		continuar = input('Continuar? S/N').strip().upper()
		if continuar == 'N':
			break
		elif continuar == 'S':
			continue
	except Exception as e:
		print(e)

print(f'Total da compra: R$ {total:.2f}')
print(f'Produtos que custam mais de R$ 1000,00: {produtos_mil} produtos')
print(f'Produto mais barato: {mais_barato} - R$ {valor_barato:.2f}')