# Exercício Python #028 - Jogo da Adivinhação v.1.0
# Exercício Python 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

sleep(1)
print(f'Vou pensar em um número entre 1 e 10 e quero que tente adivinhar. Ok?')
sleep(1)
computador = randint(1, 10)
acertou = True

while acertou:
	try:
		sleep(1)
		jogador = int(input('Palpite: '))
		sleep(1)
		print('Analisando...')
		sleep(1)
		acertou = computador != jogador
	except ValueError:
		print('Apenas valores numéricos!')
	else:

		if jogador == computador:
			print(f'Acertou! Era mesmo o número {computador}')
			break
		else:
			print(f'Errou! Não é o número {jogador}. Vamos de novo...')