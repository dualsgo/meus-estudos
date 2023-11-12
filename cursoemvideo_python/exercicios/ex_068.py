"""Desafio 068 - Jogo par ou ímpar (Aula 01 a 15): Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
"""
from random import randint

# Inicializa as vitórias e derrotas
vitoria = 0
derrota = 0

# Inicia o loop do jogo
while True:
    # Jogador escolhe PAR ou ÍMPAR
    escolha = input('PAR ou ÍMPAR? ').strip().upper()

    # Validação da escolha do jogador
    while escolha not in ['PAR', 'ÍMPAR']:
        escolha = input('Escolha inválida. Digite apenas PAR ou ÍMPAR: ').strip().upper()

    # Jogador escolhe o valor
    jogador = int(input('Qual é o seu valor? 0 a 10 '))
    # Computador sorteia um valor
    computador = randint(0, 10)
    print(f'Computador jogou {computador}')

    # Calcula a soma dos valores para verificar se é PAR ou ÍMPAR
    par_impar = jogador + computador

    print(f'{jogador} + {computador} é {par_impar}')

    # Verifica se a escolha do jogador é correta e atualiza vitória ou derrota
    if (par_impar % 2 == 0 and escolha == 'PAR') or (par_impar % 2 == 1 and escolha == 'ÍMPAR'):
        print(f'\033[1;32m{par_impar} é {escolha}! O jogador venceu.\033[m')
        vitoria += 1
    else:
        print(f'\033[1;31m{par_impar} é {escolha == "PAR" and "ÍMPAR" or "PAR"}! O computador venceu.\033[m')
        derrota += 1

    # Verifica se atingiu o limite de vitórias ou derrotas
    if vitoria == 3 or derrota == 3:
        break

# Mensagem final indicando o fim do jogo
print('FIM DE JOGO!')

# Mensagem final indicando se o jogador venceu, perdeu ou empatou
if vitoria > derrota:
    print(f'Parabéns! Você venceu o jogo com {vitoria} vitórias.')
elif derrota > vitoria:
    print(f'Infelizmente, você perdeu o jogo com {derrota} derrotas. Tente novamente.')
else:
    print('O jogo terminou em empate.')

# Exibe o placar final
print(f'Placar: Jogador {vitoria} x {derrota} Computador')


""" MINHA LÓGICA

# Importando módulo randint
from random import randint
# Inicializa as vitórias
vitoria = 0
derrota = 0
# Inicializa o loop infinito
while True:
    # Jogador escolhe PAR ou IMPAR
    escolha = str(input('PAR ou ÍMPAR? ')).strip().upper()
    # Jogador escolhe o valor
    jogador = int(input('Qual é o seu valor? 0 a 10 '))
    # Sorteia o e mostra o valor do computador
    computador = randint(0,10)
    print(f'Computador jogou {computador}')
    # Soma os valores para verificar se é par ou impar
    par_impar = jogador + computador
    # Se for par
    if par_impar % 2 == 0:
        # Informa os valores e o total
        print(f'{jogador} + {computador} é {par_impar}')
        # Se a escolha do jogador for PAR
        if escolha == 'PAR':
            print(f'\033[1;32m{par_impar} é PAR! O jogador escolheu {escolha} e venceu.\033[m')
            # Incrementa as vitórias do jogador
            vitoria += 1
        elif escolha == 'IMPAR':
            print(f'\033[1;31m{par_impar} é ÍMPAR! O jogador escolheu {escolha}, portanto o computador venceu.\033[m')
            derrota += 1
        else:
            # Jogador escolhe PAR ou IMPAR
            escolha = str(input('Somente PAR ou ÍMPAR ')).strip().upper()
    elif par_impar % 2 == 1:
        # Informa os valores e o total
        print(f'{jogador} + {computador} é {par_impar}')
        # Se a escolha do jogador for PAR
        if escolha == 'IMPAR':
            print(f'\033[1;32m{par_impar} é ÍMPAR! O jogador escolheu {escolha} e venceu.')
            # Incrementa as vitórias do jogador
            vitoria += 1
        elif escolha == 'PAR':
            print(f'\033[1;31m{par_impar} é ÍMPAR! O jogador escolheu {escolha}, portanto o computador venceu.\033[m')
            derrota += 1
        else:
            # Jogador escolhe PAR ou IMPAR
            escolha = str(input('Somente PAR ou ÍMPAR ')).strip().upper()
    if vitoria == 3 or derrota == 3:
        break
print('FIM DE JOGO!')
if vitoria == 1:
    print(f'Conseguiu apenas uma vitória!')
elif vitoria > 1:
    print(f'Parabéns. Foram {vitoria} vitórias!')
else:
    print('Tente novamente')
print(f'Placar Jogador {vitoria} x {derrota} Computador')

"""