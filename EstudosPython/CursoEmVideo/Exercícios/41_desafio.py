# Python Exercício #041 - Classificando Atletas
# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, conforme a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JÚNIOR
# - Até 25 anos: SÊNIOR
# - Acima de 25 anos: MASTER
from datetime import date
# Tarefa 1: Ler o ano de nascimento
ano_nascimento = int(input('Digite seu ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento
# Tarefa 2: Definir as categorias conforme a idade
print('Sua categoria é: ', end='')
if idade < 10:
    print('MIRIM')
elif idade < 15:
    print('INFANTIL')
elif idade < 20:
    print('JÚNIOR')
elif idade < 26:
    print('SÊNIOR')
else:
    print('MASTER')
# Tarefa 3: Mostrar o resultado