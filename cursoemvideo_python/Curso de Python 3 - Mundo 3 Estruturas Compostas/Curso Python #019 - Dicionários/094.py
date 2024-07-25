# Exercício Python #094 - Unindo dicionários e listas
# Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

pessoas = dict()
x = 0

while True:
	dados = list()
	pessoa = dict()

	pessoa['nome'] = input('Nome: ').strip().title()
	dados.append(pessoa['nome'])

	pessoa['idade'] = input('Idade: ')
	dados.append(pessoa['idade'])

	pessoa['gênero'] = input('Masculino ou Feminino: ').strip().title()
	dados.append(pessoa['gênero'])

	x += 1
	pessoas[f'{x}'] = dados

	continuar = ''
	while continuar not in ('S', 'N'):
		continuar = input('Outra pessoa? S/N: ').strip().upper()

	if continuar == 'N':
		print('Encerrando...')
		break

for chave, valor in pessoas.items():
	print(f'Pessoa {chave}')
	print(f'Nome: {valor[0]}')
	print(f'Idade: {valor[1]}')
	print(f'Gênero: {valor[2]}')