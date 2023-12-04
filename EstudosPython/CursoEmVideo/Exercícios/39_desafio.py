# Exercício Python #039 - Alistamento Militar
#  Faça um programa que leia o ano de nascimento de um jovem e informe, conforme a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
# Tarefa 1: Ler o ano de nascimento
ano_nascimento = int(input('Digite o seu ano de nascimento: '))
ano_atual = date.today().year

# Tarefa 2: Verificar as condições de alistamento
idade = ano_atual - ano_nascimento
print(idade)
idade_alistamento = 18
ano_alistamento = ano_nascimento + idade_alistamento

# Tarefa 3: Mostrar o tempo que falta ou se passou do prazo
if idade < idade_alistamento:
    print('Ainda não está na hora')
    print(f'Seu alistamento deverá ser feito em {ano_alistamento}. Faltam {ano_alistamento - ano_atual} anos.')
elif idade > idade_alistamento:
    print('Passou da hora')
    print(f'Seu alistamento deveria ter sido feito em {ano_alistamento}. Passaram-se {ano_atual - ano_alistamento} anos.')

else:
    print('Aliste-se')

