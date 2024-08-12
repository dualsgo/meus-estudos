# Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def valor_válido(mensagem):
	while True:
		try:
			return int(input(mensagem))
		except ValueError:
			print('Valor inválido para essa operação!')


def maior(valores):
	if len(valores) == 1:
		print(f'Apenas o valor {valores[0]} foi digitado!')
	else:
		print('Os valores digitados foram: ')
		for i, v in enumerate(lista, 1):
			print(v, end=', ' if i < len(lista) else '.\n')
		print(f'O maior valor é {max(valores)}!')


def continuar():
	while True:
		entrada = input('Deseja continuar?\n[S] Sim\n[N] Não\nSua resposta: ').strip().upper()
		if entrada in "SN":
			return entrada


lista = list()
while True:
	lista.append(valor_válido('Digite um valor: '))
	if continuar() == 'N':
		maior(lista)
		break