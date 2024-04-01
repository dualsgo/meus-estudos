# Exercício Python #055 - Maior e menor da sequência
# Exercício Python 055: Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

import random
pesos = [round(random.uniform(60.0, 180.0), 1) for h in range(5)]
for pessoa, peso in enumerate(pesos, 1):
	print(f'Pessoa {pessoa}: {peso:>8}kg')