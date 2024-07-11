# Exercício Python 020: O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle
turma = [input(f'{i}º aluno: ') for i in range(1, 5)]
shuffle(turma)
print('Ordem: ', end='')
for aluno in turma:
	print(aluno, end=' ')