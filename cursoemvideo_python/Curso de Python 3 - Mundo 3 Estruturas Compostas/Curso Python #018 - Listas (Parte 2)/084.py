# Exercício Python #084 - Lista composta e análise de dados
# Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

pessoas = []
pessoa = []
nome_pesado = []
nome_leve = []
mais_pesado = float('-inf')
mais_leve = float('inf')

while True:
	pessoa.clear()

	try:
		nome = input('Digite um nome: ')
		pessoa.append(nome)

		peso = float(input('Agora o peso: Kg '))
		pessoa.append(peso)
	except ValueError:
		print(f'Valor inválido!')
		continue

	pessoas.append(pessoa)

	continuar = input('S/N ').strip().upper()
	if continuar == 'S':
		continue
	else:
		break

print(f'Foram cadastradas: {len(pessoas)} pessoas.')

for y, x in enumerate(pessoas):
	if pessoas[x][1] > mais_pesado:
		nome_pesado.append(pessoa[x][0])
	elif pessoas[x][1] < mais_leve:
		nome_leve.append(pessoa[x][0])

print(f'Maior peso: {mais_pesado}Kg - Pessoas: {nome_pesado}')
print(f'Menor peso: {mais_leve}Kg - Pessoas: {nome_leve}')