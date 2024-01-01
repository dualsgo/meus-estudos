# Exercício Python #090 - Dicionário em Python - Aula 00 até 19 - Mundo 3
# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

boletim = []

while True:
    aluno = {'nome': str(input('Digite o nome do aluno: ')), 'media': float(input(f'Média do aluno: '))}

    if aluno['media'] < 5:
        aluno['situacao'] = '\033[1;31mREPROVADO\033[m'
    elif aluno['media'] < 7:
        aluno['situacao'] = '\033[1;33mEM RECUPERAÇÃO\033[m'
    else:
        aluno['situacao'] = '\033[1;32mAPROVADO\033[m'

    boletim.append(aluno.copy())

    continuar = str(input('Continuar? S/N ')).strip().upper()
    if continuar not in 'SN':
        continuar = str(input('Continuar? S/N ')).strip().upper()
    else:
        if continuar == 'S':
            print('Prosseguindo...')
        elif continuar == 'N':
            print('Encerrando...')
            break

for i, aluno in enumerate(boletim):
    print(f"Aluno {aluno['nome']} teve a média {aluno['media']} e está {aluno['situacao']}.")