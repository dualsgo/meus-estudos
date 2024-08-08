# Exercício Python #090 - Dicionário em Python - Aula 00 até 19 - Mundo 3
# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.


def obter_nota(mensagem):
	while True:
		try:
			média = float(input(mensagem))
			if 0 <= média <= 10:
				return média
			else:
				print('Entre 0 e 10')
		except ValueError:
			print('Tente novamente')


def obter_nome(mensagem):
	while True:
		entrada = input(mensagem).strip().title()
		condição = entrada.replace(' ', '').isalpha()

		while not condição:
			print('Somente caracteres alfabéticos')
			break

		if condição:
			return entrada


boletim = []

while True:
	aluno = dict(nome=obter_nome('Digite o nome do aluno: '), media=obter_nota('Digite a nota do aluno: '))

	aluno['situação'] = '\033[1;31mREPROVADO\033[m' if aluno['media'] < 5 else "\033[1;33mEM RECUPERAÇÃO\033[m" if aluno['media'] < 7 else '\033[1;32mAPROVADO\033[m'

	boletim.append(aluno.copy())

	continuar = str(input('Continuar? S/N ')).strip().upper()
	if continuar not in 'SN':
		continuar = str(input('Continuar? S/N ')).strip().upper()
	else:
		if continuar == 'S':
			print('Prosseguindo...')
		elif continuar == 'N':
			print('Encerrando...')
			break

for i, aluno in enumerate(boletim):
	print(f"Aluno {aluno['nome']} teve a média {aluno['media']} e está {aluno['situação']}.")