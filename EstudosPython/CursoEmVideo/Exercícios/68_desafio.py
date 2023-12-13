# Exercício Python #068 - Jogo do Par ou Ímpar - Aula 00 até 15 - Mundo 2
# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from time import sleep
from random import randint
from emoji import emojize

vitorias = 0
while True:

    par_ou_impar = int(input(emojize(':tecla_2: Par ou :tecla_1: Ímpar? ', language='pt')))
    verdade = True
    while verdade:
        if par_ou_impar != 1 and 2:
            print('Somente 2 para PAR ou 1 para ÍMPAR')
            par_ou_impar = int(input(''))
        else:
            verdade = False

    jogador = int(input(emojize(':teclado: Digite o valor: ', language='pt')))
    print(f'Você escolheu {'par' if par_ou_impar == 2 else 'ímpar'} e jogou {jogador}...')
    sleep(1)

    computador = randint(1, 2)
    print(f'Computador jogou {computador}...')
    sleep(1)

    soma = jogador + computador
    print(f'Total é {soma}. ', end='')
    sleep(1)

    par = soma % 2 == 0
    impar = not par
    print('Deu par' if par else 'Deu ímpar')
    sleep(1)

    if par and par_ou_impar == 2 or impar and par_ou_impar == 1:
        print('Vitória!')
        vitorias += 1
    else:
        print('Derrota!')
        break

sleep(1)
print(f'Vitórias consecutivas: {vitorias}')
