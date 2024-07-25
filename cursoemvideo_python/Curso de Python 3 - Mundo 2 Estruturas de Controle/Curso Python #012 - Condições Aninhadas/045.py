# Exercício Python #045 - GAME: Pedra Papel e Tesoura
# Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.

import random
computador = random.choice(['Pedra', 'Papel', 'Tesoura'])

print(f'Escolha sua jogada.\n1 - Pedra\n2 - Papel\n3 - Tesoura')

while True:
	try:
		escolha = int(input('Digite o número correspondente à sua escolha: '))

	except ValueError:
		print('Por favor, digite um número válido.')
		continue

	if escolha < 1 or escolha > 3:
		print('Por favor, digite um número entre 1 e 3.')
		continue

	usuário = 'Pedra' if escolha == 1 else 'Papel' if escolha == 2 else 'Tesoura'

	print(f'{'Computador:':<11}{computador:>10}\n{'Usuário:':<11}{usuário:>10}')

	if usuário == 'Pedra' and computador == "Tesoura" or usuário == 'Papel' and computador == 'Pedra' or usuário == 'Tesoura' and computador == "Papel":
		print(f'{f'Venceu! {usuário} vence {computador}.'}')

	elif usuário == computador:
		print(f'{'Empate!'}')

	else:
		print(f'{f'Perdeu! {computador} vence {usuário}.'}')
	break