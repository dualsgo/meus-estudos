# Exercício Python 004: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

from emoji import emojize

algo = input(emojize(':memorando: Digite algo: ', language='pt'))

try:
	float(algo)
	algo = float(algo) if '.' in algo else int(algo)
except ValueError:
	pass

print(f'"{algo}" é do tipo \033[1;31m{type(algo)}\033[m')