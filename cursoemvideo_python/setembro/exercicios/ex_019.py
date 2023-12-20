"""Desafio 019 - Aluguel de Carros (Aula 01 a 08): Um professor quer sortear um dos seus alunos para apagar o quadro. Faça isso lendo o nome deles e escrevendo na tela o nome do aluno escolhido.
"""

# Passo 1: Importar a biblioteca random
from random import choice

# Passo 2: Entrar com os nomes dos alunos - Armazenaremos os nomes dos alunos em uma variável cada
primeiro_aluno = input('Qual é o nome do primeiro aluno? ')
segundo_aluno = input('E do segundo? ')
terceiro_aluno = input('Agora é a vez do terceiro: ')
quarto_aluno = input('Por último mas não menos importante, o quarto aluno: ')

# Criamos uma variável para receber a lista de alunos
lista_de_alunos = [primeiro_aluno, segundo_aluno, terceiro_aluno, quarto_aluno]

# Exibir o aluno selecionado com o método random.choice() que escolhe um entre os presentes na lista.
print(f"""
Uni, duni, duni, tê. Salamê minguê.
Entre \033[1;32m{primeiro_aluno}\033[m, \033[1;32m{segundo_aluno}, \033[1;32m{terceiro_aluno}\033[m e \033[1;32m{quarto_aluno}\033[m
O aluno escolhido foi você, \033[1;32m{choice(lista_de_alunos)}\033[m.""")

# Ordem alfabética - sort()
lista_de_alunos.sort()
print(f"Em ordem alfabética: {', '.join(lista_de_alunos)}")
