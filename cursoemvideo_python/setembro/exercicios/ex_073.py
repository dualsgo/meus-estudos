"""Desafio 073 - Tupla com times de futebol (Aula 01 a 16): Crie uma tupla preenchida com os 20 primeiros colocados na tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre

- Apenas os 5 primeiros colocados
- Apenas os últimos 4 colocados
- Uma lista com os times em ordem alfabética
- Em que posição está o time da Chapecoense
"""
# Criar a tupla com os vinte primeiros colocados
classificacao = ("Palmeiras", "Botafogo", "Grêmio", "Red Bull Bragantino", "Atlético-MG", "Flamengo", "Athletico", "Fluminense", "Cuiabá", "Corinthians", "São Paulo", "Fortaleza", "Internacional", "Santos", "Vasco", "Bahia", "Cruzeiro", "Goiás", "Coritiba", "América-MG")

# Exibir todos os times por ordem de classificação:
print("\nTodos os times por ordem de classificação:")
for posicao, time in enumerate(classificacao, start=1):
    print(f'{posicao:2} - {time}')

# Exibir os cinco primeiros
lideres = classificacao[:5]
print('\n\033[1;31mOs cinco primeiros times na tabela são:\033[m')
for posicao, time in enumerate(lideres, start=1):
    print(f'{posicao:2} - {time}')

# Exibir os 4 últimos
print(f'\nOs times na zona de rebaixamento são:')
zona_rebaixamento = classificacao[-4:]
for posicao, time in enumerate(zona_rebaixamento, start=len(classificacao) - 3):
    print(f'{posicao:2} - {time}')

# Em ordem alfabética
print(f'\nOs times participantes do Campeonato Brasileiro 2023 em ordem alfabética:')
ordem_alfabetica = sorted(classificacao)
for posicao, time in enumerate(ordem_alfabetica, start=1):
    print(f'{posicao:2} - {time}')

# Mostrar a posição do Vasco
posicao_time = classificacao.index("Vasco") + 1
print(f'\nA posição do Vasco da Gama é {posicao_time}º\n')

