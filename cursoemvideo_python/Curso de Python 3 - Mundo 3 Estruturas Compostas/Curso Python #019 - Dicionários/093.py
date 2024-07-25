# Exercício Python #093 - Cadastro de Jogador de Futebol
# Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

informações = dict()
partidas = list()

informações['nome'] = input('Nome do jogador: ')
informações['partidas'] = int(input('Quantidade de partidas: '))

for i in range(1, informações['partidas']+1):
	partidas.append(int(input(f'Quantos gols marcados na partida {i}? ')))

informações['gols'] = partidas
informações['total'] = sum(partidas)

for c, v in informações.items():
	print(f'{c}: {v}')

for i, v in enumerate(informações['gols'], 1):
	print(f'Partida {i}: {v} gols')