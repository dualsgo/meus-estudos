# Exercício Python #068 - Jogo do Par ou Ímpar
# Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
placar = 0
while True:
	try:
		jogador = int(input('Digite um valor: '))
	except ValueError:
		print(f'Apenas números.')
		continue

	while True:
		par_ímpar = input('Par ou Ímpar? [P/I]').strip().upper()
		if par_ímpar not in ('I', 'P'):
			continue
		else:
			break

	computador = randint(0, 10)
	soma = computador + jogador

	if par_ímpar == 'I' and soma % 2 == 1 or par_ímpar == 'P' and soma % 2 == 0:
		print(f'Vitória! Vamos de novo...')
		placar += 1
	else:
		print(f'Derrota! Você venceu {placar} vezes seguidas.' if placar > 0 else 'Game over!')
		break