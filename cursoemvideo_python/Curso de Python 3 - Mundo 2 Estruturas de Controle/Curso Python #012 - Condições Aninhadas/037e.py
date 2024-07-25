# Exercício Python 037: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

while True:
	try:
		valor = int(input('Digite um valor: '))
		break
	except ValueError:
		print('Somente números inteiros.')

while True:
	try:
		base = int(input('''Escolha a base:\n[1]Binário\n[2]Octal\n[3]Hexadecimal'''))
		if base == 1:
			print(f'{valor} em binário: {valor:b}')
		elif base == 2:
			print(f'{valor} em octal: {valor:o}')
		elif base == 3:
			print(f'{valor} em hexadecimal: {valor:x}')
		else:
			continue

	except ValueError:
		print('Base inválida!')