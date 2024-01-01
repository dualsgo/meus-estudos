# Exercício Python #091 - Jogo de Dados em Python - Aula 00 até 19 - Mundo 3
# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from time import sleep
from random import randint

# Inicializa uma lista vazia para armazenar os jogadores
jogadores = []

# Loop para criar 4 jogadores
for indice, _ in enumerate(range(4), 1):
    # Cria um dicionário para representar um jogador
    jogador = {'nome': f'Jogador({indice})', 'pontuacao': randint(1, 6)}

    # Imprime a pontuação do jogador
    print(f"O {jogador['nome']} tirou {jogador['pontuacao']}")

    # Aguarda por um segundo para simular um intervalo entre os jogadores
    sleep(1)

    # Adiciona o jogador à lista de jogadores
    jogadores.append(jogador)

# Imprime o título do ranking
print(f'{"Ranking":^20}')

# Ordena a lista de jogadores com base na pontuação, em ordem decrescente
jogadores = sorted(jogadores, key=lambda jogador: jogador['pontuacao'], reverse=True)

# Imprime o ranking com a posição, nome do jogador e pontuação
for indice, jogador in enumerate(jogadores, 1):
    print(f'{indice:<5} {jogador["nome"]} - {jogador["pontuacao"]}')