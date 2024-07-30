# Exercício Python #070 - Estatísticas em produtos - Aula 00 até 15 - Mundo 2
#  Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

cadastros = quantidade_produtos_mais_mil = valor_total = valor_produto_mais_mil = 0
descrição_mais_barato = descrição_produto_mais_mil = ''
valor_produto_mais_barato = float('+inf')
def obter_preço(mensagem):
	try:
		return float(input(mensagem))
	except ValueError:
		print('Dados inválidos')


print(f'{'-'*30}')
print(f'{'CADASTRO DE PRODUTOS':^30}')
print(f'{'-'*30}')

while True:
	descrição = input('Descrição do produto: ').strip().upper()
	valor = obter_preço('Valor do produto: R$ ')

	if valor < valor_produto_mais_barato:
		valor_produto_mais_barato = valor
		descrição_mais_barato = descrição

	if valor > 1000:
		quantidade_produtos_mais_mil += 1
		descrição_produto_mais_mil = descrição
		valor_produto_mais_mil = valor
	print('Cadastro realizado com sucesso!')
	print(f'{'Descrição:':<20}{descrição:>25}\n{'Valor:':<20}{f'{'R$':>15}{valor:>10.2f}'}')
	print(f'{'-' * 45}')
	valor_total += valor
	continuar = input('Digite S para continuar ou N para encerrar: S / N').strip().upper()
	while continuar not in ['S', 'N']:
		print('Você escolheu uma opção inválida@!')
		continuar = input('Digite S para continuar ou N para encerrar: S / N').strip().upper()
	print(f'{'-' * 45}')
	if continuar == 'S':
		print('Próximo cadastro: ')

	else:
		print('Encerrando o programa...')
		break

print(f'{'-' * 45}')
print(f'{'VALOR TOTAL':^45}')
print(f'{'-' * 45}')
print(f'{'Valor total:':<30}{f'{'R$':>5}{valor_total:>10.2f}'}')
print(f'{'-' * 45}')
print(f'{'Produtos que custam mais de MIL REAIS:':<40} {quantidade_produtos_mais_mil:>5}')
print(f'{'-' * 45}')
print(f'{'PRODUTO MAIS BARATO':^45}')
print(f'{'Descrição:':<20}{descrição_mais_barato:>25}\n{'Valor:':<20}{f'{'R$':>15}{valor_produto_mais_barato:>10.2f}'}')