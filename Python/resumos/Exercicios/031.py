# Exercício Python #031 - Custo da Viagem
# Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.


while True:
	try:
		distancia = float(input('Digite a distância em KM: '))
	except ValueError:
		print(f'Apenas valores numéricos')
	else:
		print(f'Sua viagem de {distancia}Km irá custar:', f'R$ {distancia * (.5 if distancia < 201 else 0.45):.2f}')
		break