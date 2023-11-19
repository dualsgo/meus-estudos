"""
Desafio 088 -  (Aula 01 a 18): Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa deve perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
"""
from random import randint

# Inicializa uma lista que vai conter os jogos, cada jogo é uma sub-lista com 6 números
bilhete = []

# Solicita ao usuário a quantidade de jogos que deseja gerar
qtde_jogos = int(input('Quantos jogos deseja simular? '))

# Loop para a quantidade de jogos solicitada
for sorteio in range(qtde_jogos):
    # Cria uma nova lista para representar um jogo
    jogo = []

    # Exibe o número do jogo sorteado
    print(f'\033[1;31m{sorteio + 1}º JOGO SORTEADO\033[m')

    # Loop para gerar 6 números aleatórios para o jogo atual
    for i in range(6):
        # Gera um número aleatório entre 1 e 60
        numero = randint(1, 60)

        # Garante que o número sorteado não se repita dentro do mesmo jogo
        while numero in jogo:
            numero = randint(1, 60)

        # Adiciona o número sorteado ao jogo
        jogo.append(numero)

        # Exibe o número sorteado
        print(f'\033[1;32m{i + 1}º número sorteado: {numero}\033[m')

    # Adiciona o jogo à lista de bilhetes
    bilhete.append(sorted(jogo))

# Exibe os bilhetes gerados
print('SEUS BILHETES SÃO: ')
for simulacao in bilhete:
    print(simulacao)

