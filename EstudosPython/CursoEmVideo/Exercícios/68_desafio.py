# Exercício Python #068 - Jogo do Par ou Ímpar - Aula 00 até 15 - Mundo 2
# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from time import sleep
from random import randint
from emoji import emojize

vitorias = 0

# Loop principal do jogo
while True:
    jogador = int(input(emojize(':teclado: Digite o valor: ', language='pt')))

    # Solicitação para o jogador escolher ímpar (1) ou par (2)
    par_ou_impar = int(input(emojize(':tecla_1: Ímpar\n:tecla_2: Par\n', language='pt')))

    # Loop para garantir que o jogador escolha apenas entre 1 ou 2
    while True:
        if 1 != par_ou_impar != 2:
            print('Somente 2 para PAR ou 1 para ÍMPAR')
            par_ou_impar = int(input(''))
        else:
            break

    # Exibe a escolha do jogador
    print(emojize(f':moai: Jogador: É {"par" if par_ou_impar == 2 else "ímpar"} e jogou {jogador}...', language='pt'))
    sleep(1)

    # O computador escolhe aleatoriamente entre 1 e 2
    computador = randint(1, 2)
    print(emojize(f':rosto_de_robô: Computador: É {'par' if jogador == 1 else 'ímpar'} e jogou {computador}...', language='pt'))
    sleep(1)

    # Calcula a soma dos valores jogados
    soma = jogador + computador
    print(f'Total é: {soma}. ', end='')
    sleep(1)

    # Verifica se a soma é par ou ímpar
    par = soma % 2 == 0
    impar = not par
    print('Deu par!' if par else 'Deu ímpar!')
    sleep(1)

    # Determina o vencedor com base na escolha do jogador e no resultado
    if par and par_ou_impar == 2 or impar and par_ou_impar == 1:
        print(emojize(':marca_de_seleção: Vitória!', language='pt'))
        vitorias += 1
    else:
        print(emojize(':xis: Derrota!', language='pt'))
        break  # Encerra o jogo se o jogador perder

# Exibe o número de vitórias consecutivas
sleep(1)
print(emojize(f':troféu: Vitórias consecutivas: {vitorias}', language='pt'))
