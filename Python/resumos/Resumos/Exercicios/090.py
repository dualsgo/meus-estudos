# Exercício Python #090 - Dicionário em Python
# Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

aluno = dict()
aluno['nome'] = input('Nome do aluno: ')
aluno['média'] = float(input('Média do aluno: '))
média = aluno['média']
aluno['situação'] = 'aprovado' if média >= 7 else 'em recuperação' if média >= 5 else 'reprovado'

print(f'O aluno {aluno["nome"]} tem a média {aluno["média"]:.1f} e está {aluno["situação"]}.')