"""Desafio 041 - Classificando atletas (Aula 01 a 12): A CNN - Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atléta e mostre sua categoria de acordo com a idade:

- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 20 anos: SÊNIOR
- Acima: MASTER"""
from datetime import date

cor = {
    'red': '\033[1;31m',
    'green': '\033[1;32m',
    'yellow': '\033[1;33m',
    'fecha': '\033[m',
    'destaque': '\033[1m'}

print(f"""
    {cor['destaque']}CNN - CONFEDERAÇÃO NACIONAL DE NATAÇÃO{cor['fecha']}""")

# Ler o ano de nascimento
print('Digite o seu ano de nascimento: ')
ano = int(input(''))

# Calcular a idade
idade = date.today().year - ano

# Categorizar
if idade <= 9: # Até 9 anos
    categoria = 'MIRIM'
elif idade <= 14: # De 9 a 14 anos
    categoria = 'INFANTIL'
elif idade <= 19: # De 15 a 19 anos
    categoria = 'SÊNIOR'
elif idade <= 25: # De 20 até 25 anos
    categoria = 'SÊNIOR'
else: # Com 26 ou mais
    categoria = 'MASTER'
print(f'{cor["destaque"]}Com {idade} anos, sua categoria será:{cor["destaque"]} {cor["green"]}{categoria:^30}{cor["fecha"]}')