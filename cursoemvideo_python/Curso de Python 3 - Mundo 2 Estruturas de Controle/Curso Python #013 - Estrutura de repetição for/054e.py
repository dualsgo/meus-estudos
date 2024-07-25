# Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from random import randint
from datetime import date
from time import sleep

ano_atual = date.today().year
maiores = menores = 0
while True:
	try:
		ano_inicial = int(input('Digite o início do intervalo: '))
		print(f'{'-'*40}')
		print(f'{'PESSOA':^10}{'ANO NASC':^10}{'IDADE':^10}{'MAIOR?':^10}')
		print(f'{'-'*40}')
		for pessoa in range(1,8):
			sleep(1)
			ano_nascimento = randint(ano_inicial, ano_atual)
			idade = ano_atual - ano_nascimento
			maioridade = 'SIM' if idade >= 18 else 'NÃO'

			if idade >= 18:
				print(f'\033[1;32m{pessoa:^10}{ano_nascimento:^10}{idade:^10}{maioridade:^10}\033[1;32m')
				maiores += 1
			else:
				print(f'\033[1;31m{pessoa:^10}{ano_nascimento:^10}{idade:^10}{maioridade:^10}\033[m')
				menores += 1
		print(f'{'-'*40}')
		print(f'Total de maiores de idade: {maiores}')
		print(f'Total de menores de idade: {menores}')
		print(f'{'-'*40}')

		break
	except ValueError:
		print('ERRO')

	"""from datetime import date
ano_atual = date.today().year
ano_nascimento = [int(input(f'Ano de nascimento da {i}ª pessoa: ')) for i, v in enumerate(range(7), 1)]
maiores = [i for i in ano_nascimento if ano_atual - i > 17]
print(f'Ao todos temos {len(maiores)} maiores de idade e {len(ano_nascimento) - len(maiores)} menores de idade!')"""