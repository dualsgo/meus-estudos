# Exercício Python #058 - Jogo da Adivinhação v2.0
# Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
computador = randint(1, 999)

print(f'Estou pensando em um número. Tente adivinhar...')
palpites = 1
while True:
	try:
		palpite = int(input(f'{palpites}º Palpite: '))
	except ValueError:
		print(f'Calma aí, paizão. Esse valor não é válido.')
	else:

		if palpite < computador:
			print(f'É maior...')
		elif palpite > computador:
			print(f'É menor...')
		else:
			print(f'Parabéns. Acertou com {palpites} palpites' if palpites > 1 else 'Uau, acertou de primeira!')
			break

		palpites += 1