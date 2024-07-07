# Exercício Python #019 - Sorteando um item na lista
# Exercício Python 019: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
from random import choice
print(f"O escolhido foi: {choice([input(f'Digite o nome do {i}º aluno: ').strip().title() for i in range(1, 5)])}")

while True:
	try:
		nomes = [input(f'Digite o nome do {i}º aluno: ').strip().title() for i in range(1, 5)]
	except Exception as e:
		print(f'Ocorreu o erro: {e}')
	else:
		escolhido = choice(nomes)
		print(f'Uni, duni, tê...')
		print(f'O aluno escolhido foi você: {escolhido}')
		break