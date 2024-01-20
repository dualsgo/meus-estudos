# Exercício Python #020 - Sorteando uma ordem na lista - Aula 00 até 08 - Mundo 1
# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle
from emoji import emojize
from time import sleep

# Tarefa 1: Ler o nome dos quatro alunos.
alunos = [
    str(input(emojize(':estudante: Digite o nome do primeiro aluno: ', language='pt'))).strip().title(),
    str(input(emojize(':estudante: Digite o nome do segundo aluno: ', language='pt'))).strip().title(),
    str(input(emojize(':estudante: Digite o nome do terceiro aluno: ', language='pt'))).strip().title(),
    str(input(emojize(':estudante: Digite o nome do quarto aluno: ', language='pt'))).strip().title()
]

# Embaralhar a ordem dos alunos
shuffle(alunos)

# Adicionar um atraso para criar suspense
sleep(.5)

# Tarefa 2: Exiba a ordem do sorteio.
print(emojize(f'A ordem do sorteio é a seguinte: :cone_de_festa:\n {', '.join(alunos)}.', language='pt'))