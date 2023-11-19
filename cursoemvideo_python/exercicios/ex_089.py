"""Desafio 089 -  (Aula 01 a 18): Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente """
boletim = []

# Loop principal para adicionar alunos ao boletim
while True:
    alunos = []
    aluno = str(input('Digite o nome do aluno: ')).title().strip()
    alunos.append(aluno)
    notas = []

    # Loop para adicionar as notas de cada bimestre
    for bimestre in range(4):
        pontos = float(input(f'Digite a nota do {bimestre + 1}º bimestre: '))

        # Verifica se a nota está dentro do intervalo válido (entre 0 e 10)
        if 0 < pontos <= 10:
            notas.append(pontos)
        else:
            print('Valor não permitido')
            pontos = float(input('Digite novamente um valor válido: '))

    # Adiciona a lista de notas à lista de alunos
    alunos.append(notas[:])

    # Adiciona a lista de alunos ao boletim
    boletim.append(alunos[:])

    # Pergunta se deseja adicionar mais alunos
    resposta = input('Deseja adicionar mais alunos? (S/N)').upper().strip()

    # Verifica a resposta para decidir se continua ou encerra o programa
    if resposta == 'N':
        print('Encerrando o programa!')
        break
    elif resposta not in 'SN':
        print('Resposta inválida!')
        resposta = input('Deseja adicionar mais alunos? (S/N)').upper().strip()

# Exibe as médias e situações de cada aluno no boletim
for aluno in boletim:
    nome_aluno = aluno[0]
    medias = sum(aluno[1]) / 4

    print(f'A média de {nome_aluno} é {medias}.')

    # Verifica a situação do aluno com base na média
    if medias <= 4.9:
        print('Aluno não aprovado!')
    elif medias <= 5.9:
        print('Aluno em recuperação!')
    else:
        print('Aluno aprovado!')

# Solicita o nome do aluno para ver o boletim individual
nome = str(input('Digite o nome do aluno que deseja ver o boletim: ')).strip().title()

# Busca o aluno no boletim
aluno_encontrado = None
for a in boletim:
    if a[0] == nome:
        aluno_encontrado = a
        break

# Exibe o boletim individual do aluno, se encontrado
if aluno_encontrado:
    notas_individuais = aluno_encontrado[1]
    print(f'O aluno {nome} teve as seguintes notas:')
    for i, nota in enumerate(notas_individuais, start=1):
        print(f'{i}º Bimestre: {nota}')
else:
    print(f'Não encontrei o aluno {nome}.')
