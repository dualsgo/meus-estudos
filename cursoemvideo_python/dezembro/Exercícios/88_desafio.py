# Exercício Python #088 - Palpites para a Mega Sena - Aula 00 até 18 - Mundo 3
# Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep
jogos = []  # Lista principal

quantidade_jogos = int(input('Digite a quantidade de jogos que deseja simular: '))

for jogo in range(quantidade_jogos):
    bilhete = []  # Lista com cada bilhete de seis números

    while len(bilhete) < 6:
        n = randint(1, 60)
        if n in bilhete:
            n = randint(1, 60)
        else:
            bilhete.append(n)

        jogos.append(bilhete[:])

    bilhete.sort()
    print(f'Jogo {jogo+1}: {bilhete}')
    sleep(1)
    bilhete.clear()