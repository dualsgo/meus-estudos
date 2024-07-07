# Exercício Python 009: Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

from emoji import emojize

while True:
	try:
		número = int(input('Digite o valor que deseja ver a tabuada: '))
		for i in range(1, 11):
			print(emojize(f'{número}:xis:{i:2}:sinal_de_igual:{número * i:2}', language='pt'))
		break
	except ValueError:
		print('O valor digitado não é válido para essa operação!')