# Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from emoji import emojize
from random import randint


def palpite(mensagem):
	while True:
		try:
			return int(input(mensagem))
		except ValueError:
			print('Opção inválida! Digite um número válido.')


print(emojize(f'{':videogame: Vamos jogar! :videogame:':^30}\nAcabei de pensar em um número entre 1 e 100. Você consegue adivinhar?', language='pt'))

computador = randint(1, 100)
tentativa = 1

while True:
	usuário = palpite(f'{tentativa}ª tentativa: ')

	if usuário < 1 or usuário > 100:
		print('Apenas valores entre 1 e 100.')
		continue

	if usuário == computador:
		print(f'Acertou! Era mesmo {computador}. Foram {tentativa} tentativas.')
		break
	else:
		dica = emojize('\033[1;32mMaior :seta_para_cima:\033[m' if usuário < computador else '\033[1;31mMenor :seta_para_baixo:\033[m', language='pt')
		print(f'Errou! É {dica} que {usuário}. Tente novamente...')
		tentativa += 1
		continue