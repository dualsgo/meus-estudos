# Exercício Python 019: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

from random import choice

print(f'O aluno escolhido foi: \033[1;32m{choice([input(f'{i}º aluno: ').strip().title() for i in range(1, 5)])}\033[m')