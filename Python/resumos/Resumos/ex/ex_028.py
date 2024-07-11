# Exercício Python 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint


def palpite(mensagem):
	while True:
		try:
			return int(input(mensagem))
		except ValueError:
			print('Opção inválida! Digite um número válido.')


print(f'{'Vamos jogar!':^20}')

computador = randint(1, 100)
tentativa = 1

while True:
	usuário = palpite(f'{tentativa}ª tentativa: ')

	if usuário < 1 or usuário > 100:
		print('Apenas valores entre 1 e 100.')
		continue

	if usuário == computador:
		print(f'Acertou! Foram {tentativa} tentativas.')
		break
	else:
		dica = '\033[1;32mMaior\033[m' if usuário < computador else '\033[1;31mMenor\033[m'
		print(f'Errou! É {dica}. Tente novamente...')
		tentativa += 1
		continue