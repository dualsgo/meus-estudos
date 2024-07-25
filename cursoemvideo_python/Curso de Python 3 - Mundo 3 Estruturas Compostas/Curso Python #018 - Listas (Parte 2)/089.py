# Exercício Python #089 - Boletim com listas compostas
# Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.


boletim = []

while True:
    try:
        aluno = []  # Cria uma nova lista para cada aluno
        nome = input('Digite o nome do aluno: ').strip().title()
        aluno.append(nome)
        nota_1 = float(input('1º Bimestre: '))
        nota_2 = float(input('2º Bimestre: '))
    except ValueError:
        print(f'Ops... Valores inválidos. Tente novamente.')
        continue

    aluno.append(nota_1)
    aluno.append(nota_2)
    media = (nota_1 + nota_2) / 2
    aluno.append(media)
    boletim.append(aluno)

    continuar = ''
    while continuar not in ('S', 'N'):
        continuar = input('Outro aluno? S/N').strip().upper()

    if continuar == 'S':
        continue
    if continuar == 'N':
        break

print('-' * 46)
print(f'|{"No":^8}|{"Nome":^8}|{"Nota 1":^8}|{"Nota 2":^8}|{"Média":^8}|')
print('-' * 46)

for i, aluno in enumerate(boletim):
    print(f'|{i:^8}|{aluno[0]:^8}|{aluno[1]:^8}|{aluno[2]:^8}|{aluno[3]:^8}|')

print('-' * 46)

while True:
    try:
        escolha = int(input('Verificar informações de qual aluno? '))
    except ValueError:
        print(f'Valor inválido.')
        continue

    if escolha >= len(boletim):
        print(f'Aluno não localizado.')
        continue

    else:
        print('-' * 46)
        print(f'|{"No":^8}|{"Nome":^8}|{"Nota 1":^8}|{"Nota 2":^8}|{"Média":^8}|')
        print(f'|{escolha:^8}|{boletim[escolha][0]:^8}|{boletim[escolha][1]:^8}|{boletim[escolha][2]:^8}|{boletim[escolha][3]:^8}|')
        print('-' * 46)

    continuar = ''
    while continuar not in ('S', 'N'):
        continuar = input('Outro aluno? S/N').strip().upper()

    if continuar == 'S':
        continue
    if continuar == 'N':
        print('Encerrando...')
        break