# Exercício Python #020 - Sorteando uma ordem na lista
# Exercício Python 020: O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import sample

while True:
	try:
		nomes = [input(f'Digite o nome do {i}º aluno: ').strip().title() for i in range(1, 5)]
	except Exception as e:
		print(f'Ocorreu o erro: {e}')
	else:
		for _, n in enumerate(sample(nomes, 4), 1):
			print(f'{_}º a apresentar: {n}')
		break