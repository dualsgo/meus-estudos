# Exercício Python #019 - Sorteando um item na lista - Aula 00 até 08 - Mundo 1
# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

from random import choice
from emoji import emojize
from time import sleep
# Tarefa 1: Ler o nome dos alunos
alunos = [str(input(emojize(':estudante: Digite o nome do primeiro aluno: ', language='pt'))), str(input(emojize(':estudante: Digite o nome do segundo aluno: ', language='pt'))), str(input(emojize(':estudante: Digite o nome do terceiro aluno: ', language='pt'))), str(input(emojize(':estudante: Digite o nome do quarto aluno: ', language='pt')))]

# Tarefa 2: Exibir o nome do aluno escolhido.
escolhido = choice(alunos)
print('O aluno escolhido foi: ', end='')
sleep(1)
print(emojize(f'{escolhido} :professora:', language='pt'))
