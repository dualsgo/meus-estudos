# Exercício Python #092 - Cadastro de Trabalhador em Python - Aula 00 até 19 - Mundo 3
# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime
from random import randint

dados = []
ano_atual = datetime.now().year

while True:
    pessoa = {}  # Cria um novo dicionário para cada pessoa

    pessoa['nome'] = str(input('Nome: '))
    pessoa['nascimento'] = int(input('Ano de nascimento: '))
    pessoa['idade'] = ano_atual - pessoa['nascimento']

    carteira = str(input('Possui CTPS: S/N ')).strip().upper()

    while carteira not in 'SN':
        carteira = str(input('Resposta inválida: S/N ')).strip().upper()

    if carteira == 'S':
        pessoa['ctps'] = randint(1234567, 9999999)
        pessoa['contratacao'] = int(input('Ano de contratação: '))
        pessoa['salario'] = float(input('Salário: R$ '))

    dados.append(pessoa.copy())

    continuar = str(input('Continuar? S/N ')).strip().upper()

    while continuar not in 'SN':
        continuar = str(input('Continuar? S/N ')).strip().upper()

    if continuar == 'N':
        print('Encerrando...')
        break
    elif continuar == 'S':
        print('Prosseguindo...')

for pessoa in dados:
    if 'ctps' in pessoa:  # Verifica se a pessoa tem CTPS
        print(
            f"{pessoa['nome']}, nasceu em {pessoa['nascimento']} possui {pessoa['idade']} anos, porta a CTPS nº {pessoa['ctps']}. Trabalha desde {pessoa['contratacao']} com salário de R$ {pessoa['salario']:.2f} e terá que contribuir mais {35 - (ano_atual - pessoa['contratacao'])} anos para se aposentar.")
    else:
        print(
            f"{pessoa['nome']}, nascido em {pessoa['nascimento']} possui {pessoa['idade']} anos e ainda não é contribuinte.")