# Exercício Python #045 - GAME: Pedra Papel e Tesoura
# Crie um programa que faça o computador jogar Jokenpô com você.
from time import sleep
from random import randint
# Tarefa 1: Receber a jogada do jogador e do computador
computador = randint(1, 3)
print('Jogador, faça a sua jogada:')
print('[1] Pedra [2] Papel [3] Tesoura')
jogador = int(input(''))

pedra = 1
papel = 2
tesoura = 3

print('Você jogou', end=' ')
sleep(1)
# Tarefa 2: Definir as regras para cada combinação
if jogador == pedra:
    print('pedra')
    sleep(1)
    print('O computador jogou', end=' ')
    sleep(1)
    if computador == papel:
        print('papel')
        sleep(1)
        print('Computador vence!')
    elif computador == tesoura:
        print('tesoura')
        sleep(1)
        print('Jogador vence!')
elif jogador == papel:
    print('papel')
    sleep(1)
    print('O computador jogou', end=' ')
    sleep(1)
    if computador == pedra:
        print('pedra')
        sleep(.5)
        print('Jogador vence!')
    elif computador == tesoura:
        print('tesoura')
        sleep(1)
        print('Computador vence!')
elif jogador == tesoura:
    print('tesoura')
    sleep(1)
    print('O computador jogou', end=' ')
    sleep(1)
    if computador == pedra:
        print('pedra')
        sleep(1)
        print('Computador vence!')
    elif computador == papel:
        print('papel')
        sleep(1)
        print('Jogador vence!')
else:
    print('Escolha inválida!')
# Tarefa 3: Exibir o vencedor