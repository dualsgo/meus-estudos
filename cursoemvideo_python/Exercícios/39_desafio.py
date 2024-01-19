# Exercício Python #039 - Alistamento Militar - Aula 00 até 12 - Mundo 2
#  Faça um programa que leia o ano de nascimento de um jovem e informe, conforme a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
# Tarefa 1: Ler o ano de nascimento
ano_nascimento = int(input('Digite o seu ano de nascimento: '))
ano_atual = date.today().year

# Tarefa 2: Verificar as condições de alistamento
idade = ano_atual - ano_nascimento
print(f'Você nasceu em {ano_nascimento} e tem atualmente, em {ano_atual}, \033[1;32m{idade} anos de idade\033[m.')
idade_alistamento = 18
ano_alistamento = ano_nascimento + idade_alistamento

# Tarefa 3: Mostrar o tempo que falta ou se passou do prazo
if idade < idade_alistamento:
    print(f'Seu alistamento deverá ser feito em \033[1m{ano_alistamento}\033[m.')
    print(f'Faltam \033[1m{ano_alistamento - ano_atual} anos\033[m.')
    print('STATUS: \033[1;33mAinda não está na hora de se alistar\033[m.')

elif idade > idade_alistamento:
    print(f'Seu alistamento deveria ter sido feito em \033[1;31m{ano_alistamento}\033[m.')
    print(f'Passaram-se \033[1;31m{ano_atual - ano_alistamento} anos\033[m.')
    print('STATUS: \033[1;31mPassou da hora de se alistar\033[m.')

else:
    print('STATUS: \033[1;32mAliste-se já!\033[m')

# EXTRA - VERIFICAR SE É HOMEM OU MULHER