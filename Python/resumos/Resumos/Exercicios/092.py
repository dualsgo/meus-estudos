# Exercício Python #092 - Cadastro de Trabalhador em Python
# Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime

atual = datetime.today().year
informacoes = dict()

informacoes['nome'] = input('Digite o nome: ').strip().title()
informacoes['nascimento'] = int(input('Digite o ano de nascimento: '))
informacoes['idade'] = atual - informacoes['nascimento']

print(f'Nome: {informacoes["nome"]}')
print(f'Ano de nascimento: {informacoes["nascimento"]}')
print(f'Idade: {informacoes["idade"]} anos')

if informacoes['idade'] >= 18:
    ctps = input('Possui CTPS? S/N: ').strip().upper()
    if ctps == 'S':
        informacoes['CTPS'] = int(input('Digite o número da CTPS: '))
        print(f'CTPS nº: {informacoes["CTPS"]}')
        if informacoes['CTPS']:
            informacoes['ano_contratacao'] = int(input('Digite o ano de contratação: '))
            informacoes['salario'] = float(input('Digite o salário: R$ '))
            informacoes['aposentadoria'] = (informacoes['ano_contratacao'] + 30) - atual

            print(f'Ano de contratação: {informacoes["ano_contratacao"]}')
            print(f'Salário: R$ {informacoes["salario"]:.2f}')
            print(f'Tempo para se aposentar: {informacoes["aposentadoria"]} anos')