# Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

ano_atual = date.today().year

while True:
	try:
		ano_nascimento = int(input('Digite o seu ano de nascimento: '))
		idade = ano_atual - ano_nascimento
		ano_alsitamento = ano_nascimento + 18

		if ano_alsitamento < ano_atual:
			print(f'Você completou 18 anos em {ano_alsitamento} deveria ter se apresentado ao serviço militar obrigatório!')
		elif ano_alsitamento > ano_atual:
			print(f'Você ainda tem {idade} anos. Só deverá se apresentar daqui a {ano_alsitamento - ano_atual} anos, em {ano_alsitamento}.')
		else:
			print(f'Você que completa 18 anos em {ano_atual} deve se apresentar ao serviço militar obrigatório!')
		break
	except ValueError:
		print('Você está utilizando um tipo de dao inválido para essa operação!')