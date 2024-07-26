# Exercício Python #045 - GAME: Pedra Papel e Tesoura - Aula 00 até 12 - Mundo 2
# Crie um programa que faça o computador jogar Jokenpô com você.
from time import sleep
from random import randint, choice
from emoji import emojize

# Versão mais recente - Preciso corrigir o erro na lógica do empate


def obter_valor(mensagem):
	while True:
		try:
			jogada = int(input(mensagem))
			while jogada not in [1, 2, 3]:
				print(f'\033[1;31m{'-' * 30}\033[m')
				print('\033[1;31mOpção inválida! Escolha novamente...\033[m')
				print(f'\033[1;31m{'-' * 30}\033[m')
				jogada = int(input(mensagem))
			return jogada
		except ValueError:
			print('O valor digitado não é permitido!')


def avaliação(player, computer):
	if player == computer:
		return emojize(':pessoa::aperto_de_mãos::rosto_de_robô:', language='pt')
	else:
		if player == 1 and computador == 3 or player == 2 and computer == 1 or player == 3 and computer == 2:
			return emojize('Jogador :pessoa: vence!', language='pt')
		else:
			return emojize('Computador :rosto_de_robô: vence!', language='pt')

print(f'{'-' * 30}')
print(emojize('VAMOS JOGAR JO :punho_levantado: KEN :mão_levantada: PO :mão_em_v_de_vitória:!', language='pt'))
print(f'{'-' * 30}')
sleep(1)
print('Escolha a sua jogada: ')
computador = randint(1,3)
jogador = obter_valor(emojize('[1] PEDRA :punho_levantado:\n[2] PAPEL :mão_levantada:\n[3] TESOURA :mão_em_v_de_vitória:\nEscolha: ', language='pt'))
print(f'{'-' * 30}')

resultado = avaliação(jogador, computador)

jogador_jogou = emojize('PEDRA :punho_levantado:' if jogador == 1 else 'PAPEL :mão_levantada:' if jogador == 2 else 'TESOURA :mão_em_v_de_vitória:', language='pt')
computador_jogou = emojize('PEDRA :punho_levantado:' if computador == 1 else 'PAPEL :mão_levantada:' if computador == 2 else 'TESOURA :mão_em_v_de_vitória:', language='pt')

print(emojize(f'{':rosto_de_robô: COMPUTADOR: ':<20}{computador_jogou:>10}', language='pt'))
sleep(1)
print(emojize(f'{':pessoa: JOGADOR: ':<20}{jogador_jogou:>10}', language='pt'))
sleep(1)
print(f'{'-' * 30}')
print(emojize(f'{jogador_jogou} ganha de {computador_jogou}', language='pt'))
sleep(1)
print(f'{'-' * 30}')
print(f'\033[1mResultado: {resultado}\033[m')
print(f'{'-' * 30}')

# Versão antiga
computador = choice(['Pedra', 'Papel', 'Tesoura'])

print(f'Escolha sua jogada.\n1 - Pedra\n2 - Papel\n3 - Tesoura')

while True:
	try:
		escolha = int(input('Digite o número correspondente à sua escolha: '))
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
	except ValueError:
		print('Por favor, digite um número válido.')
		continue