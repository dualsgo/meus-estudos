# Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

while True:
	try:
		km = float(input('Digite a distância em Km: '))
		custo = km * (.5 if km <= 200 else .45)
		print(f'{'Custo da viagem:':<20}{f'R$ {custo:.2f}'}')
		break
	except Exception as erro:
		print(f'Erro: {erro}\nTente novamente.')