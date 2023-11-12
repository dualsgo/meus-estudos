"""Desafio 039 - Alistamento militar (Aula 01 a 12): Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:

- Se ele ainda vai se alistar ao serviço militar
- Se é a hora de se alistar
- Se já passou do tempo de se alistar

Seu programa também deverá mostrar o tempo que falta ou que já passou para se alistar."""
from datetime import date

# Cores
cor = {
    'red': '\033[1;31m',
    'green': '\033[1;32m',
    'yellow': '\033[1;33m',
    'fecha': '\033[m',
    'destaque': '\033[1m'}

print(f"""
{cor['destaque']}ALISTAMENTO MILITAR{cor['fecha']}
{date.today().day}/{date.today().month}/{date.today().year}
""")
# Verifica se é homem ou mulher
print("""
Você é homem ou mulher?
[1] Homem
[2] Mulher
""")
sexo = int(input(''))
while sexo == 0 or sexo > 2:
    print(""" OPÇÃO INVÁLIDA!
    Você é homem ou mulher?
    [1] Homem
    [2] Mulher
    """)
    sexo = int(input(''))
if sexo == 2:
    resposta = input('Seu alistamento não é obrigatório! Deseja seguir? S ou N? ')
    if resposta == 'Nn':
        print('OK! Então procure um emprego.')
    else:
        print('Digite seu ano de nascimento: ')
        ano = int(input(''))
elif sexo == 1:
    print('Alistamento obrigatório!')
    # Ler o ano de nascimento
    print('Digite seu ano de nascimento: ')
    ano = int(input(''))
# EXTRA - Coletar ano atual direto do sistema
ano_atual = date.today().year
idade = ano_atual - ano
print(f'Você, nascido no ano de {ano} irá completar {idade} anos em {ano_atual}.')
# Comparar os anos para avaliar as condições
if idade < 18:
    print(f"""{cor['green']}AINDA NÃO É SUA HORA, JOVEM!{cor['fecha']}
{cor['green']}Faltam {18 - idade} anos para você se alistar.{cor['fecha']} Será no ano de {ano + 18}""")
elif idade == 18:
    print(f"""{cor['yellow']}PRECISAMOS DE VOCÊ!{cor['fecha']}
{cor['yellow']}Esse ano de {ano_atual} é o ano em que você deve se alistar{cor['fecha']}!
""")
else:
    print(f"""{cor['red']}JÁ PASSOU DA HORA!{cor['fecha']}
{cor['red']}Você deveria ter se alistado a {idade - 18} anos, no ano de {ano + 18}.{cor['fecha']}""")
