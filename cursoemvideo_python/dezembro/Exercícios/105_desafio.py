# Exercício Python #105 - Analisando e gerando Dicionários - Aula 00 até 21 - Mundo 3
# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)

# Adicione também as docstrings dessa função para consulta pelo desenvolvedor.

def notas(*valores):
    boletim = dict()
    quantidade_notas = soma_notas = maior_nota = menor_nota = 0

    while True:
        boletim['notas'] = float(input('Digite a nota do aluno: '))

        quantidade_notas += 1

        if quantidade_notas == 1:
            maior_nota = menor_nota = boletim['notas']
        elif quantidade_notas > 1:
            if boletim['notas'] > maior_nota:
                maior_nota = boletim['notas']
            if boletim['notas'] < menor_nota:
                menor_nota = boletim['notas']

        soma_notas += boletim['notas']

        continuar = str(input('Continuar S/N')).strip().upper()
        while continuar not in 'SN':
            continuar = str(input('Comando inválido. Tente novamente')).strip().upper()
        if continuar in 'N':
            media_turma = soma_notas / quantidade_notas
            print(f'Foram cadastradas {quantidade_notas} notas.')
            print(f'A maior nota foi {maior_nota} e a menor {menor_nota}')
            print(f'A média da turma é {media_turma:.2f}')
            break
        else:
            print('Seguindo...')


notas()