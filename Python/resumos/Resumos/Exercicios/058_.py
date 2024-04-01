# Versão do computador

from time import sleep

def adivinhacao_computador(numero):
	limite_inferior = 1
	limite_superior = 1000
	palpite = limite_superior // 2

	tentativas = 1

	while palpite != numero:
		print(f"O computador palpita {palpite}.")
		sleep(1)
		if palpite < numero:
			limite_inferior = palpite + 1
		else:
			limite_superior = palpite - 1

		palpite = (limite_inferior + limite_superior) // 2
		tentativas += 1

	print(f"O computador acertou o número {numero} em {tentativas} tentativas.")

numero_escolhido = int(input("Escolha um número entre 1 e 1000: "))
adivinhacao_computador(numero_escolhido)