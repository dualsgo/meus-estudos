# Exercício Python #031 - Custo da Viagem - Aula 00 até 09 - Mundo 1
# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

from random import randint
# Tarefa 1: Perguntar a distância de uma viagem em
distancia = randint(100, 500)
print(f'Você está prestes a fazer uma viagem de {distancia}Km')

# Tarefa 2: Calcular o preço da viagem
viagem_curta = distancia <= 200

preco = .5 if viagem_curta else .45
preco_viagem = distancia * preco

print(f'O preço da sua viagem será R$ {preco_viagem:.2f}')

# Versão 2 - Com validação

while True:
	try:
		distancia = float(input('Digite a distância em KM: '))
		print(f'Sua viagem de {distancia}Km irá custar:', f'R$ {distancia * (.5 if distancia < 201 else 0.45):.2f}')
		break
	except ValueError:
		print(f'Apenas valores numéricos')