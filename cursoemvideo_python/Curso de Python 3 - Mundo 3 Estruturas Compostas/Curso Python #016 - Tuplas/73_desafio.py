# Exercício Python #073 - Tuplas com Times de Futebol - Aula 00 até 16 - Mundo 3
# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

# Lista de times do Brasileirão 2023
times = ('Palmeiras - SP', 'Gremio - RS', 'Atlético Mineiro - MG', 'Flamengo - RJ', 'Botafogo - RJ', 'Red Bull Bragantino - SP', 'Fluminense - RJ', 'Athletico - PR', 'Internacional - RS', 'Fortaleza - CE', 'São Paulo - SP', 'Cuiaba - MT', 'Corinthians - SP', 'Cruzeiro - MG', 'Vasco da Gama - RJ', 'Bahia - BA', 'Santos - SP', 'Goias - GO', 'Coritiba - PR', 'America - MG')

# Imprime os participantes do Brasileirão 2023 em ordem alfabética
print('\033[1mPARTICIPANTES BRASILEIRÃO 2023\033[m')
times_em_ordem = sorted(times)
for equipe in times_em_ordem:
    print(f'{equipe}')
print('\n')

# Imprime a tabela completa do Brasileirão 2023
print('TABELA BRASILEIRÃO 2023')
for posicao, equipe in enumerate(times):
    print(f'{posicao+1:2}º - {equipe}')
print('\n')

# Separa as equipes nas diferentes zonas (Libertadores, Pré-Libertadores, Sul-Americana, Zona Neutra e Rebaixamento)
libertadores = times[:4]
print('\033[1;32mZona da Libertadores - Brasileirão 2023\033[m')
for posicao, equipe in enumerate(libertadores):
    print(f'{posicao+1:2}º - {equipe}')

pre_libertadores = times[4:6]
print('\033[1;36mZona da Pré Libertadores - Brasileirão 2023\033[m')
for posicao, equipe in enumerate(pre_libertadores, start=4):
    print(f'{posicao+1:2}º - {equipe}')

sulamericana = times[6:14]
print('\033[1;34mZona da Sul-Americana - Brasileirão 2023\033[m')
for posicao, equipe in enumerate(sulamericana, start=6):
    print(f'{posicao+1:2}º - {equipe}')

nada = times[14:16]
print('\033[1;37mZona Neutra - Brasileirão 2023\033[m')
for posicao, equipe in enumerate(nada, start=14):
    print(f'{posicao+1:2}º - {equipe}')

rebaixados = times[16:]
print('\033[1;31mZona de Rebaixamento - Brasileirão 2023\033[m')
for posicao, equipe in enumerate(rebaixados, start=17):
    print(f'{posicao:2}º - {equipe}')
print('\n')

# Letra D - Imprime a posição do CR Vasco da Gama - RJ
print('Posição do CR Vasco da Gama- RJ')
posicao_vasco = times.index('CR Vasco da Gama - RJ') + 1
print(f'O Vasco terminou o campeonato em {posicao_vasco}º')


