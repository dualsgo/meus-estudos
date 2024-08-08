# Exercício Python #079 - Valores únicos em uma Lista - Aula 00 até 17 - Mundo 3
# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.


def adicionar_valores(mensagem):
	while True:
		try:
			return int(input(mensagem))
		except ValueError:
			print(f'{'Apenas valores numéricos!':^30}')


lista = []

while True:
	valor = adicionar_valores(f'\033[1;34m{'Digite um valor: ':^30}\033[m')
	if valor not in lista:
		print(f'\033[1;32m{'-' * 30}')
		print(f'{'Valor adicionado!':^30}')
		print(f'{'-' * 30}\033[m')
		lista.append(valor)
	else:
		print(f'\033[1;31m{'-' * 30}')
		print('Valor repetido! Vou desconsidera-lo...')
		print(f'{'-' * 30}\033[m')
	while True:
		continuar = input(f'\033[1m{'Deseja continuar? S/N':^30}\033[m').strip().upper()
		print(f'\033[1;34m{'-' * 30}\033[m')
		if continuar not in 'SN':
			continue
		else:
			break
	if continuar == 'N':
		break

lista.sort()

print(f'Os valores digitados foram: ', end='')
for a, i in enumerate(sorted(lista), 1):
	print(i, end=', ' if a != len(lista) else '.')