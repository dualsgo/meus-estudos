"""Desafio 039 -  (Aula 01 a 12): Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:

- Se ele ainda vai se alistar ao serviço militar
- Se é a hora de se alistar
- Se já passou do tempo de se alistar

Seu programa também deverá mostrar o tempo que falta ou que já passou para se alistar."""
import datetime
print("""
ALISTAMENTO MILITAR
""")
# Ler o ano de nascimento
print('Digite seu ano de nascimento: ')
ano = int(input(''))

# EXTRA - Coletar ano atual direto do sistema
ano_atual = datetime.datetime.now().year
idade = ano_atual - ano

# Comparar os anos para avaliar as condições
if idade <= 17:
    print(f"""AINDA NÃO É SUA HORA, JOVEM!
Você, nascido no ano de {ano} irá completar {idade} anos em {ano_atual}.
Faltam {18 - idade} anos para você se alistar.""")
elif idade == 18:
    print(f"""PRECISAMOS DE VOCÊ!
Você, nascido no ano de {ano} irá completar {idade} anos em {ano_atual}.
Esse ano de {ano_atual} é o ano em que você deve se alistar!
""")
else:
    print(f"""JÁ PASSOU DA HORA!
Você, nascido no ano de {ano} irá completar {idade} anos em {ano_atual}.
Você deveria ter se alistado a {idade - 18} anos.""")
