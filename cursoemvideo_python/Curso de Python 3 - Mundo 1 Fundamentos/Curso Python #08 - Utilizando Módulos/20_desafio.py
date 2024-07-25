# Exercício Python #020 - Sorteando uma ordem na lista - Aula 00 até 08 - Mundo 1
# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle, sample
from emoji import emojize
from time import sleep

# Versão 1 - Com shuffle

turma = [input(f'{i}º aluno: ') for i in range(1, 5)]
shuffle(turma)
print('Ordem: ', end='')
for aluno in turma:
	print(aluno, end=' ')

# Versão 2 - Com sample

while True:
	try:
		nomes = [input(f'Digite o nome do {i}º aluno: ').strip().title() for i in range(1, 5)]
		for _, n in enumerate(sample(nomes, 4), 1):
			print(f'{_}º a apresentar: {n}')
		break
	except Exception as e:
		print(f'Ocorreu o erro: {e}')