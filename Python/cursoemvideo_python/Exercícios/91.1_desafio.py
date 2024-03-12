# Exercício Python #091 - Jogo de Dados em Python - Aula 00 até 19 - Mundo 3
# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from time import sleep
from random import randint

# Inicializa uma lista vazia para armazenar os jogadores
jogadores = []

# Loop para criar 4 jogadores
for indice, _ in enumerate(range(4)):
    # Cria um dicionário para representar um jogador
    jogador = {'nome': f'Jogador({indice + 1})', 'pontuacao': randint(1, 6)}

    # Imprime a pontuação do jogador
    print(f"O {jogador['nome']} tirou {jogador['pontuacao']}")

    # Aguarda por um segundo para simular um intervalo entre os jogadores
    sleep(1)

    # Adiciona o jogador à lista de jogadores
    jogadores.append(jogador)

# Imprime o título do ranking
print(f'{"Ranking (sem sorted)":^30}')

# Implementa o algoritmo de ordenação Bubble Sort
# O Bubble Sort é um algoritmo de ordenação simples que percorre repetidamente a lista, compara elementos adjacentes e os troca se estiverem na ordem errada. Esse processo continua até que a lista esteja ordenada.

# n = len(jogadores): Obtém o número total de jogadores na lista. Isso servirá para definir os limites do loop.
n = len(jogadores)

# for i in range(n): O primeiro loop (i) percorre toda a lista.
for i in range(n):

    # for j in range(0, n-i-1): O segundo loop (j) percorre a lista até o elemento n-i-1. A ideia é que após cada passagem do loop externo, o maior elemento já está na posição correta, então podemos reduzir o alcance do loop interno.
    for j in range(0, n - i - 1):

        # Compara as pontuações e troca se necessário
        # if jogadores[j]['pontuacao'] < jogadores[j+1]['pontuacao']:: Compara as pontuações de dois jogadores adjacentes. Se o jogador na posição j tiver uma pontuação menor que o jogador na posição j+1, então precisamos trocar os jogadores para colocar o jogador com a maior pontuação primeiro.

        # jogadores[j], jogadores[j+1] = jogadores[j+1], jogadores[j]: Realiza a troca dos jogadores. Isso é feito usando a técnica de desempacotamento de tuplas no Python. Se a condição do passo anterior for verdadeira, trocamos os jogadores nas posições j e j+1.
        if jogadores[j]['pontuacao'] < jogadores[j + 1]['pontuacao']:
            jogadores[j], jogadores[j + 1] = jogadores[j + 1], jogadores[j]
# Imprime o ranking com a posição, nome do jogador e pontuação
for indice, jogador in enumerate(jogadores, 1):
    print(f'{indice:<5} {jogador["nome"]} - {jogador["pontuacao"]}')