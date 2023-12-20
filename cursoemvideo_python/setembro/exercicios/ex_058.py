"""Desafio 058 - Jogo da Adivinhação 2.0 (Aula 01 a 14): Melhore o jogo do desafio 28 onde o computador vai pensar em um número entre 0 e 10, só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
"""
# Fazer o computador pensar em um número com random
from random import randint
# O intervalo é entre 0 e 10
computador = randint(0, 10)
# O jogador dá seu palpite
jogador = int(input('Digite seu palpite: '))
# Inicializa e anota o número de palpites
palpites = 1
# Enquanto o jogador não acertar, o programa irá solicitar que o usuário de outro palpite
while jogador != computador:
    print('\033[7;31;40mVOCÊ ERROU!\033[m')
    # Incrementa os palpites
    palpites += 1
    # Irá mostrar se o palpite está maior ou menor
    if jogador > computador:
        print('\033[7;31;40mÉ MENOS... TENTE OUTRA VEZ!\033[m')
    else:
        print('\033[7;32;40mÉ MAIS! TENTE MAIS UMA VEZ.\033[m')
    # Solicita nova tentativa
    jogador = int(input('Tente novamente: '))
if palpites <= 3:
    print(f'\033[7;32;40mVOCÊ ACERTOU em {palpites} tentativas\033[m\n\033[7;31;40mExcelente!\033[m')
else:
    print(f'\033[7;32;40mVOCÊ ACERTOU em {palpites} tentativas\033[m\n\033[7;31;40mConsegue fazer melhor?\033[m')