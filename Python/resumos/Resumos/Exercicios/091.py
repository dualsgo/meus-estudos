# Exercício Python #091 - Jogo de Dados em Python
# Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep

jogadores = {f'jogador{i}': randint(1, 6) for i in range(1, 5)}

print(f'{'Sorteio dos jogadores:':^25}')
for jogador, pontuação in jogadores.items():
    sleep(1)
    print(f'{jogador} tirou o número {pontuação}')

ranking = sorted(jogadores, key=jogadores.get, reverse=True)

print(f'{'Ranking dos jogadores:':^25}')
for i, jogador in enumerate(ranking, start=1):
    sleep(1)
    print(f'{i}º lugar: {jogador} com {jogadores[jogador]} pontos')